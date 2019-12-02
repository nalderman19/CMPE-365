'''
CMPE 365 - Assignment 2, Part 1
Nicholas Alderman, 20060982, 16naa5
'''
import random
import math

class Set:
	def __init__(self, elements, sum):
		self.elements = elements;
		self.sum = sum

emptySet = Set([],0)

#define a set whose subsets we want to evaluate
S = [3,5,3,9,18,4,5,6]
#define target val
k = 28

#Original BFI code that counts and returns number of operations
def BFI_SS(S, k):
	#create empty list of subsets
	subsets = [emptySet]
	ops = 0
	#loop through subset passed through in parameter
	for i in range(0, len(S)):
		subsetsLen = len(subsets)
		ops += 1
		for j in range(0,subsetsLen):
			#create temp variable to keep track of subsets
			temp = Set(subsets[j].elements + [S[i]], subsets[j].sum + S[i])
			subsets.append(temp)
			#increment by 2 since 2 operatons were done in the if statement
			ops += 2
			#check to see if temp is target value
			if temp.sum == k:
				ops += 1
				#if temp = target, return the elements and the ops variable
				return [temp.elements, ops]
	#fallback return statement
	return ["No set exists", ops]

#modified BFI code used by HS algorithm
def BFI_SS_Modified(ModSums):
	#create empty list of subsets
	ops = 0
	subsets = [emptySet]
	#loop through subset passed in from HS algorithm
	for i in range(0, len(ModSums)):
		subsetsLen = len(subsets)
		ops += 1
		for j in range(0, subsetsLen):
			#use temp variable to keep track of subsets
			temp = Set(subsets[j].elements + [ModSums[i]], subsets[j].sum + ModSums[i])
			subsets.append(temp)
			#increment by 2 since 2 operations were done in the if statement
			ops += 2
	#return list of subsets and sums, and number of operations
	return [subsets, ops]


#Pair sum code to pair sorted SetA and SetB
#used to check if target is achieved (k)
def Pair_Sum(SetA, SetB, k):
	ops = 0
	i = 0
	j = len(SetB) - 1
	sum = 0
	#loop through SetA and SetB
	while j > -1 and i < len(SetA):
		ops += 1
		#Case 1: k is found
		if SetA[i].sum + SetB[j].sum == k:
			ops += 1
			#return value where k is found
			return [[SetA[i].elements, SetB[j].elements], ops]
		ops += 1
		#Case 2: value lower than k is found
		if SetA[i].sum + SetB[j].sum < k:
			#increment i (increment through SetA)
			i += 1
		#Case 3: value greater than k is found
		else:
			if SetA[i].sum + SetB[j].sum > k:
				#decrement j (decrement through SetB)
				j -= 1
	return ["Target not found in subset sums.", ops]

#HS Algorithm
def HS_SS(S, k):
	ops = 0
	#Splits up 'S' into even left and right parts
	SRight = S[:len(S) // 2]
	SLeft = S[(len(S) // 2):]

	#uses Modified BFI to sum each part and assigns its [0] value to another subset
	SumL = BFI_SS_Modified(SLeft)
	SubSubSets_L = SumL[0]
	ops += SumL[1]

	SumR = BFI_SS_Modified(SRight)
	SubSubSets_R = SumR[0]
	ops += SumR[1]

	#loops through left and right parts and if the proper result is found, return it
	for i in SubSubSets_L:
		ops += 1
		if (i.sum == k):
			return [i.elements, ops]
	for j in SubSubSets_R:
		ops += 1
		if (j.sum == k):
			return[j.elements, ops]

	#sorts left and right parts and uses the Pair Sum algorithm to check to find values
	#that sum to k
	SubSubSets_R.sort(key=lambda x: x.sum, reverse=False)
	ops += 3 * len(SubSubSets_L) * math.log(len(SubSubSets_L), 2)
	SubSubSets_L.sort(key=lambda x: x.sum, reverse=False)
	ops += 3 * len(SubSubSets_R) * math.log(len(SubSubSets_R), 2)
	#calls PairSum, passing in each part
	PairSum = Pair_Sum(SubSubSets_L, SubSubSets_R, k)
	return [PairSum[0], PairSum[1] + ops]




#return solution from HS Algorithm
final = HS_SS(S, k)
print("HS Algorithm: (set, ops)")
print(final)

#return solution from BFI Algorithm
final2 = BFI_SS(S, k)
print("BFI Algorithm: (set, ops)")
print(final2)

