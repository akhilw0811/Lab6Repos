def encode(password):
    if len(password) != 8:
        return "Your password is required to be 8 digits long."

    encoded_pw = ""

    for digit in password:
            encoded_digit = str((int(digit) + 3) % 10)
            encoded_pw += encoded_digit

    return encoded_pw

def decode(encrypted):
    """decodes an encoded string"""
    decoded_str = ""
    for i in encrypted:
        char = chr(ord(i) - 3)
        if char == "/":
            char = "9"
        elif char == ".":
            char = "8"
        elif char == "-":
            char = "7"
        decoded_str += char
    return decoded_str

encoded = ""
# display menu
cont = True

while cont != False:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    # prompt for input
    option = int(input("Please enter an option: "))

    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded = encode(password)
        print("Your password has been encoded and stored!\n")

    elif option == 2:
        decoded = decode(encoded)
        print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")

    elif option == 3:
        cont = False


