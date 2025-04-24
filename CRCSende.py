import random
import time
import socket

def xor(a,b):
    result=[]
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend,divisor):
    pick=len(divisor)
    temp=dividend[0:pick]
    
    while pick<len(dividend):
        if temp[0]=='1':
            temp=xor(temp,divisor)+dividend[pick]
        else:
            temp=xor('0'*len(divisor),temp)+dividend[pick]
        pick+=1
    if temp[0]=='1':
        temp=xor(temp,divisor)
    else:
        temp=xor('0'*len(divisor),temp)
    return temp

def encode_data(data,key):
    l_key=len(key)
    append_data=data+'0'*(l_key-1) 
    remainder=mod2div(append_data,key)
    codeword=data+remainder
    print("\nSender Side")
    print(f"Data: {data}")
    print(f"Remainder: {remainder}")
    print(f"Encoded Data: {codeword} with Key: {key}")
#Additional logic for error seeding
    index=random.randint(0,len(codeword)-1)
    bit='1' if codeword[index]=='0' else '0'
    if random.random()<0.5:
        codeword=codeword[:index]+bit+codeword[index+1:]
        print("1 bit error seeded")
        print("Erroneous Data: "+codeword)
    return codeword

sender=socket.socket()
sender.connect(('localhost',12345))

for i in range(10):
    print()
    print(i+1)
    #data=input("Enter data: ")
    data=''.join(random.choice('01') for _ in range(5))
    #key=input("Enter key: ")
    key='1101'
    codeword=encode_data(data,key)
    print("Sending data...")
    sender.send(codeword.encode())
    time.sleep(0.5)
sender.close()
