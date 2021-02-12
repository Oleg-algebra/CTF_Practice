'=================================SOLVED================================='
#p and q - rsa divisors
p=256128251579833588962640669288236343457
q=334659195040579408284360462422195488949

# e - public key
e=65537
# c - encrypted message
c=4541193573047010079622862634544566667638995016075815652287123393675051074423
# message - decrypted message in decimal form
message=167269892078202100584180265768846377249494409110894
RSA_100=p*q
num=(p-1)*(q-1)
import sympy
# d - private key
d=sympy.mod_inverse(e,num) # find d
hex_message=hex(message)  # transform message from decimal to hex
print(d)
print(RSA_100)
print(num)
