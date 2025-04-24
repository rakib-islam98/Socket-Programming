def calculate_parity_bits(data_bits):
    d=[int(bit) for bit in data_bits]
    p1=d[0]^d[1]^d[3]
    p2=d[0]^d[2]^d[3]
    p3=d[1]^d[2]^d[3]
    return [p1,p2,p3] 

def generate_hamming_code(data_bits):
    if len(data_bits) != 4 or not set(data_bits).issubset({'0','1'}):
        raise ValueError("Input must be a 4-bit binary string.")
    
    d=[int(b) for b in data_bits]
    p=calculate_parity_bits(data_bits)

    hamming=[p[0],p[1],d[0],p[2],d[1],d[2],d[3]]
    overall_parity=sum(hamming)%2
    hamming=hamming+[overall_parity]
    return ''.join(str(b) for b in hamming)

data=input("Enter 4-bit binary data: ")
encoded=generate_hamming_code(data)
print("Hamming Code (8-bit):", encoded)
