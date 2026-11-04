limit = int(input("Print numbers up to: "))

#odd numbers
i=1
while i<=limit:
    if i%2 == 0:
        i+=1
        continue
    print(i)
    i+=1

print(f"while loop has  stopped at i value as {i}")

#even numbers
i=1
while i<=limit:
    if i%2 != 0:
        i+=1
        continue
    print(i)
    i+=1

print(f"while loop has  stopped at i value as {i}")

