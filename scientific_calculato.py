import math
import random
import statistics
valid = ['+', '-', '*', '/', '//', '%', '**', 'sqrt', 'abs', 'cbrt', 'root', 'square', 'cube',
         'log', 'log2', 'log10', 'logy', 'sin', 'cos', 'tan', 'cosec', 'sec', 'cot',
         'sinh', 'cosh', 'tanh', 'cosech', 'sech', 'coth', 'asin', 'acos', 'atan',
         'acosec', 'asec', 'acot', 'asinh', 'acosh', 'atanh', 'acosech', 'asech', 'acoth',
         'ceil', 'floor', 'trunc', 'round', 'percentage', 'inc', 'dec', 'gcd', 'lcm',
         'comb', 'perm', 'fact', 'rand', 'randf', 'swap', 'sign', 'exp', 'e', '10',
         '2', 'pi', 'rec', 'degrees', 'radians', 'min', 'max', 'avg',
         'm+', 'm-', 'ms', 'mc', 'mr', 'exit']

memory = 0
memory2 = 0

while True:
    operator = input(f"Enter operator {valid}: ").strip().lower()
    if  operator not in valid:
        print("invalid operator") 
    elif operator == "exit":
        print("Exiting calculator. Goodbye!") 
        break
    #memory clear
    elif operator == "mc":
        memory = 0
        memory2 = 0
        print(memory)
        print(memory2)
    #memory recall
    elif operator == "mr":
        print(memory)
        print(memory2)  

    elif operator in ['sqrt', 'abs', 'log', 'log2', 'log10']:
        num1= float(input("Enter a number : "))
        if operator=='sqrt':
            if num1<0:
                print("Cannot calculate square root of a negative number.")
            else: 
                print(round(math.sqrt(num1),3))
    #Absolute Value
        elif operator=="abs":
            print(abs(num1))
        # log (natural log, base e)
        elif operator =="log":
            if num1 > 0:
                print(round(math.log(num1),3))
            else:
                print("Input must be greater than 0 for log")
        #Log Base 2
        elif operator =="log2":
            if num1 > 0:
                print(round(math.log2(num1), 3))
            else:
                print("Input must be greater than 0 for log2")
    # log10 (base 10)
        elif operator =="log10":
            if num1 > 0:
                print(round(math.log10(num1),3))
            else:
                print("Input must be greater than 0 for log10")
    else:
        num1= float(input("Enter a number : "))
        num2= float(input("Enter another number : "))
        # basic operations
        if operator =="+":
            print(round(num1+num2,3))
        elif operator == "-":
            print(round(num1-num2,3))
        elif operator =="*":
            print(round(num1*num2,3))
        elif operator=="/":
            if num2 !=0:
                print(round(num1/num2,3))
            else:
                print("Cannot divide by zero.")
        elif operator =="//":
            if num2 !=0: 
                print(int(num1//num2))
            else:
                print("Cannot divide by zero.")
        elif operator =="%":
            if num2!=0:
                print(round(num1%num2,3))
            else:
                print("Cannot divide by zero.")
        elif operator =="**":
            if num1 == 0 and num2 < 0:
                print("Cannot calculate 0 to a negative power.")
            elif num1 < 0 and num2 % 1 != 0:
                print("Cannot calculate a negative number to a fractional power.")
            else:
                print(round(num1 ** num2, 3))    
        # roots, squares, cubes
        elif operator == "cbrt":
            print(round(math.cbrt(num1),3))
            print(round(math.cbrt(num2),3))
        elif operator == "root":
            n = int(input("Enter root number (n): "))
            if n <= 0:
                print("Root number must be greater than 0.")
            elif num1 < 0 or num2 < 0:
                print("Both numbers must be 0 or greater for root.")
            else:
                print(round(math.pow(num1, (1 / n)), 3))
                print(round(math.pow(num2, (1 / n)), 3))
        elif operator =="square":
            print(round(math.pow(num1,2),3))
            print(round(math.pow(num2,2),3))
        elif operator=="cube":
            print(round(math.pow(num1,3),3))
            print(round(math.pow(num2,3),3))
        # logy (log of num1 with base num2)
        elif operator =="logy":
            if num1 <= 0:
                print("Number must be greater than 0 for logy")
            elif num2 <= 0 or num2 == 1:
                print("Base must be greater than 0 and not equal to 1")
            else:
                print(round(math.log(num1, num2), 3))
        #trigonometry (angles in degrees)
        elif operator == "sin" :
            print(round(math.sin(math.radians(num1+num2)),3))
            print(round(math.sin(math.radians(num1)),3))
            print(round(math.sin(math.radians(num2)),3))
        elif operator == "cos" :
            print(round(math.cos(math.radians(num1+num2)),3))
            print(round(math.cos(math.radians(num1)),3))
            print(round(math.cos(math.radians(num2)), 3))
        elif operator == "tan" :
            if (num1 + num2) % 180 == 90 or num1 % 180 == 90 or num2 % 180 == 90:
                print("tan is undefined at 90, 270, ... degrees (check num1, num2 and num1+num2)")
            else:
                print(round(math.tan(math.radians(num1+num2)),3))
                print(round(math.tan(math.radians(num1)),3))
                print(round(math.tan(math.radians(num2)),3))
        elif operator == "cosec" :
            if (num1 + num2) % 180 == 0 or num1 % 180 == 0 or num2 % 180 == 0:
                print("cosec is undefined at 0, 180, 360, ... degrees (check num1, num2 and num1+num2)")
            else:
                print(round(1/math.sin(math.radians(num1+num2)),3))
                print(round(1/math.sin(math.radians(num1)),3))    
                print(round(1/math.sin(math.radians(num2)),3))
        elif operator == "sec" :
            if (num1 + num2) % 180 == 90 or num1 % 180 == 90 or num2 % 180 == 90:
                print("sec is undefined at 90, 270, ... degrees (check num1, num2 and num1+num2)")
            else:
                print(round(1/math.cos(math.radians(num1+num2)),3))
                print(round(1/math.cos(math.radians(num1)),3))
                print(round(1/math.cos(math.radians(num2)),3))
        elif operator == "cot" :
            if (num1 + num2) % 180 == 0 or num1 % 180 == 0 or num2 % 180 == 0:
                print("cot is undefined at 0, 180, 360, ... degrees (check num1, num2 and num1+num2)")
            else:
                print(round(1 / math.tan(math.radians(num1 + num2)), 3))
                print(round(1 / math.tan(math.radians(num1)), 3))
                print(round(1 / math.tan(math.radians(num2)), 3))
        elif operator == "sinh" :
            print(round(math.sinh(num1 + num2), 3))
            print(round(math.sinh(num1), 3))
            print(round(math.sinh(num2), 3))
        elif operator == "cosh" :
            print(round(math.cosh(num1 + num2), 3))
            print(round(math.cosh(num1), 3))
            print(round(math.cosh(num2), 3))
        elif operator == "tanh":
            print(round(math.tanh(num1 + num2), 3))
            print(round(math.tanh(num1), 3))
            print(round(math.tanh(num2), 3))
        elif operator == "cosech" :
            if num1 + num2 == 0 or num1 == 0 or num2 == 0:
                print("cosech is undefined at 0 (check num1, num2 and num1+num2)")
            else:
                print(round(1 / math.sinh(num1 + num2), 3))
                print(round(1 / math.sinh(num1), 3))
                print(round(1 / math.sinh(num2), 3))
        elif operator == "sech" :
            print(round(1/math.cosh(num1+num2),3))
            print(round(1/math.cosh(num1),3))
            print(round(1/math.cosh(num2),3))
        elif operator == "coth" :
                if num1 + num2 == 0 or num1 == 0 or num2 == 0:
                    print("coth is undefined at 0 (check num1, num2 and num1+num2)")
                else:   
                 print(round(1/math.tanh(num1+num2),3))
                 print(round(1/math.tanh(num1),3))
                 print(round(1/math.tanh(num2),3))
        elif operator == "asin":
            if -1 <= num1 <= 1 and -1 <= num2 <= 1:
                print(round(math.degrees(math.asin(num1)), 3))
                print(round(math.degrees(math.asin(num2)), 3))
            else:
                print("Input must be between -1 and 1 for asin")        
        elif operator =="acos":
            if -1 <= num1 <= 1 and -1 <= num2 <= 1:
                print(round(math.degrees(math.acos(num1)),3))
                print(round(math.degrees(math.acos(num2)),3))
            else:
                print("Input must be between -1 and 1 for acos")   
        elif operator == "atan":
            print(round(math.degrees(math.atan(num1)), 3))
            print(round(math.degrees(math.atan(num2)), 3)) 
        elif operator =="acosec":
            if abs(num1) >= 1 and abs(num2) >= 1:
                print(round(math.degrees(math.asin(1 / num1)), 3))
                print(round(math.degrees(math.asin(1 / num2)), 3))
            else:
                print("Input must be <= -1 or >= 1  for acosec")   
        elif operator =="asec":
            if abs(num1) >= 1 and abs(num2) >= 1:
                print(round(math.degrees(math.acos(1 / num1)), 3))
                print(round(math.degrees(math.acos(1 / num2)), 3))
            else:
                print("Input must be <= -1 or >= 1 for asec")
        elif operator =="acot":
            if num1 != 0 and num2 != 0:
                print(round(math.degrees(math.atan(1 / num1)), 3))
                print(round(math.degrees(math.atan(1 / num2)), 3))
            else:
                print("Input must not be 0 (zero) for acot")
        # inverse hyperbolic functions (plain numbers, NOT angles)
        elif operator =="asinh":
            print((round(math.asinh(num1), 3)))
            print((round(math.asinh(num2), 3)))
        elif operator =="acosh":
            if num1 >= 1 and num2 >= 1:
                print(round(math.acosh(num1), 3))
                print(round(math.acosh(num2), 3))
            else:
                print("Input must be >= 1 for acosh")
        elif operator =="atanh":
            if -1 < num1 < 1 and -1 < num2 < 1:
                print(round(math.atanh(num1), 3))
                print(round(math.atanh(num2), 3))
            else:
                print("Input must be between -1 and 1 (not including -1 and 1) for atanh")
        elif operator =="acosech":
            if num1 != 0 and num2 != 0:
                print(round(math.asinh(1 / num1), 3))
                print((round((math.asinh(1/num2)), 3)))
            else:
                print("Input must not be 0 for acosech")
        elif operator =="asech":
            if 0 < num1 <= 1 and 0 < num2 <= 1:
                print(round(math.acosh(1 / num1), 3))
                print(round(math.acosh(1 / num2), 3))
            else:
                print("Input must be greater than 0 and at most 1 for asech")
        elif operator =="acoth":
            if abs(num1) > 1 and abs(num2) > 1:
                print(round(math.atanh(1 / num1), 3))
                print(round(math.atanh(1 / num2), 3))
            else:
                print("Input must be < -1 or > 1 for acoth")
        #rounding
        elif operator =="ceil":
            print(math.ceil(num1))
            print(math.ceil(num2))
        elif operator =="floor":
            print(math.floor(num1))
            print(math.floor(num2))
        #Truncate
        elif operator == "trunc":
            print(math.trunc(num1))
            print(math.trunc(num2))
        elif operator=="round":
            print(round(num1,3))
            print(round(num2,3))
        #percentage
        elif operator=="percentage":
            if num2 !=0:
                print(round((num1 / num2) * 100, 3))
            else:
                print("Cannot calculate percentage with a denominator of zero.")
        #inc   Increase %
        elif operator=="inc":
            print(round(num1 * (1 + num2 / 100), 3))
        #dec       Decrease %
        elif operator=="dec":
            print(round(num1 * (1 - num2 / 100), 3))
        # Greatest Common Divisor
        elif operator =="gcd":
            if num1 % 1 == 0 and num2 % 1 == 0:
                print(math.gcd(int(num1),int(num2)))
            else:
                print("Both numbers must be whole numbers for gcd")
        #Least Common Multiple
        elif operator =="lcm":
            if num1 % 1 == 0 and num2 % 1 == 0:
                print(math.lcm(int(num1),int(num2)))
            else:
                print("Both numbers must be whole numbers for lcm")
        #comb      nCr
        elif operator=="comb":
            if num1 % 1 == 0 and num2 % 1 == 0 and num1 >= 0 and num2 >= 0:
                print(math.comb(int(num1), int(num2)))
            else:
                print("Both numbers must be whole numbers, 0 or greater, for comb")
        #perm      nPr
        elif operator=="perm":
            if num1 % 1 == 0 and num2 % 1 == 0 and num1 >= 0 and num2 >= 0:
                print(math.perm(int(num1), int(num2)))
            else:
                print("Both numbers must be whole numbers, 0 or greater, for perm")   
        #fact      Factorial  
        elif operator == "fact":
            if num1 % 1 == 0 and num2 % 1 == 0 and num1 >= 0 and num2 >= 0:
                print(math.factorial(int(num1)))
                print(math.factorial(int(num2)))
            else:
                print("Both numbers must be whole numbers, 0 or greater, for factorial")   
        # random numbers
        elif operator == "rand":
            if num1 % 1 == 0 and num2 % 1 == 0 and num1 <= num2:
                print(random.randint(int(num1), int(num2)))
            else:
                print("Enter whole numbers, and the 1st number must not be bigger than the 2nd")
        elif operator == "randf":
            print(round(random.uniform(num1, num2), 3))
        # other operations
        #swap      Swap Two Numbers
        elif operator=="swap":
            num1,num2 = num2,num1
            print("num1 =", num1)
            print("num2 =",num2)
        #Sign change:
        elif operator=="sign":
            print(-num1)
            print(-num2)
        elif operator == "exp":
            print(round(math.exp(num1),3))
            print(round(math.exp(num2),3))
        elif operator =="e":
            print(round(num1*math.e,3))
            print(round(num2*math.e,3))
            print(round((num1+num2)*math.e, 3))
        elif operator =="10":
            print(round(10**num1,3))
            print(round(10**num2,3))
        elif operator=="2":
            print(round(2**num1,3))
            print(round(2**num2,3))
        elif operator == "pi":
            print(round(num1*math.pi,3))
            print(round(num2*math.pi,3))
            print(round((num1+num2)*math.pi,3))
        #Reciprocal: 1/x
        elif operator == "rec":
            if num1 != 0 and num2 != 0:
                print(round(1 / num1, 3))
                print(round(1 / num2, 3))
            else:
                print("Input must not be 0 for rec")
        # Radians → Degrees
        elif operator=="degrees":
            print(round(math.degrees(num1),3))
            print(round(math.degrees(num2),3))
        # Degrees → Radians
        elif operator=="radians":
            print(round(math.radians(num1),3))
            print(round(math.radians(num2),3))
        elif operator =="min":
            print(min(num1,num2))
        elif operator =="max":
            print(max(num1,num2)) 
        # Average
        elif operator=="avg":
            print(round(statistics.mean([num1, num2]), 3))
        #memory
        elif operator == "m+":
            memory += num1
            memory2 += num2
            print(memory)
            print(memory2)
        elif operator == "m-":
            memory -= num1
            memory2 -= num2
            print(memory)
            print(memory2)
        elif operator == "ms":
            memory = num1
            memory2 = num2
            print(memory)
            print(memory2)
        else:
            print("invalid operator")
