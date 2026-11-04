maths=int(input("Enter your maths marks: "))
english=int(input("Enter your english marks: "))
python=int(input("Enter your python marks: "))
web=int(input("Enter your web marks: "))
gk=int(input("Enter your gk marks: "))

total=maths+english+python+web+gk
print('Your total marks is',total)
average = total / 5
print('Your average is',average)
percentage = (total / 500) * 100
print('Your percentage is',percentage)
if 90<=percentage<=100:
    print('Grade is A+')
elif 80<=percentage<90:
    print('Grade is A')
elif 75<=percentage<80:
    print('Grade is B')
elif 50<=percentage<75:
    print('Grade is C')
elif 40<=percentage<50:
    print('Grade is D')
elif 36<=percentage<40:
    print('Grade is E')
else:
    print('Grade is F')