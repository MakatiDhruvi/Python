
def getParenthesis(Str, Count):
	if Count > 0 :
		printParenthesis(Str, 0, Count, 0, 0)
	return

def printParenthesis(Str, Position, Count, Open, Close):
	if Close == Count :
		for i in Str:
			print(i, end = "")
		print()
		return
	else:
		if Open > Close :
			Str[Position] = ')'
			printParenthesis(Str, Position + 1, Count, Open, Close + 1)
		if Open < Count :
			Str[Position] = '('
			printParenthesis(Str, Position + 1, Count, Open + 1, Close)

Count = int(input("Enter number of combinations required: "))
if Count > -1 and Count <= 8 :
    Str = [""] * 2 * Count
    getParenthesis(Str, Count)
else:
    print("Enter number between -1 to 8")
