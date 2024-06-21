"""
list=['Ana','Ben','Jack','Maria','Oliver']

search=input("What name would you like to find? ")
found=False

for i in list:
    if search==i:
print('It has found the name ')

if found==False:
    print('Not found')

"""

list=[243,43,64,198,2,1,879,28,48]
list.sort()
print(list)



length=len(list)
upperbound=length-1
lowerbound=0

search=int(input("What number would you like to find? "))

while lowerbound <= upperbound:
    mid=(upperbound+lowerbound)//2

    if list[mid]==search:
        print('The number has been found in the index '+str(mid))
        found=True
        break

    elif list[mid]>search:
        upperbound=mid-1

    elif list[mid]<search:
        lowerbound=mid+1

if found==False:
    print('Number not found')



'''
print('Brian'<'Peter')
list=["Brian", "Meg", "Peter", "Joe", "Stewie", "Lois"]


length=len(list)
upperbound=length-1
lowerbound=0

search=input("What number would you like to find? ")
found=False

while lowerbound <= upperbound:
    mid=(upperbound+lowerbound)//2

    if list[mid]==search:
        print('The number has been found in the index '+str(mid))
        found=True
        break

    elif list[mid]>search:
        upperbound=mid-1

    elif list[mid]<search:
        lowerbound=mid+1

if found==False:
    print('Number not found')
    
'''