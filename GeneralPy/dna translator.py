# Encoding Map
encode_map = {
    'TTT': 'A',
    'TAC': 'B',
    'AGG': 'C',
    'GCT': 'D',
    'AAG': 'E',
    'CTC': 'F',
    'GAT': 'G',
    'CAA': 'H',
    'GAC': 'I',
    'CCC': 'J',
    'AAT': 'K',
    'CGC': 'L',
    'ATC': 'M',
    'GCA': 'N',
    'AAA': 'O',
    'TCA': 'P',
    'GAG': 'Q',
    'TCC': 'R',
    'GCG': 'S',
    'GGT': 'T',
    'CTG': 'U',
    'TAG': 'V',
    'CAG': 'W',
    'TGG': 'X',
    'TCG': 'Y',
    'ACC': 'Z'
}

decode_map = {v: k for k, v in encode_map.items()}

def encode_text(text):
    encoded = ''
    for i in range(0, len(text),  3):
        triplet = text[i:i+3]
        if triplet in encode_map:
            encoded += encode_map[triplet]
    return encoded

def decode_text(encoded_text):
    decoded = ''
    for char in encoded_text:
        if char in decode_map:
            decoded += decode_map[char]
    return decoded

def main():
    print("Choose to encode or decode:")
    print("1. Decode")
    print("2. Encode")
    choice = input("Enter your choice (1 or  2): ")

    if choice == '1':
        text = input("Enter the text to deocode: ").upper()
        encoded = encode_text(text)
        print(f"Encoded text: {encoded}")
    elif choice == '2':
        encoded_text = input("Enter the encoded text to encode: ").upper
        decoded = decode_text(encoded_text)
        print(f"Decoded text: {decoded}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
