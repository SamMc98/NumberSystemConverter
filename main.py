Remainders = []
Answer = []

def headerValue(baseNum, rangeNum):
  print("Header values in base", baseNum, "up to", rangeNum, ":")
  for powerRange in range(rangeNum):
    headerVal = baseNum**powerRange #** is to the power of ^
    print(headerVal)

def multiply(NumberToConvert, baseNumber):
  count = str(NumberToConvert).__len__()
  listed = []
  totalList = []
  for digit in str(NumberToConvert):
    listed.append(digit)
  for each in range(count):
    count = count - 1
    total = int(listed[each]) * (int(baseNumber)**count)
    totalList.append(total)
  num = sum(totalList)
  print("The converted number is:",num)
  #converts to base 10, it seems
  #NEEDS TO ADD VALIDATION TO CHECK IF WITHIN BASE RANGE
  #EG BASE 7 HAS TO HAVE NUMBERS LESS THAN 7/UP TO 6
  #for each digit in str(NumberToConvert) must be < baseNumber
  #each digit in 1454 must be < 7
  #try/except OR if else


def divide(Num, Base):
  #print("Higher base to lower base.")
  Div = Num
  if (int(Num) >= 1):
   Div = Num / Base
   Mod = Num % Base
   Num = int(Div)
   Remainders.append(int(Mod))
   divide(Div, Base)
  else:
    Mod = Div
    Div = 0
    count = Remainders.__len__()
    for i in range(count):
     count = count - 1
     Answer.append(Remainders[count])
    printDivAns(Remainders, Answer)

def printDivAns(Remainders, Answer):
    x = ""
    for i in Answer:
      x += str(i)
    print("Answer: ",x)

#Main
#multiply
print("Enter the Number")
numberToConvertInput = int(input())
print("Enter a base number:")
baseNumberInput = int(input())
multiply(numberToConvertInput, baseNumberInput)

#headerValue
print("Enter a base number:")
baseNumInput = int(input())
print("Enter a range to not exceed:")
rangeInput = int(input())
headerValue(baseNumInput, rangeInput) #baseNumber, range

#divide
print("Enter the number")
Num = int(input())
print("Enter the base number")
Base = int(input())
divide(Num, Base)