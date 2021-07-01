#forlloop1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#forlloop2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
print(x)
#forlloop3
for x in range(6):
  print(x)

#forlloop4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break

  print(x)