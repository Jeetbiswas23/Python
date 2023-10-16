"""
# 1 Question
or_2r = 3
print(or_2r)
# 2nd Question
#Backslash
a= 3*\
4*\
5*\
3*\
8
print(a)
# Parathesis
b= (3*
4*
5*
3*
8)
print(b)
 #3 Question
jk3_ = 2+5j
print(jk3_)
#4 Question
cv = "Hello World"
print(type(cv))
#5  Question
yt =2
tg =3.4
print(type(yt))
print(type(tg))
#input from the user
a =float(input("ENTER YOUR NUMBER"))
b =int(input("ENTER YOUR NUMBER"))
df = a+b
print("The Sum is",df)

age =30
a = str(age)
print(a)


marks = int(input("Enter your Marks"))
if (marks >=90) :
    print("A")
elif (marks>=80):
    print("B")
elif (marks>=70):
    print(("C"))
else:
    print("FAIL")

a = int(input("enter your number"))
if(a%2==0):
    print("EVEN")
else:
    print("ODD")

#Leap year
b =int(input("Enter your year"))
if((b%4==0 and b%100 !=0) or (b%400==0)):
    print("Leap year")
else:
    print("not leap year")

#Electricity Bill
n =int(input("Enter your units"))
if(n<=100):
    print(n*10)
elif(n>100 and n<=200):
    print(n*20)
elif(n<200 and n>=300):
    print(n*30)
elif(n>300):
    print(n*40)
print(n)


#Temp converter
f = float(input("enter your fahrenheit degree"))
c =float(input("enter your celcius degree"))
unit = input("Convert to (C/F)")
p =0
q=0
if(unit=="C"):
    p = (f - 32) * 5 / 9
elif(unit=="F"):
    q=(c*9/5)+32
print("Fahrenhiet to celcius",p)
print("Celcius to Fahrenhiet",q)


#BMI
w=float(input("Enter your weight in kg"))
h =float(input("Enter your height in m"))
BMI =w/(h**2)
if (BMI < 18.5):
    print("Underweight")
elif(BMI > 18.5 and BMI <=24.9):
    print("Normal Weight")
elif(BMI>25 and BMI<=29.9):
    print("Overweight")
elif(BMI>=30):
    print("Obese")
else:
    print("Have a nice day")

# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not Armstrong number")



rows = 6
for i in range(rows):
    for j in range(i):
        print("*", end ="\t")
    print()

num_rows=int(input("Enter your row"))
for i in range(num_rows):
    for j in range(num_rows-i-1):
        print(" ",end =" ")
    for k in range(i+1):
        print("*", end=" ")
    print()



def print_rectangle(n, m):
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n-1 or
                    j == 0 or j == m-1):
                print("*", end="")
            else:
                print(" ", end="")

        print()


# Driver program for above function
rows = 6
columns = 20
print_rectangle(rows, columns)

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()

#Factorial of a number
n = int(input("Enter your number"))
fact = 1

for i in range(1, n+1):
	fact = fact * i

print("The factorial of ",n, "is : ", end="")
print(fact)

#countdown Timer                -------|    This has to be done😀
import time

def countdown(n):
    if n < 0:
        print("Invalid duration!")
        return

    while n >= 0:
        mins, secs = divmod(n, 60)
        print(f'{mins:02}:{secs:02}', end='\r')
        if n == 0:
            print("\nTime's up!")
            break
        time.sleep(1)
        n -= 1

# Get user input for the countdown duration
try:
    n = int(input("Enter the number of seconds for the countdown: "))
    countdown(n)
except ValueError:
    print("Please enter a valid integer!")




#Sum of square of number        _______|


#Guess a number guess
import random


def guess_number(min_value, max_value):
    # Computer randomly selects a number between min_value and max_value
    number_to_guess = random.randint(min_value, max_value)
    guess = None
    attempts = 0

    print(f"Guess a number between {min_value} and {max_value}!")

    while guess != number_to_guess:
        try:
            # Player provides their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")

        except ValueError:
            print("Please enter a valid integer!")


# Get range from the user
try:
    min_value = int(input("Enter the minimum value for the guessing range: "))
    max_value = int(input("Enter the maximum value for the guessing range: "))

    if min_value < max_value:
        guess_number(min_value, max_value)
    else:
        print("The minimum value should be less than the maximum value.")

except ValueError:
    print("Please enter valid integers for the range!")

import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get audio command from the user
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        command = ""

        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not hear your request.")
        except sr.RequestError:
            print("Sorry, the service is unavailable.")
        return command.lower()

def main():
    speak("Hello, I'm Jarvis. How can I assist you?")
    while True:
        command = get_audio()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "how are you" in command:
            speak("I'm just a program, so I don't have feelings, but I'm operating optimally!")
        elif "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()

def sum(a,d):
    f=a+d
    return f
sum_res = sum(2,3)
print(sum_res)

i=1
while i<3:
    j=0
    while j<5:
        j = j +1
        if j==3:
            continue
        print(j, end = " ")
    i = i +1
    


import math

def is_prime(a):
    if a <= 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

a = int(input("Enter your number: "))
result = is_prime(a)

if result:
    print("This is a prime number.")
else:
    print("This is not a prime number.")

print(result)


w=int(input("Enter the range"))
for i in range(2,w+1):
    if(range(i)):
        print(i)


n = 10
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()


#Question 4 of class document
def check_balance(balance):
    return balance


def deposit(balance, amount):
    balance += amount
    return balance


def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        return balance, True
    else:
        return balance, False


balance = 0.0

while True:
    # Display Menu
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")

    # Get user's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", check_balance(balance))
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = deposit(balance, amount)
        print("Deposited $" + str(amount) + ". New Balance: $" + str(balance))
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        balance, success = withdraw(balance, amount)
        if success:
            print("Withdrew $" + str(amount) + ". New Balance: $" + str(balance))
        else:
            print("Insufficient funds.")
    elif choice == 4:
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid choice. Please select a valid option.")



#List
my_list=[1,4,9,8]
a=my_list.append(6)
b=my_list.insert(2,7)
c=my_list.remove(1)
d=len(my_list)
print(a)
print(b)
print(c)
print(d)

li=[1,2,3,4]
li2=[1,2,6,7]
a=li+li2
print(a)

li=[1,2,3]
a=1 in li
print(a)

li=[3,1,2]
a=li.sort()
print(a)

li=["a","d","c"]
for item in li:
    print(item)


import time

def countdown_timer(total_seconds):
    while total_seconds > 0:
        if total_seconds == 1:
            print(str(total_seconds) + " second remaining...")
        else:
            print(str(total_seconds) + " seconds remaining...")
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")

duration = int(input("Enter the countdown duration (in seconds): "))

countdown_timer(duration)

tasks = []

while True:
    print("\nTo-Do List Manager:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Clear Completed Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task_description = input("Enter task description: ")
        tasks.append({"description": task_description, "completed": False})
        print("Task added!")

    elif choice == 2:
        if not tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(tasks, 1):
                status = "Completed" if task["completed"] else "Not completed"
                print(str(index) + ". " + task['description'] + " - " + status)

    elif choice == 3:
        task_number = int(input("Enter task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number!")

    elif choice == 4:
        tasks = [task for task in tasks if not task["completed"]]
        print("Completed tasks cleared!")

    elif choice == 5:
        print("Thank you for using the to-do list manager!")
        break

    else:
        print("Invalid choice. Please select a valid option.")

s="abcd"
s[0]='c'
print(s)

n = int(input("Enter the now of rows"))
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()



def display_menu():
    print("\nOptions:")
    print("1. View Inventory")
    print("2. Add a New Product")
    print("3. Update Product Quantity")
    print("4. Calculate Total Inventory Value")
    print("5. Exit")


def view_inventory(inventory):
    print("\nInventory:")
    for product in inventory:
        print("ID:", product['product_id'])
        print("Product Name:", product['product_name'])
        print("Unit Price: $", product['unit_price'])
        print("Quantity:", product['quantity_in_stock'])
        print("-------------------------")


def add_product(inventory):
    product = {}

    product['product_id'] = input("Enter Product ID: ")
    product['product_name'] = input("Enter Product Name: ")
    product['unit_price'] = float(input("Enter Unit Price: "))
    product['quantity_in_stock'] = int(input("Enter Quantity in Stock: "))

    inventory.append(product)
    print("Product added successfully!")


def update_product_quantity(inventory):
    product_id = input("Enter Product ID to Update: ")

    found = False
    for product in inventory:
        if product['product_id'] == product_id:
            new_quantity = int(input("Enter New Quantity: "))
            product['quantity_in_stock'] = new_quantity
            print("Quantity Updated Successfully!")
            found = True
            break

    if not found:
        print("Product ID not found.")


def calculate_total_value(inventory):
    total_value = 0
    for product in inventory:
        total_value += product['unit_price'] * product['quantity_in_stock']

    print("Total Inventory Value: $", total_value)


# Initial Inventory
inventory = [
    {'product_id': '001', 'product_name': 'Shirt', 'unit_price': 25.0, 'quantity_in_stock': 10},
    {'product_id': '002', 'product_name': 'Pants', 'unit_price': 40.0, 'quantity_in_stock': 20}
]

while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_inventory(inventory)
    elif choice == "2":
        add_product(inventory)
    elif choice == "3":
        update_product_quantity(inventory)
    elif choice == "4":
        calculate_total_value(inventory)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

tasks = []
completed_tasks = []

while True:
    print("\nTo-Do List Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark the Task as Complete")
    print("4. Clear Completed Tasks")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)

    elif choice == "2":
        print("\nCurrent Tasks:")
        for task in tasks:
            print("-", task)
        print("\nCompleted Tasks:")
        for task in completed_tasks:
            print("-", task)

    elif choice == "3":
        print("\nSelect a task to mark as complete by entering its position:")
        for i in range(len(tasks)):
            print(str(i + 1) + ".", tasks[i])

        try:
            task_num = int(input())
            if 0 < task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)
                completed_tasks.append(completed_task)
                print("Task marked as complete!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        completed_tasks.clear()
        print("All completed tasks cleared!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please choose again.")

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 6

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#Write a Python Program to Print Pascal Triangle

def generate_pascal_triangle(n):
    result = []  # List to hold the rows of the triangle
    for i in range(n):
        # Initialize the row with 1 (every row starts with 1)
        row = [1]
        if result:  # If result is not empty
            last_row = result[-1]
            # Generate the values in the current row by summing adjacent values in the last row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # Every row ends with 1
            row.append(1)
        result.append(row)
    return result
# Input the number of rows
num_rows = int(input("Enter number of rows: "))

pascal = generate_pascal_triangle(num_rows)

# Print Pascal's Triangle
for i in range(num_rows):
    print("   " * (num_rows - i), end="")
    for j in pascal[i]:
        print(j, end="      ")
    print()



# WAP to Draw the following Pattern for n number:
#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

# Input the number of rows
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for j in range(n, i-1, -1):
        print(i, end=" ")
    print()  # Move to the next line after each row

#2D List
matrix=[]
matrix.append([1,2,3])
matrix.append([4,5,6])
matrix.append([3,7,8])
print(matrix)


#Find the sum of each row of matrix of size m x n. For example, for the following matrix output will be like this
l1=[]
l2=[]
m=int(input("Enter the no of rows"))
n=int(input("Enter the no of columns"))
for i in range(m):
    for j in range(n):
        print("Enter",i,j,"elements")
        c=int(input())
        l1.append(c)
    l2.append(l1)
    l2=[]
    for i in l2:
        print(i)
d=0
sum_rows=0
for i in l2:
    for j in l2[d]:
        sum_rows+=j
    print("Sum of the row",d+1,"=",sum_rows())
    sum_rows=0
    d+=1


l1 = []
l2 = []

m = int(input("Enter the no of rows: "))
n = int(input("Enter the no of columns: "))

for i in range(m):
    l1 = []  # Reset l1 for a new row
    for j in range(n):
        print("Enter", i, j, "elements:")
        c = int(input())
        l1.append(c)
    l2.append(l1)

d = 0
sum_rows = 0
for i in l2:
    for j in l2[d]:
        sum_rows += j
    print("Sum of the row", d+1, "=", sum_rows)  # Corrected this line
    sum_rows = 0
    d += 1

#Q!Write a Python Program to Calculate the Area of a Triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Input the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = calculate_triangle_area(base, height)

# Display the result
print(f"The area of the triangle with base {base} and height {height} is: {area}")

#Write a Python Program to Swap Two Variables
# Input the values of the two variables
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print("Original values: x =", x, ", y =", y)

# Swap the values
x, y = y, x

print("Swapped values: x =", x, ", y =", y)

#Write a Python Program to Convert Celsius to Fahrenheit
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Input the temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print("Temperature in Celsius:", celsius, "is equivalent to", fahrenheit, "Fahrenheit")

#Write a Python Program to Check if a Number is Odd or Even
# Input the number
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

#Write a Python Program to Check if a Number is Positive, Negative or 0
# Input the number
number = float(input("Enter a number: "))

# Check if the number is positive, negative or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Write a Python Program to Check Armstrong Number
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Write a Python program to check if a given number is Fibonacci number?
N = int(input("Enter the number of terms : "))

# first two terms are f1, f2 equal to 0 and 1 respectively
f1, f2 = 0, 1
count = 0

# checking for invalid inputs
if(N <= 0):
    print("Invalid Input, Kindly enter number greater than 0")

# if only one number in the sequence
elif(N == 1):
    print("Generating Fibonacci Sequence upto ", N, ": ")
    print(f1)

# for all the other cases, i.e. when N > 1
else:
    print("Generating Fibonacci sequence upto ", N, ": ")
    while count < N:
        print(f1)
        fth = f1 + f2
# swapping the values for f1 and f2
        f1 = f2
        f2 = fth
        count += 1

#Write a Python program to print cube sum of first n natural numbers
def cube_sum(n):
    Calculate the cube sum of the first n natural numbers.
    total = 0
    for i in range(1, n+1):
        total += i**3
    return total

# Input the number of natural numbers
n = int(input("Enter the value of n: "))

# Calculate the cube sum
result = cube_sum(n)

# Display the result
print("The cube sum of the first", n, "natural numbers is:", result)

#Write a Python program to print all odd numbers in a range.
# Input the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Odd numbers in the range", start, "to", end, "are:")

for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)

#Pascal Triangle
def generate_pascal_triangle(n):
    Generate Pascal's Triangle for n rows.
    result = []  # List to hold the rows of the triangle
    for i in range(n):
        # Initialize the row with 1 (every row starts with 1)
        row = [1]
        if result:  # If result is not empty
            last_row = result[-1]
            # Generate the values in the current row by summing adjacent values in the last row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # Every row ends with 1
            row.append(1)
        result.append(row)
    return result

# Input the number of rows
num_rows = int(input("Enter number of rows: "))

pascal = generate_pascal_triangle(num_rows)

# Print Pascal's Triangle
for i in range(num_rows):
    print("   " * (num_rows - i), end="")
    for j in pascal[i]:
        print(j, end="      ")
    print()


#WAP to Draw the following Pattern for n number:
#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5
# Input the number of rows
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for j in range(n, i-1, -1):
        print(i, end=" ")
    print()  # Move to the next line after each row


n = int(input("enter number"))

for i in range (1,n+1):
    star = "*" * (i)
    space= " "* (n-i)*2
    star1= "*" * (i)
    print(star1+space+star)

for i in range (1,n+1):
    star = "*" * (n-i)
    space= " "* (i)*2
    star1= "*" * (n-i)
    print(star1+space+star)

"""
#List is an Object
list=(("h","J","K"))
print(list)








































































































