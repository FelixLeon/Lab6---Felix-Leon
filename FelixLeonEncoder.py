
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

#Menu
def menu():
    passwordOG = str()
#Left PasswordDec as a placeholder variable for the decoded password,
#feel free to use it or ignore it however you see fit
    passwordDec = str()
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
            print('The encoded password is ' + passwordDec, end='')
            print(', and the original password is ' + passwordOG + '.\n')
        if option == 3:
            break
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
