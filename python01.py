print("hello world")

# variables
age = 20

price = 19.25

first_name = "Brenold"

is_online = False
print(age)

# receiving input from a user


name = input("What is your name? ")
print("You are welcome " + name)
if(name == "John"):
  print("you are welcome")


birthDate = input("Enter your birthday ")

age = 2022 - int(birthDate)

print(age)

# int()  for converting a value to an integer
# float() for converting a value to a float like 10.2
# bool()  for converting a value to a boolean
# str()  for converting a value to a string

# execise  Adding 2 numbers
num1 = input("Enter first number ")
num2 = input("Enter second number ")

sum = int(num1) + int(num2)
print( "Sum is: ", sum)
# or
print("sum is : " + str(sum))

# defining a function
def Addition( a, b):   
    sum = int(a) + int(b)
    print("Sum: ", sum)
      
          
# to terminte the function or if block of code press ENTER + SHIFT + TAB

temp = 20

if temp > 30:
      print("its a hot day")
elif temp > 20:
      print("its a nice day")
elif temp > 10:
      print("its a bit cold")
else:
    print("it's cold")      
              
    