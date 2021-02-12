'==================================SOLVED=================================='
#encrypted_message
enc_message='L[IPICNHtL?aH}O{zCO{>?A.r'
# key: hex --> decimal
key=int('0f',16)
#print(key)
# enc_message: ascii --> decimal
decimal_message=[]
for s in enc_message:
    decimal_message.append(ord(s))
# decryption "bit-flipping attack"
decrypt_message=[]
for n in decimal_message:
    decrypt_message.append(n^key)
#write decrypted message
message=''
for n in decrypt_message:
    message+=chr(n)
print(message)