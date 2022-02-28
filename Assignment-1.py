NumberDictionary = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def GetLCM(Number1, Number2):
   if Number1 > Number2:
       Greater = Number1
   else:
       Greater = Number2
   while True:
       if (Greater % Number1 == 0) and (Greater % Number2 == 0):
           LCM = Greater
           break
       Greater += 1
   return int(LCM)
def GetGCD(Numerator, Denominator):
    GCD = str(int(Numerator / Denominator))
    NumberDictionaryCount = 0
    while NumberDictionaryCount < len(NumberDictionary):
        GCD = GCD.replace(str(NumberDictionaryCount), NumberDictionary[NumberDictionaryCount])
        NumberDictionaryCount += 1
    return GCD
Number1 = input("Enter First Number:")
Number2 = input("Enter Second Number:")
NumberDictionaryCount = 0
while NumberDictionaryCount < len(NumberDictionary):
    Number1 = Number1.replace(NumberDictionary[NumberDictionaryCount], str(NumberDictionaryCount))
    Number2 = Number2.replace(NumberDictionary[NumberDictionaryCount], str(NumberDictionaryCount))
    NumberDictionaryCount += 1
Number1 = int(Number1)
Number2 = int(Number2)
print(GetGCD(Number1 * Number2, (GetLCM(Number1, Number2))))
