x=(3,78,67,34,88,11,23,19)
print("The tuple is ",x)
even=[]
odd=[]
for i in x:
  if (i%2==0):
    even.append(i)
  else:
    odd.append(i)
print("The even tuple are:")
print(tuple(even))
print("The odd tuple are:")
print(tuple(odd))
