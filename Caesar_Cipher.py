alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(original_text, shift_amount, cipher_direction):
    output = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        shifted_index = alphabet.index(letter) + shift_amount
        shifted_index %= len(alphabet)
        output += alphabet[shifted_index]

    print(f"The {cipher_direction}d text is: {output}")

    


print("Welcome to Caesar Cipher!")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(original_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")