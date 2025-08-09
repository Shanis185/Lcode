n=int(input())
listt=list(map(int,input().split()))
curr_sum=max_sum=0
for i in listt:
    
    curr_sum=max(curr_sum+i,i)
    max_sum=max(curr_sum,max_sum)

print(max_sum)
