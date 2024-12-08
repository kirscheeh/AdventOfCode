transmission = "110100101111111000101000"

def decode(transmission, decoded_transmission) -> int:
    print(set(transmission))
    if set(transmission) == set(['0']):
        return int(decoded_transmission, 2)
    
    packet_version = transmission[0:3]
    packet_type_id = transmission[3:6]  

    print(list(map(''.join, zip(*[iter(transmission[6:])]*5))))


print(decode(transmission, ""))

