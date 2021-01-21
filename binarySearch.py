
''' This is a binary search algorithm for an already sorted sequence
n: number of items
item: what we are searching for
start: the beginning of the seq n
end: the end of the seq
mid: the middle of the seq n
midVal: the value in the middle of the sequence
'''

file=open("words.txt","r")
content=file.read()
content_list = content.splitlines()
file.close()
List=content_list #converts the text file to a list
def binarySearch(n,item):
    start=0
    end=len(n)-1

    while start <= end:
        mid= start + end // 2 
        midVal = n[mid] #returns the value in the mid point
    
        if midVal > item:
            end=mid-1
        elif midVal < midVal:
            end=mid+1
        else:
            return mid

List=sorted(List)
item='zuza'
result=(binarySearch(List,item))
print('The position of %s is %d.'%(item,result))
