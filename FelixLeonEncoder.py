
#Felix Leon
#Encoder
def encoder(password):
    password = list(str(password))
    number = int()
    for i in range(0, 8):
        number = int(password[i])
        number += 3
        if number > 9:
            number -= 10
        password[i] = str(number)
    password = ''.join(password)
    return password


# Valerie Samuels wrote this decoding function
def decode(password):
    decoded_password = ""

    # take each number in the password and subtract 3 from it
    for num in password:
        decoded_num = int(num) - 3

        # account for the 0 to 9 number limit
        if decoded_num < 0:
            decoded_num += 10

        decoded_password += str(decoded_num)

    return decoded_password


#Menu
def menu():
    passwordOG = str()
#Left PasswordDec as a placeholder variable for the decoded password,
#feel free to use it or ignore it however you see fit
    while True:
        print("Menu\n----------------\n1. Encode\n2. Decode\n3. Quit")
        print('\nPlease enter an option: ', end='')
        option = int(input())
        if option == 1:
            print('Please enter your password to encode: ', end='')
            passwordOG = input()
            print('Your password has been encoded and stored!')
            print('\n')
            passwordOG = encoder(passwordOG)
#Option 2 calls on PasswordDec
        if option == 2:
            # I moved the password_dec inside this option 2
            password_dec = decode(passwordOG)
            print('The encoded password is ' + passwordOG, end='')
            print(', and the original password is ' + password_dec + '.\n')
        if option == 3:
            break
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
