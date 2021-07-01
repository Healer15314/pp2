l = input().split()
x = int(input())
string = ""
def f(n,l,string):
    string = string +  l[-n:] + l[:-n]

for t in f(x,l,string):
    print(t,end=" ")

 

