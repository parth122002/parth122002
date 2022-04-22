import string
import itertools
import pandas as pd, numpy as np
message=str(input("Enter the message:-"))
user_key=str(input("Enter the key:-"))

st="abcdefghiklmnopqrstuvwxyz"
string=[]
matrix=pd.DataFrame([[0 for i in range (5)] for j in range(5)])
for key in range(len(user_key)):
  if user_key[key] == 'j':
    string.append('i')
  elif user_key[key] not in string:
    string.append(user_key[key])
  
for i in range(len(st)):
  if st[i] not in string:
    string.append(st[i])

index=0
for row in range(0,5):
  for col in range(0,5):
    matrix[row][col] = string[index]
    index+=1

print("\n5x5 Matrix:")
for i in range(5):
    for j in range(5):
        print(matrix[i][j], end = " ")
    print()

print("\nMessage in pair:")
for s in range(0,len(message)+1,2):
  if s<len(message)-1:
    if message[s]==message[s+1]:
      message=message[:s+1]+'x'+message[s+1:]
    if len(message)%2 != 0:
        message = message[:]+'x'
print(message)

print("\nEncrypt Cipher:")
for letter in range(0,len(message)-1,2):
  result = list(zip(*np.where(matrix.values == message[letter])))
  result1 = list(zip(*np.where(matrix.values == message[letter+1])))
  ix=result,result1
  for q,w in result:
    for e,r in result1:
      if q == e:
        if r == 4: 
          print(matrix[w+1][e]+matrix[0][q],end="")
        elif w == 4:
          print(matrix[0][e]+matrix[r+1][q],end="")
        else:
          print(matrix[w+1][e]+matrix[r+1][q],end="")
      elif w == r:
        if q == 4:
          print(matrix[r][0]+matrix[w][e+1],end="")
        elif e == 4:
          print(matrix[r][q+1]+matrix[w][0],end="")
        else:
          print(matrix[r][q+1]+matrix[w][e+1],end="")
      else:
        print(matrix[w][e]+matrix[r][q],end="")


print("\n")



import string
import itertools
import pandas as pd, numpy as np
message=str(input("Enter the message:-"))
user_key=str(input("Enter the key:-"))

st="abcdefghiklmnopqrstuvwxyz"
string=[]
matrix=pd.DataFrame([[0 for i in range (5)] for j in range(5)])
for key in range(len(user_key)):
  if user_key[key] == 'j':
    string.append('i')
  elif user_key[key] not in string:
    string.append(user_key[key])
  
for i in range(len(st)):
  if st[i] not in string:
    string.append(st[i])

index=0
for row in range(0,5):
  for col in range(0,5):
    matrix[row][col] = string[index]
    index+=1

print("\n5x5 Matrix:")
for i in range(5):
    for j in range(5):
        print(matrix[i][j], end = " ")
    print()

print("\nEncrypt Cipher:")
for letter in range(0,len(message)-1,2):
  result = list(zip(*np.where(matrix.values == message[letter])))
  result1 = list(zip(*np.where(matrix.values == message[letter+1])))
  ix=result,result1
  for q,w in result:
    for e,r in result1:
      if q == e:
        if r == 0: 
          print(matrix[w-1][e]+matrix[4][q],end="")
        elif w == 0:
          print(matrix[4][e]+matrix[r-1][q],end="")
        else:
          print(matrix[w-1][e]+matrix[r-1][q],end="")
      elif w == r:
        if q == 0:
          print(matrix[r][4]+matrix[w][e-1],end="")
        elif e == 0:
          print(matrix[r][q-1]+matrix[w][0],end="")
        else:
          print(matrix[r][q-1]+matrix[w][e-1],end="")
      else:
        print(matrix[w][e]+matrix[r][q],end="")

print("\n")
