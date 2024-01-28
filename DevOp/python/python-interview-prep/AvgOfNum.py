# Collects number, makes list

def collectNumbers(totalNumbers): 
    print("Please Enter", totalNumbers, "numbers:")
    for i in range(0,totalNumbers):
        ele = float(input())
        myList.append(ele) # Loop to put every element inside the list

# Calculates average

def calculateAverage():
    total = 0
    for i in range(0,len(myList)):
        total = total + myList[i]
    return (total/totalNumbers)

myList = [] # Empty, to accept values to puth inside of the list

totalNumbers=int(input("Average of how many numbers? ")) #
collectNumbers(totalNumbers) # Calling Function to create a list

average=calculateAverage() # Calling funtion to calculate average
print("The average is : ", average)
