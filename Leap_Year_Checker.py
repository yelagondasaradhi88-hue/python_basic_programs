year = int(input("Enter a year: "))


if year%400==0:
    leap=True
elif year%100==0 :
    leap=False
elif year%4==0:
    leap=True
else:
    leap=False

if leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")