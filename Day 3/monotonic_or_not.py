def monotonic_list(a):
    return (all(a[i]<a[i+1] for i in range(len(a)-1)) or all(a[i]>=a[i+1] for i in range(len(a)-1)))
ar= []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    ar.append(element)
if monotonic_list(arn):
    print("Yup, It's an Monotonic List")
else:
    print("No, It's not an Monotonic List")
