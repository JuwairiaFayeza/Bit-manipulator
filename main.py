# num1=9
# num2=7

# print(num1 & num2)
# print(num1 | num2)
# print(num1 ^ num2)
# print(~num1)
# print(~num2)
# print("num1 left shift" , num1<<1)
# print("print right shift", num1>>1)

def iseven(n):
    if(n ^ 1== n+1):
        return True 
    else :
        return False

number= 30
if iseven(number):
    print("Number is even")
else:
    print("Number is odd")