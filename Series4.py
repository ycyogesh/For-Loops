#Harmonic Series 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms and sum

n = int(input("Enter Number"))
sum = 0

for i in range(1,n+1):
    sum = sum + (1/i)

print(sum)
