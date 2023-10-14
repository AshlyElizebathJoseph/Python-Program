file=open('sentence','w+')
file=open('sentence','r')
a=file.read()
word=[]
print(a)
c=a.split(",")
print("Number of sentence: ",len(c)-1)
d=a.split(" ")
print("Number of words in text: ",len(d))
count1=count2=count3=count4=0
for i in a:
  if(i.islower()):
    count1=count1+1
  elif(i.isupper()):
    count2=count2+1
  elif(i.isdigit()):
    count3=count3+1
  else:
    count4=count4+1
print("The number of lowercase characters is: ",count1)
print("The number of uppercase characters is: ",count2)
print("The number of digits is: ",count3)
print("The number of special case  is: ",count4-1)
