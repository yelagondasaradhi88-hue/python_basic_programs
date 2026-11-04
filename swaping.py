a=int(input("give a:"))
b=int(input("give b:"))
print(f"Before swap: a = {a}, b = {b}")
#with using temp
temp=a
a=b
b=temp
print(f"value of a is :{a}")
print(f"value of b is :{b}")
q=int(input())
r=int(input())
print(f"Before swap: q = {q}, r = {r}")
#without using temp
q=q+r
r=q-r
q=q-r
print(f"value of q is :{q}")
print(f"value of r is :{r}")
#Python shortcut
x = int(input("give x: "))
y = int(input("give y: "))
print(f"Before swap: x = {x}, y = {y}")

x, y = y, x
print(f"After swap (Python shortcut): x = {x}, y = {y}")