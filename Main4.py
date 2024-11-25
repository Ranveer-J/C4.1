num = 23
print("Table of 23")

for i in range(1,11):
    mul = num*i
    print("23 * %d = %d" % (i,mul)) 



num1 = 5
for i in range(0,num1):
    
    for j in range(0,i+1):
        print("*" ,end=" ")

    print("\n")



num = 1
sum = 0
while (num<= 10):
    sum = sum+num
    num= num+1
    
print("The sum of the first ten natural numbers is :" ,sum)





num2 = 43
flag = False


for i in range(2,num2):
    if (num2 % i) == 0 :
        flag = True

if flag:
    print(num2, "is a prime number")
else:
    print(num2, "is not a prime number")
