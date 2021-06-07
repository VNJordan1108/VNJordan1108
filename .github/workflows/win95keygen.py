"""
Windows 95 key generator (Console Version) by Jordan

I know that my code is not the best code but I hope my code 
will help you at some point.
-Jordan-
"""
import random

def GenerateCDKey(a):
    firstSegment = random.randrange(0,999)
    while firstSegment in [333, 444, 555, 666, 777, 888, 999]:
        firstSegment = random.randrange(0,999)
    if firstSegment<10:
        firstSegment = "00" + str(firstSegment)
    elif firstSegment<100:
        firstSegment = "0" + str(firstSegment)        
    secondSegmentList = []
    for i in range(6):
        secondSegmentList.append(random.randrange(0,10))
    sumListSecond = 0
    for i in range(len(secondSegmentList)):
        sumListSecond = sumListSecond + secondSegmentList[i]
    if sumListSecond%7 == 0:
        randomtmp = random.randrange(0, secondSegmentList[5])
        secondSegmentList[5] = secondSegmentList[5] - randomtmp
        secondSegmentList[6] = randomtmp
    else:
        for i in range(len(secondSegmentList)):
            if secondSegmentList[i] > sumListSecond%7:
                randomtmp = random.randrange(0, 6)
                secondSegmentList[i] = secondSegmentList[i] - (sumListSecond%7 - randomtmp)
                secondSegmentList.append(randomtmp)
                break
    for i in range(len(secondSegmentList)):
        secondSegment = secondSegment + str(secondSegmentList[i])
    a = str(firstSegment) + "-" + secondSegment
    return a

#---------------------------------------------------------------
def GenerateOEMKey(a):
    first3DigitOfFirstSegment = random.randrange(1,367) + "-" + 
    if first3DigitOfFirstSegment<10:
        first3DigitOfFirstSegment = "00" + str(first3DigitOfFirstSegment)
    elif first3DigitOfFirstSegment<100:
        first3DigitOfFirstSegment = "0" + str(first3DigitOfFirstSegment) 
    last2DigitOfFirstSegment = random.randrange(3,96)
    if last2DigitOfFirstSegment<10:
        last2DigitOfFirstSegment = "0" + str(last2DigitOfFirstSegment)
    FirstSegment = first3DigitOfFirstSegment + last2DigitOfFirstSegment

       
    secondSegmentList = [0]
    for i in range(6):
        secondSegmentList.append(random.randrange(0,10)) 
    for i in range(len(secondSegmentList)):
        secondSegment = secondSegment + str(secondSegmentList[i])
    a = str(FirstSegment) + "-" + secondSegment
    
    return a




#----------------------------------------------------------------

userChoice =  str(input("Do you want CD key or OEM key (CD/OEM): "))
userChoice.upper()
amount = int(input("Enter amount of key you want to generate: "))
keyOut = ""
if userChoice == "CD":
    for i in range(amount):
        GenerateCDKey(keyOut)
        keyOutArray.append(keyOut)
elif userChoice == "OEM":
    for i in range(amount):
        GenerateOEMKey(keyOut, amount)
        keyOutArray.append(keyOut)

for i in range(len(keyOutArray)):
    print(keyOutArray[i], "\n")
