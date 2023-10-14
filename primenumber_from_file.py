file=open('text.txt','w+')
file=open('text.txt','r')
a=file.read()
b=a.split(",")
num=[]
for i in b:
  if(i!='\n'):
    num.append(int(i))
print(num)
prime=[]
flag=0
for i in num:
  if (i>1):
    p=int(i+1/2)
    for j in range(2,p):
      if (i%j ==0):
        flag=1
      if(flag==0):
        prime.append(i)
      flag=0
print("prime numbers= ",prime)
