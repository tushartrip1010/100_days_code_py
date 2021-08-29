def fibo(a):
    m,n=0,1
    count=0
    if a<=0:
        print("wrong input")
    elif a==1:
        print("fibonacci series: {m}")
    else:
        print("fibonacci series:",end="")
        while count<a:
            count+=1
            print(m,end="")
            nth=m+n
            m=n
            n=nth
a = int(input("How Many Terms do you want to Display: "))
fibo(a)
         
