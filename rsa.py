from decimal import Decimal 
  
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))

def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True
 
check_p = prime_check(p)
check_q = prime_check(q)
while(((check_p==False)or(check_q==False))):
    print("\nYour input is not prime number...... ")
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

message = int(input("Enter the Message:-"))

n = p * q 

totient = (p-1)*(q-1) 

def gcd(m,n): 
    if n==0: 
        return m 
    else: 
        return gcd(n,m%n) 

for k in range(2,totient): 
    if gcd(k,totient)== 1: 
        break
  
  
for i in range(1,10): 
    x = 1 + i*totient 
    if x % k == 0: 
        d = int(x/k) 
        break
        
print('\nn = '+str(n))
print('totient = '+str(totient))
print('Public key = '+str(k))
print('Private key = '+str(d))

while True:
  user_in =str(input("\nEnter E for encryption and D for decryption:-"))
  if user_in == 'E':
    local_cipher = Decimal(0) 
    local_cipher =pow(message,k) 
    cipher_text = local_cipher % n  
    print('cipher text = '+str(cipher_text)+' with public key = '+str(k))
  elif user_in == 'D':
    decrypt_t = Decimal(0) 
    decrypt_t= pow(cipher_text,d) 
    decrpyted_text = decrypt_t % n 
    print('decrypted text = '+ str(decrpyted_text) +' with private key = '+str(d))
    break
