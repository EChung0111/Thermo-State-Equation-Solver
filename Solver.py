import sympy
import math

R = 0.08314

while True:
    print("Which State Equation Do You Want To Use?")
    print("(1) Perfect Gas")
    print("(2) Vdw")
    print("(3) Redlich Kwong")
    print()
    State_Eq = input()
    print()
    allow_eq_list = ["1","2","3"]
    if State_Eq not in allow_eq_list:
        print("Invalid Selection! Please try again.")
    else:
        break
        
if State_Eq == "2":
    optionlist = ['P','V','a','b','T']
    while True:
        print("P = (RT)/(V-b) - a/V^2")
        print("Units: bar Kelvin Liters")
        print("Which Variable are you trying to solve for?")
        varsolv = input()
        print()
        
        if varsolv not in optionlist:
            print("You chose an invalid option.")
            print("You need to chose a variable in the equation shown above.")
            print('Try choosing a different variable')
            print()
        else:
            break
            
    for var in optionlist:
        if varsolv != var:
            print(f"Please enter a value for the following variable: {var}")
            vars()[var] = float(input())
            print()
    
    if varsolv != 'P':
        vars()[varsolv] = sympy.symbols(varsolv)
        exp = (R*T)/(V-b)-a/V**2-P
        sol = sympy.solve(exp)
        print(f"{varsolv} = {sol[0]}")
    else:
        P = (R*T)/(V-b)-a/V**2
        print(f"P = {P}")

elif State_Eq == "1":
    optionlist = ['P','V','T']
    while True:
        print("P = (RT)/V")
        print("Units: bar Kelvin Liters")
        print("Which Variable are you trying to solve for?")
        varsolv = input()
        print()
        
        if varsolv not in optionlist:
            print("You chose an invalid option.")
            print("You need to chose a variable in the equation shown above.")
            print('Try choosing a different variable')
            print()
        else:
            break
            
    for var in optionlist:
        if varsolv != var:
            print(f"Please enter a value for the following variable: {var}")
            vars()[var] = float(input())
            print()
    
    if varsolv != 'P':
        vars()[varsolv] = sympy.symbols(varsolv)
        exp = (R*T)/V-P
        sol = sympy.solve(exp)
        print(f"{varsolv} = {sol[0]}")
    else:
        P = (R*T)/V
        print(f"P = {P}")

elif State_Eq == "3":
    optionlist = ['P','V','A','B','T']
    while True:
        print("P = (RT)/(V-B) - A/sqrT(T)V(V+B)")
        print("Units: bar Kelvin Liters")
        print("Which Variable are you trying to solve for?")
        varsolv = input()
        print()
        
        if varsolv not in optionlist:
            print("You chose an invalid option.")
            print("You need to chose a variable in the equation shown above.")
            print('Try choosing a different variable')
            print()
        else:
            break
            
    for var in optionlist:
        if varsolv != var:
            print(f"Please enter a value for the following variable: {var}")
            vars()[var] = float(input())
            print()
    
    if varsolv != 'P':
        vars()[varsolv] = sympy.symbols(varsolv)
        exp = (R*T)/(V-B)-A/(sqrt(T)*V*(V+B))-P
        sol = sympy.solve(exp)
        print(f"{varsolv} = {sol[0]}")
    else:
        P = (R*T)/(V-B)-A/(sqrt(T)*V*(V+B))
        print(f"P = {P}")
