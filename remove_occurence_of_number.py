a=input("Enter the size of list: ")
list=[]
for i in range(0,a):
  list.append(int(input("Enter the element: ")))
print(list)
p=int(input("Enter the element to remove: "))
for j in list:
  if(j==p):
    list.remove(p)
print(list)
