user_input=str(input("Enter the E for encryption and D for decryption:-"))
word=str(input("Enter the word:-"))
key=int(input("Enter the key:-"))
if user_input == "E" or user_input == "e":
  for i in range(0,len(word)):
    st=word[i]
    result=ord(st)+key
    if st.isupper() == True:
      if result > 90:
        str_res=chr(result - 26)
        print(str_res,end="")
      else:
        str_res=chr(result)
        print(str_res,end="")
    else:
      if result > 122:
        str_res=chr(result - 26)
        print(str_res,end="")
      else:
        str_res=chr(result)
        print(str_res,end="")
elif user_input == "D" or user_input == "d":
  for i in range(0,len(word)):
    st=word[i]
    result=ord(st)-key
    if st.isupper() == True:
      if result < 65:
        str_res=chr(result + 26)
        print(str_res,end="")
      else:
        str_res=chr(result)
        print(str_res,end="")
    else:
      if result < 97:
        str_res=chr(result + 26)
        print(str_res,end="")
      else:
        str_res=chr(result)
        print(str_res,end="")
        
        
        
 word=str(input("Enter the word:-"))
for key in range(0,26):
  print("For key",key," Output:")
  for i in range(0,len(word)):
    st=word[i]
    result=ord(st)-key
    if st.isupper() == True:
      if result < 65:
        str_res=chr(result + 26)
      else:
        str_res=chr(result)
      print(str_res,end="")
    else:
      if result < 97:
        str_res=chr(result + 26)
      else:
        str_res=chr(result)
      print(str_res,end="")
  print("\n")
