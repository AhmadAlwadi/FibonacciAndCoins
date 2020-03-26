#This file is used to generate simple Fibonacci numbers for observations

FiboNumbers=[]

n1, n2 = 0, 1

for i in range(0, 19):
	nth = n1 + n2
	n1, n2 = n2, nth
	FiboNumbers.append(nth)

print(FiboNumbers)