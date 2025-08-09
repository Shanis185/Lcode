n=int(input())
arr=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    arr.append((a,b))
count=1
arr1=sorted(arr,key=lambda x:x[1])
end=arr1[0][1]
for i in range(1,n):
    if arr1[i][0]>=end:
        count+=1
        end=arr1[i][1]
print(count)