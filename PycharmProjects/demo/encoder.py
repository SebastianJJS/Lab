# Sebastian Jurado

def encoder(original_password):
    encoded_password = ''
    for i in original_password:
        digit = int(i) + 3
        if digit > 9:
            digit -= 10
        encoded_password += str(digit)
    return encoded_password


def decoder(encoded_password):
    decoded_password = ''
    for i in encoded_password:
        digit = int(i) - 3
        if digit < 0:
            digit += 10
        decoded_password += str(digit)
    return decoded_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = input("Please enter an option: ")
        if choice == "1":
            original_password = input("Please enter your password to encode: ")
            encoded = encoder(original_password)
            print("Your password has been encoded and stored!\n")
        elif choice == "2":
            decoded = decoder(decoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
        elif choice == "3":
            return False


if __name__ == '__main__':
    main()
