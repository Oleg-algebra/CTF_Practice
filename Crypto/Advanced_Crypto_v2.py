"===========================SOLVED========================="
"===================CODE DOESN'T WORK===================="

import time
import codecs
import itertools
import string
LENGTH=6

file=open('encrypt_message.txt','r')
message=''
for line in file:
    message+=line
file.close()
#print(message[0:1047])


def divide_text(text,ln):
    lst=[]
    length=ln
    k=0

    n=int(len(text)/length)
    #print(n)
    #print(len(text)/length)
    while True:
        block = ''
        try:
            if k<n:
                block+=text[k*length:(k+1)*length]
                lst.append(block)
                k+=1
            else:
                raise IndexError
            #print(block)
        except IndexError:
            lst.append(text[k*length:])
            break

    return lst

def select_symbols(lst_blocks,ln):
    l=ln

    lst_char=[]

    for k in range(l):
        n_char = ''
        for block in lst_blocks:
            try:
                n_char+=block[k]
            except IndexError:
                break
        lst_char.append(n_char)

    return lst_char

def is_right_byte(lst,bt):
    for char in lst:
        if chr(ord(char)^bt) not in string.printable:
            return False
        else:
            continue

    return True

def key_breaker(lst_key):
    key_parts = {}
    count=0
    for el in lst_key:
        lst=[]
        for i in range(0,257):
            if is_right_byte(el,i):
                lst.append(i)
        key_parts['block_'+str(count)]=lst
        count+=1

    return key_parts



def block_dist(str1,str2):
    if len(str1)!=len(str2):
        return 'LENGTH ERROR!'

    s1=bytearray(str1.encode())
    s2=bytearray(str2.encode())

    result=bytearray()

    for i in range(len(s1)):
        result.append(s1[i]^s2[i])

    return result

def norm_hamming_distance(lst,ln):
    dist=0
    #print(lst)
    for i in range(len(lst)-1):
        #print(lst[i])
        for j in range(i+1,len(lst)-1):
            dist+=bin(int(codecs.encode(block_dist(lst[i],lst[j]),encoding='hex'),16)).count('1')

    return dist/len(lst)/ln

def guess_key_length(text):
    key_length={}
    lst=[]
    for length in range(1,int(len(text)/2)):
        if norm_hamming_distance(divide_text(text,length),length)!=0:
            key_length[length]=norm_hamming_distance(divide_text(text,length),length)

    return dict(sorted(key_length.items(), key=lambda item: item[1]))

def create_key(dct):
    return itertools.product(*dct.values(),repeat=1)

#print(guess_key_length(message))
'''
for k,v in guess_key_length(message).items():
    print('{} | {} \n'.format(k,v))

'''
'''
for key,value in key_breaker(select_symbols(divide_text(message,LENGTH),LENGTH)).items():
    print('{} | {} \n'.format(key,value))
    print(len(value))
    #print(type(value))
time.sleep(30)
for el in create_key(key_breaker(select_symbols(divide_text(message,LENGTH),LENGTH))):
    print('{} \n'.format(el))
'''


