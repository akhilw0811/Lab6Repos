def encode(password):
    if len(password) != 8:
        return "Your password is required to be 8 digits long."

    encoded_pw = ""

    for digit in password:
            encoded_digit = str((int(digit) + 3) % 10)
            encoded_pw += encoded_digit

    return encoded_pw


# display menu

cont = True

while cont != False:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    # prompt for input
    option = int(input("Please enter an option: "))
    password = input("Please enter your password to encode: ")

    if option == 1:
        encode(password)
        print("Your password has been encoded and stored!")

    if option == 2:
        decode(encoded_pw)
        print(f"The encoded password is {encoded_pw} and the original password is {decoded_pw}.")
    if option == 3:
        cont = False


