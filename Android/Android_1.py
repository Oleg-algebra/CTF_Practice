lst=[100, -1, 127, -57, -59, 62, 56, 8, 46, -40, -52, -10, -104, -74, 12, -63]
encypt_message=int('0xfe546279a62683de8ca334b673420696',16)
decrypt_message=[]
print(encypt_message)
#print(len(bytearray(encypt_message)))

def find_info():

    a = [48, 59, 44, 59, 116, 41, 63, 57, 47, 40, 51, 46, 35, 116, 23, 63, 41, 41, 59, 61, 63, 30, 51, 61, 63, 41, 46]
    b=[-30, -32, -15, -52, -21, -10, -15, -28, -21, -26, -32]
    c=[65, 72, 57]

    m=''
    d=''
    f=''
    for i in a:
        m+=chr(i^90)
    for i in b:
        d+=chr(i^-123)
    for i in c:
        f+=chr(i^12)

    print(m)
    print(d)
    print(f)

def base_n(number,base):
    base_list=[]
    num=number
    while num>=base:
        base_list.append(num%base)
        num=num//base
        if num<base:
            base_list.append(num)
        #print(num)
    return base_list[-1::-1]

def from_base_n_to_decimal(base,base_list):
    number = 0
    for i in range(len(base_list)):
        number+=base_list[i]*base**(len(base_list)-1-i)
    return number

def reverse():

    lst = [100, -1, 127, -57, -59, 62, 56, 8, 46, -40, -52, -10, -104, -74, 12, -63]
    res=[]
    lst1=bytearray(base_n(encypt_message,256))

    for i in range(len(lst1)):
        res.append((lst1[i]+lst[i])%256)
    #print(res)
    return bytes(res)


def print_m1():
    m1='fe 54 62 79 a6 26 83 de 8c a3 34 b6 73 42 06 96'.split()
    l=[]
    for i in m1:
        l.append(int(i,16))

    return l

import Crypto.Hash.MD5 as md5
md5_orig_message=md5.new()
md5_orig_message.update(reverse())
print(md5_orig_message.hexdigest())
print(int('fe546279a62683de8ca334b673420696',16))
l=[]
for i in base_n(encypt_message,256):
   l.append(i&0xff)
print(*l)
print(*base_n(encypt_message,256))

#print(len(base_n(encypt_message,256)))
#print(decrypt_message)