'=======================SOLVED========================='
#encrypted message, remove '%'
mes='%4e%6a%45%32%5a%54%4d%77%4e%7a%51%32%4f%44%59%31%4e%7a%49%31%5a%6a%63%30%4e%6a%45%33%4d%7a%5a%69'.split('%')
m=''
#hex-->ascii
for el in mes[1:]:
    m+=chr(int(el,16))
print(m)
import base64
#decode base64
base64_decode=base64.b64decode('NjE2ZTMwNzQ2ODY1NzI1Zjc0NjE3MzZi').decode()
print(base64_decode)
