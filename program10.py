def insertionSort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key

testList = []
n=int(input("Enter no of element you want to enter: "))

for i in range(0, n):
    ele=int(input())
    testList.append(ele)

insertionSort(testList)
print('Sorted Array in Ascending Order:')
print(testList)