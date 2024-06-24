import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, StackingRegressor
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
import lightgbm as lgb
from scipy.stats import randint, uniform
import shap

# Load the dataset
data = pd.read_csv('house_prices.csv')

# Display basic information about the dataset
print(data.info())

# Display the first few rows of the dataset
print(data.head())

# Drop columns with too many missing values and separate target variable
data = data.drop(columns=['Alley', 'PoolQC', 'Fence', 'MiscFeature', 'Id'])
y = data['SalePrice']
X = data.drop(columns=['SalePrice'])

# Handle outliers: Remove data points with sale prices outside the 99th percentile
upper_bound = y.quantile(0.99)
lower_bound = y.quantile(0.01)
mask = (y >= lower_bound) & (y <= upper_bound)
X = X[mask]
y = y[mask]

# Apply log transformation to the target variable
y = np.log1p(y)

# Define numerical and categorical columns
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Create preprocessing pipelines for numerical and categorical data
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define advanced models for comparison
models = {
    'Random Forest': RandomForestRegressor(random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42),
    'XGBoost': xgb.XGBRegressor(random_state=42),
    'LightGBM': lgb.LGBMRegressor(random_state=42)
}

# Evaluate each model using cross-validation
for name, model in models.items():
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])
    scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
    print(f'{name} MAE: {np.mean(-scores):.4f} (+/- {np.std(-scores):.4f})')

# Choose the best model and perform hyperparameter tuning using RandomizedSearchCV
param_distributions = {
    'regressor__n_estimators': randint(100, 500),
    'regressor__max_depth': randint(3, 20),
    'regressor__learning_rate': uniform(0.01, 0.1)
}

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', xgb.XGBRegressor(random_state=42))
])

random_search = RandomizedSearchCV(pipeline, param_distributions, n_iter=50, cv=5, n_jobs=-1, scoring='neg_mean_absolute_error', random_state=42)
random_search.fit(X_train, y_train)

best_model = random_search.best_estimator_
print(f'Best Parameters: {random_search.best_params_}')
print(f'Best Mean Absolute Error: {-random_search.best_score_:.4f}')

# Feature importance using SHAP values
best_model.fit(X_train, y_train)
explainer = shap.Explainer(best_model.named_steps['regressor'])
shap_values = explainer(best_model.named_steps['preprocessor'].transform(X_test))

# Plot SHAP values for feature importance
shap.summary_plot(shap_values, X_test, feature_names=numerical_cols.tolist() + list(best_model.named_steps['preprocessor'].named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_cols)))

# Visualize actual vs predicted prices
y_pred = best_model.predict(X_test)
y_pred = np.expm1(y_pred)  # Inverse of log transformation
y_test_exp = np.expm1(y_test)  # Inverse of log transformation

plt.figure(figsize=(10, 6))
plt.scatter(y_test_exp, y_pred, alpha=0.3)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()

# Ensemble Learning with Stacking
estimators = [
    ('rf', RandomForestRegressor(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingRegressor(n_estimators=100, random_state=42)),
    ('xgb', xgb.XGBRegressor(n_estimators=100, random_state=42)),
    ('lgb', lgb.LGBMRegressor(n_estimators=100, random_state=42))
]

stacking_regressor = StackingRegressor(
    estimators=estimators,
    final_estimator=LinearRegression()
)

ensemble_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('stacking', stacking_regressor)
])

# Train and evaluate the stacking model
ensemble_model.fit(X_train, y_train)
y_pred_ensemble = ensemble_model.predict(X_test)
y_pred_ensemble = np.expm1(y_pred_ensemble)  # Inverse of log transformation
ensemble_mae = mean_absolute_error(y_test_exp, y_pred_ensemble)
print(f'Stacking Model MAE: {ensemble_mae:.4f}')
