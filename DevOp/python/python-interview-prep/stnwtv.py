# Swapping without using a temp variable

num1=10
num2=20

if num1 < num2 : 

    print("In if - Before Swap",num1, num2)

    num2=num2+num1
    num1=num2-num1
    num2=num2-num1

    print("In if - after swap",num1, num2)

else : 

    print("In if - Before Swap"), num1, num2)

    num1=num1+num2
    num2=num1-num2
    num1=num1-num2

    print("In Else - After Swap",num1,num2)
