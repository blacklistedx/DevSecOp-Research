# series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

index=int(input("Enter the index start number: "))

firstNumber=0
secondNumber=1
temp=0

print(firstNumber)
print(secondNumber)
for i in range(0, index):
    temp = firstNumber + secondNumber
    firstNumber = temp
    print(temp)
