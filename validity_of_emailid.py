a=input("Enter the mail id: ")
id=a.split("@")
list=["gmail.com","yahoo.com"]
for k in id:
  for i in list:
    if (k==i):
      print("email valid")
      flag=1
      break
    else:
      flag=0
if(flag==0):
  print("email invalid")
