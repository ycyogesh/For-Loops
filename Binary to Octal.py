#Binary to Octal Conversion

n = input("Enter Number : ")
sum = 0
j = 0
n1 = len(n)-1

for i in range(n1,-1,-1):
    sum = int(n[int(i)]) * (2**int(j)) + sum
    j+=1
print(sum)
new = sum
rem = 0
a = []
for i in range(0,len(str(new))):
    print(new,"<---------")
    rem = new%8
    new//=8
    print("-------->",new)
    a.append(rem)
a.append(new)
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")
