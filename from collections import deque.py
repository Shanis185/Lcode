
def fn(n,k,arr):
    for i in range(n-k+1):
        curr=arr[i:k+i]
        res.append(max(curr))

    






n=int(input())
k=int(input())
arr=list(map(int,input().split()))

res=[]
fn(n,k,arr)
print(res)

