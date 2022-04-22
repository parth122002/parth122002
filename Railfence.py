user_input=str(input("Enter the E for encryption and D for decryption:-"))
message=input("Enter string: ")
user_key=int(input("Enter key: "))
matrix=[[" " for i in range(len(message))] for j in range(user_key)]
if user_input == "E" or user_input == "e":
  flag=0
  row=0
  for i in range(len(message)):
    matrix[row][i]=message[i]
    if row==0:
      flag=0
    elif row==user_key-1:
      flag=1
    if flag==0:
      row+=1
    else:
      row-=1
  print("\nMatrix Formation:")
  for i in range(user_key):
    print("".join(matrix[i]))

  ct=[]
  for i in range(user_key):
      for j in range(len(message)):
          if matrix[i][j]!=' ':
              ct.append(matrix[i][j])

  print("\nCipher Text: ","".join(ct))

elif user_input == "D" or user_input == "d":
  dir_down = None
  row, col = 0, 0
  for i in range(len(message)):
    if row == 0:
      dir_down = True
    if row == user_key - 1:
      dir_down = False
         
    matrix[row][col] = '*'
    col += 1
         
    if dir_down:
      row += 1
    else:
      row -= 1
             
   
  index = 0
  for i in range(user_key):
    for j in range(len(message)):
      if ((matrix[i][j] == '*') and (index < len(message))):
        matrix[i][j] = message[index]
        index += 1
  print("\nMatrix Formation:")       
  for i in range(user_key):
    print("".join(matrix[i]))

  result = []
  row, col = 0, 0
  for i in range(len(message)):
    if row == 0:
      dir_down = True
    if row == user_key-1:
      dir_down = False
             
    if (matrix[row][col] != '*'):
      result.append(matrix[row][col])
      col += 1
             
    if dir_down:
      row += 1
    else:
      row -= 1
  
  print("\nPlain Text: ","".join(result))

print("\nD20DCS176 - Parth Mangukiya")
