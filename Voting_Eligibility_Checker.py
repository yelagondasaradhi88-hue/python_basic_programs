name=input("enter your name: ")
age = int(input("enter your age :"))
if age < 0:
        print("Please enter a valid age.")
elif age >=18:
    print(f"{name}, You age is eligible to vote. Your age: {age}")
else:
    print(f"{name}, You age is not eligible to vote. Your age: {age}")
    print(f"{name},You can vote after {18 - age} year's.")