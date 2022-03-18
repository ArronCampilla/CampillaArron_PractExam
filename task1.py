age = int(input("Enter Age:"))

def isTeenager(age):
    
    if age < 19:
        return 'true'
    else:
        return 'false'
    
print(isTeenager(age))