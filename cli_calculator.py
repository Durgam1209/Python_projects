
#calculator

def calculator(op1,op,op2):
    res=0
    def calculation(op1,op,op2):
        if op == '+':
            return float(op1+op2)
        elif op == '-':
            return op1-op2
        elif op == '*':
            return op1*op2
        elif op == '/':
            try:
                res= op1/op2
            except:
                print("Cannot divide a number by Zero \n Try again withanother number")
            else:
                return res
        elif op == '%':
            try:
                res= op1%op2
            except:
                print("Cannot divide a number by Zero \n Try again with another INTEGER number")
            else:
                return res
    return calculation(op1,op,op2)

print("-------------------Simple CLI calculator----------------------")
op1 = float(input("Enter first num: "))
op = input("Enter any of operator\n[+,-,*,/,%]:")
op2 = float(input("Enter second num: "))   

print(f'{op1} {op} {op2} = {calculator(op1,op,op2)}')