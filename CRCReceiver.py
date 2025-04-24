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

def decode_data(codeword,key):
    remainder=mod2div(codeword,key)
    print("\nReceiver Side")
    print(f"Received Codeword: {codeword}")
    print(f"Calculated Remainder: {remainder}")
    if '1' in remainder:
        print("Error detected in received data!")
    else:
        print("No error detected. Data is correct!")
        print(f"Actual Data: {codeword[:-len(key)+1]}")

#codeword=input("Enter data: ")
#key=input("Enter key: ")
key='1101'

receiver=socket.socket()
receiver.bind(('localhost',12345))
receiver.listen(1)
print("Receiver is waiting for data...")
conn,addr=receiver.accept()
print("Connected by",addr)

for i in range(10):
    print()
    print(i+1)
    codeword=conn.recv(1024).decode()
    if not codeword:
        break
    decode_data(codeword,key)
    
conn.close()
