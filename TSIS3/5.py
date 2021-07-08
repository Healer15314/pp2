l = input().split()
x = int(input())
u = ""
def f(n,l,string):
    string = string +  l[-n:] + l[:-n]
    return string
new_string = f(x,l,u)
for t in new_string:
    print(t,end=" ")

 

