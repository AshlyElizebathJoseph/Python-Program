a=input("Enter the sentence: ")
b=input("Enter the word to be replaced: ")
c=input("Enter the word to replace: ")
word=a.split()
rep=""
for i in word:
  if (i==b):
    rep=rep+c+" "
  else:
    rep=rep+i+" "
print(rep)
