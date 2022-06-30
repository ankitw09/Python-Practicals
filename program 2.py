# read list and remove duplicate and reversed 

testList = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " + str(testList))

for i in range(0, len(testList)):
	j=i+1
	while j<len(testList):
		if testList[i]==testList[j]:
			testList.pop(j)
		j=j+1

# printing list after removal
print ("The list after removing duplicates : " ,testList)
testList.reverse()
print (testList)


# using naive method
# to remove duplicated
# from list
# res = []
# for i in testList:
# 	if i not in res:
# 		res.append(i)