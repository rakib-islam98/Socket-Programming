def detect_error(received):
    r = [int(bit) for bit in received[:7]] #exclude overall parity bit
    p1 = r[0] ^ r[2] ^ r[4] ^ r[6]
    p2 = r[1] ^ r[2] ^ r[5] ^ r[6]
    p4 = r[3] ^ r[4] ^ r[5] ^ r[6]
    
    error_position = p4 * 4 + p2 * 2 + p1 * 1
    return error_position

def correct_error(received, error_pos):
    corrected = list(received)
    corrected[error_pos - 1] = '1' if corrected[error_pos - 1] == '0' else '0'
    return ''.join(corrected)

received = input("Enter 8-bit received code: ")
if len(received) != 8 or not set(received).issubset({'0', '1'}):
    print("Invalid input. Must be 8-bit binary.")
else:
    pos = detect_error(received)
    overall_parity = sum(int(b) for b in received[:7]) % 2
    expected_parity = int(received[7])
    
    if overall_parity == expected_parity and pos == 0:
        print("No error detected.")
    elif overall_parity != expected_parity and pos != 0:
        print(f"Single-bit error at position: {pos}")
        corrected = correct_error(received, pos)
        print("Corrected code:", corrected)
        print("It was a single-bit error and has been corrected.")
    else:
        print("Double-bit error detected. Unable to correct.")
