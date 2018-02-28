n=int(input("enter the no."))#take no. from user
a=[] # empty list
for i in range(2,n+1):
    a.insert(i,1) #initializing the list
for i in range(2,n+1):
    for j in range(2,n+1):
        if(i*j<n): #check multiple of 2
            a.insert(i*j,0)
for i in range(2,n+1):
    if(a[i]):
      print(i,end=' ') #printing the prime no.