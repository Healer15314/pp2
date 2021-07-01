a = list(map(int,input().split()))  
min = 10000000
for x in a:
    if(x>0 and x <min):
        min = x 
print(min)