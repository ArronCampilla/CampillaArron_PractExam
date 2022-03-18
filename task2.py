array =[]
smallest = 0

def min(smallest):
    array = [2,4,6,5,1,3]
    array.sort()
    smallest = array[:1]
    return smallest
        
print("The Smallest is:" + str(min(smallest)))