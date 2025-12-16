aList=[13,12,23,34,15,46,87,8,9,10,11,12,1,4,115]
print(aList)

count=0
for i in aList:
    count=count+i

average=count/len(aList)
print("Average is:",average)
aList.sort()
print("Smallest element is:",aList[0])
print("Largest element is:",aList[-1])