import math
import numpy as np

def find_mod_inv(a,m):
    flag = 1
    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            flag =0
            return x
    if(flag==1):
        print("Inverse not found")

m = int(input("Enter value of m :"))
alpha = int(input("Enter value of alpha :"))
q = int(input("Enter value of q:"))
xa = int(input("Enter value of xa :"))
k = int(input("Enter value of k(random no) :"))

ya = np.mod(pow(alpha ,xa),q)
print("Value of ya = ")
print(ya)

s1 = np.mod(pow(alpha,k),q)

kinv = find_mod_inv(k, (q-1))
print("Value of kinv = ")
print(kinv)

s2 = np.mod(kinv*(m-(xa*s1)),(q-1))


print("Value of s1 = ")
print(s1)
print("Value of s2 = ")
print(s2)


# verification
v1 = np.mod(pow(alpha,m),q)
v2 = np.mod((pow(ya,s1)*pow(s1,s2)),q)

print("Value of v1 = ")
print(v1)
print("Value of v2 = ")
print(v2)

if(v1==v2):
    print("Verified")