v = 0
FiboSeq = []
LengthOfSeq = 0
upperIndex = 0
solutions = []
originalSeq = []

def GetV():
	valid = False
	print("Please enter a value of v between 1 and 1 billon inclusivly: ")
	while valid == False:
		v = int(input())
		if v < 1 or v > 1000000000:
			print("Value outwith the range, try again, value has to be between 1 and 1,000,000,000")
		else:
			valid = True
	return v

def MakeFiboSeq(upperLimit):
	global solutions
	n1, n2   = 0, 1
	sequence = []
	while n1+n2 <= upperLimit:
		nth = n1+n2
		sequence.append(nth)
		n1, n2 = n2, nth
	return sequence, len(sequence), len(sequence)-1

def MainLoop(v, sequence, LengthOfSeq, upperIndex):
	total = 0 
	SecondV = v
	while total != v:
		solutions.append(sequence[upperIndex])
		total+=sequence[upperIndex]
		SecondV -= sequence[upperIndex]
		sequence, LengthOfSeq, upperIndex = MakeFiboSeq(SecondV)
	return solutions

def checkIfItsThere(dataset, val):
	valid = True
	counter = 0
	for i in dataset:
		if i == val:
			valid = False
			return valid
			break
		else:
			counter +=1
	if counter == len(dataset):
		valid = True
		return valid

v= GetV()
FiboSeq, LengthOfSeq, upperIndex = MakeFiboSeq(v)
originalSeq = FiboSeq
solutions = MainLoop(v, FiboSeq, LengthOfSeq, upperIndex)
print(solutions)