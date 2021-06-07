"""
Windows 95 key generator (Console Version) by Jordan

I know that my code is not the best code but I hope my code 
will help you at some point.
-Jordan-
"""
import random

'''def GenerateCDKey(keyOut):
    firstSegment = random.randrange(0,999)
    while firstSegment in [333, 444, 555, 666, 777, 888, 999]:
        firstSegment = random.randrange(0,999)
    if firstSegment<10:
        firstSegment = "00" + str(firstSegment)
    elif firstSegment<100:
        firstSegment = "0" + str(firstSegment)        
    secondSegmentList = []
    secondSegment = 0
    for i in range(6):
        secondSegmentList.append(random.randrange(0,10))
    sumListSecond = 0
    for i in range(len(secondSegmentList)):
        sumListSecond = sumListSecond + secondSegmentList[i]
    if sumListSecond%7 == 0:
        randomtmp = random.randrange(0, secondSegmentList[5])
        secondSegmentList[5] = secondSegmentList[5] - randomtmp
        secondSegmentList.append(randomtmp)
    else:
        for i in range(len(secondSegmentList)):
            if secondSegmentList[i] > sumListSecond%7:
                randomtmp = random.randrange(0, 6)
                secondSegmentList[i] = secondSegmentList[i] - (sumListSecond%7 - randomtmp)
                secondSegmentList.append(randomtmp)
                break
    for i in range(len(secondSegmentList)):
        secondSegment = str(secondSegment) + str(secondSegmentList[i])
    keyOut = str(firstSegment) + "-" + str(secondSegment)
    return keyOut

#---------------------------------------------------------------
def GenerateOEMKey(keyOut):
    first3DigitOfFirstSegment = random.randrange(1,367)
    if first3DigitOfFirstSegment<10:
        first3DigitOfFirstSegment = "00" + str(first3DigitOfFirstSegment)
    elif first3DigitOfFirstSegment<100:
        first3DigitOfFirstSegment = "0" + str(first3DigitOfFirstSegment) 
    last2DigitOfFirstSegment = random.randrange(3,96)
    if last2DigitOfFirstSegment<10:
        last2DigitOfFirstSegment = "0" + str(last2DigitOfFirstSegment)
    
    firstSegment = first3DigitOfFirstSegment + last2DigitOfFirstSegment

       
    secondSegmentList = [0]
    for i in range(6):
        secondSegmentList.append(random.randrange(0,10)) 
    for i in range(len(secondSegmentList)):
        secondSegment = secondSegment + str(secondSegmentList[i])
    
    
    thirdSegment = random.randrange(0, 100000)
    if thirdSegment<10:
        thirdSegment = "0000" + str(thirdSegment)
    elif thirdSegment<100:
        thirdSegment = "000" + str(thirdSegment)
    elif thirdSegment<1000:
        thirdSegment = "00" + str(thirdSegment)
    else:
        thirdSegment = "0" + str(thirdSegment)
    keyOut = str(firstSegment) + "- OEM - " + secondSegment + " - " + thirdSegment
    return keyOut'''




#----------------------------------------------------------------

userChoice =  str(input("Do you want CD key or OEM key (CD/OEM): "))
userChoice.upper()
amount = int(input("Enter amount of key you want to generate: "))
keyOut = ""
keyOutArray = []
if userChoice == "CD":
    for i in range(amount):
        firstSegment = random.randrange(0,999)
        while firstSegment in [333, 444, 555, 666, 777, 888, 999]:
            firstSegment = random.randrange(0,999)
        if firstSegment<10:
            firstSegment = "00" + str(firstSegment)
        elif firstSegment<100:
            firstSegment = "0" + str(firstSegment)        
        secondSegmentList = []
        secondSegment = 0
        for i in range(6):
            secondSegmentList.append(random.randrange(0,10))
        sumListSecond = 0
        for i in range(len(secondSegmentList)):
            sumListSecond = sumListSecond + secondSegmentList[i]
        if sumListSecond%7 == 0:
            randomtmp = random.randrange(0, secondSegmentList[5])
            secondSegmentList[5] = secondSegmentList[5] - randomtmp
            secondSegmentList.append(randomtmp)
        else:
            for i in range(len(secondSegmentList)):
                if secondSegmentList[i] > sumListSecond%7:
                    randomtmp = random.randrange(0, 6)
                    secondSegmentList[i] = secondSegmentList[i] - (sumListSecond%7 - randomtmp)
                    secondSegmentList.append(randomtmp)
                    break
        for i in range(len(secondSegmentList)):
            secondSegment = str(secondSegment) + str(secondSegmentList[i])
        keyOut = str(firstSegment) + "-" + str(secondSegment)
        keyOutArray.append(keyOut)
elif userChoice == "OEM":
    for i in range(amount):
        first3DigitOfFirstSegment = random.randrange(1,367)
        if first3DigitOfFirstSegment<10:
            first3DigitOfFirstSegment = "00" + str(first3DigitOfFirstSegment)
        elif first3DigitOfFirstSegment<100:
            first3DigitOfFirstSegment = "0" + str(first3DigitOfFirstSegment) 
        last2DigitOfFirstSegment = random.randrange(3,96)
        if last2DigitOfFirstSegment<10:
            last2DigitOfFirstSegment = "0" + str(last2DigitOfFirstSegment)
        
        firstSegment = str(first3DigitOfFirstSegment) + str(last2DigitOfFirstSegment)

        
        secondSegmentList = [0]
        secondSegment = 0
        for i in range(6):
            secondSegmentList.append(random.randrange(0,10)) 
        for i in range(len(secondSegmentList)):
            secondSegment = str(secondSegment) + str(secondSegmentList[i])
        
        
        thirdSegment = random.randrange(0, 100000)
        if thirdSegment<10:
            thirdSegment = "0000" + str(thirdSegment)
        elif thirdSegment<100:
            thirdSegment = "000" + str(thirdSegment)
        elif thirdSegment<1000:
            thirdSegment = "00" + str(thirdSegment)
        else:
            thirdSegment = "0" + str(thirdSegment)
        keyOut = str(firstSegment) + "- OEM - " + secondSegment + " - " + thirdSegment
        keyOutArray.append(keyOut)
else:
    print("Try again")

for i in range(len(keyOutArray)):
    keyOut = keyOutArray[i] + "\n"
    print(keyOut)
