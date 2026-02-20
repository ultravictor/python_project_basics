import random as rd
import string as st
a=st.punctuation + st.digits + st.ascii_letters+" "
a=list(a)
key=a.copy()
rd.shuffle(key)
#Encrypt
text=input("Enter the message :")
cipher_text=""
for i in text:
    ind=a.index(i)
    cipher_text+=key[ind]
print(cipher_text)
#Decrypt
C_text=input("Enter the encrypted text:")
plain_text=""
for i in C_text:
    index=key.index(i)
    plain_text+=a[index]
print(plain_text)
