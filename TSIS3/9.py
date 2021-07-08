a = int(input())
dict1  = dict()
for x in range(a):
    a = list(map(str, input().split()))
    if(dict1.get(a[0])== None):
        dict1[a[0]] = a[1:len(a)]
    else:
        dict1[a[0]] = dict1[a[0]] + a[1:len(a)]
for x,y in dict1.items():
    print(str(x) + ':', ', '.join([k for k in y]))
