a=input("enter the text string")   #taking text string from user
b=input("enter the pattern string")  # taking pattern string from user
n=len(a)  #length of text string
m=len(b)   #length of pattern string
res=0
q=0
for i in range(0,n-m+1):
    for j in range(0,m):
        if(a[i+j]!=b[j]):
            break
        else:
            q=q+1
    if(q==m):  #checking how many time pattern string is found
        res=res+1
print(res)
