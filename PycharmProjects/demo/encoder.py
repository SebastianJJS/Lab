# Sebastian Jurado

def encoder(original_password):
    encoded_password = ''
    for i in original_password:
        digit = int(i) + 3
        if digit > 9:
            digit -= 10
        encoded_password += str(digit)
    return encoded_password




if __name__ == '__main__':
    print(encoder(input("password: ")))
