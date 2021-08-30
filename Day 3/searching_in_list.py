def search(a,ele):
    c=0
    for i in a:
        if i==ele:
            print("present")
            c=1
            break
    if c==0:
        print("not present")
a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)
b = int(input("Element to be Search: "))
search(a, b)


# Approach 2:

def Searching(Arr, ele):
    count = 0
    if  ele in Arr:
        print("Present")
    else:
        print("Absent")


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)
b = int(input("Element to be Search: "))
Searching(a, b)
