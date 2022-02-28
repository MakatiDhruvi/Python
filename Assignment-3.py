from collections import defaultdict
ListOfItems = []
Count = int(input("How many numbers of input do you want to insert: "))
for i in range(Count) :
    ListOfItems.insert(i, input("Enter " + str(i + 1) + " Value: "))
TempList = defaultdict(list)
for Item in ListOfItems:
	TempList[str(sorted(Item))].append(Item)
Result = list(TempList.values())
print(str(Result))