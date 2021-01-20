
''' This is a binary search algorithm for an already sorted sequence
n: number of items
item: what we are searching for
start: the beginning of the seq n
end: the end of the seq
mid: the middle of the seq n
midVal: the value in the middle of the sequence
'''
def binarySearch(n,item):
    start=0
    end=len(n)-1

    while start <= end:
        mid= start + (end - start) // 2 
        midVal = n[mid] #returns the value in the mid point
        
        if midVal == item:
            return mid

        elif item < midVal:
            end=mid-1
        else:
            start=mid+1

    #item not found
    return None 


 
n=[ ]
# item=int(input('Enter a whole number to get the position:'))
item=1654

for i in range(1,1000000,3):
    n.append(i)


result=binarySearch(n,item)
print('The position of %d is %d.'%(item,result))
