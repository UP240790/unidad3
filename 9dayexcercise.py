#1.1
 
#1
age = int(input(f'Enter your age: '))
if age >= 18:
     print(f'You are old enough to drive')
else:
     print(f'You need {18-age} years to drive')
 
 #2
yourAge = int(input("Enter your age: "))
myAge = 20
 
if myAge > yourAge:
     print(f"I'm {myAge-yourAge} older than you")
elif myAge < yourAge:
     print(f"You're {yourAge-myAge} older than me")
else:
     print(f'We are of the same age ')
 
 #3
n1 = int(input(f"Enter number 1: "))
n2 = int(input(f"Enter number 2: "))
 
if n1 > n2:
     print(f"{n1} is greater than {n2}")
elif n1 < n2:
     print(f"{n2} is greater than {n1}")
else:
     print(f'The numbers are equal')
 
 
 #1.2
 #1
score = int(input("Enter your score: "))
 
if score < 50:
     print(f"Your grade is F")
elif score <= 59 and score >= 50:
     print(f"Your grade is D")
elif score <= 69 and score >= 60:
     print(f"Your grade is C")
elif score <= 89 and score >= 70:
     print(f"Your grade is B")
elif score <= 100 and score >= 90:
     print(f"Your grade is A")
else:
     print(f"Score no valid")
 
 
 #2
month = input("Enter the current month: ").upper()
 
if month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
     print(f"The current season is Autumn")
 
elif month == "DECEMBER" or month == "JANUARY" or month == "FEBRUARY":
     print(f"The current season is Winter")
 
elif month == "MARCH" or month == "APRIL" or month == "MAY":
     print(f"The current season is Spring")
 
elif month == "JUNE" or month == "JULY" or month == "AUGUST":
     print(f"The current season is Summer")
 
else:
     print(f"Invalid Data")
 
 
 #3
fruits = ['banana', 'orange', 'mango', 'lemon']
newFruit = input("Enter a fruit: ").lower()
 
if newFruit in fruits:
     print(f"The {newFruit} it's already in the list: ")
else:
     print(f"Adding the {newFruit}...")
     fruits.append(newFruit)
print(fruits)
 
 
 
 #Exercises: Level 3
person = {
     'first_name': 'Dante',
     'last_name': 'González',
 }