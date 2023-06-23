from cryptography.fernet import Fernet
import time
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb')as keyf:
        keyf.write(key)

def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key


key = load_key()

def view_pwd():
    with open('Pass.txt','r')as f:
        content = f.read()
        if len(content) >= 1 :
            print('Your Passwords are:')
            print('')
            with open('Pass.txt', 'r') as file:
                for line in file.readlines():
                    content = line.rstrip()
                    user, passw = content.split('|')
                    decrypted_pass = Fernet(key).decrypt(passw.encode())
                    print(f'Name: {user} | Password: {decrypted_pass.decode()}')
        else:
            print('')
            print('You have no Passwords saved!')
    time.sleep(1)

def add_pwd():
    user_name = input('Enter Account Name: ')
    user_pass = input('Enter Account Pass: ')
    with open('Pass.txt', 'a') as file:
        encrypted_pass = Fernet(key).encrypt(user_pass.encode())
        file.write(user_name + '|' + encrypted_pass.decode() + '\n')
    print('Password added successfully! ')
    time.sleep(1)
def remove_pwd():
    usersure_inp = input('Are you sure you want to remove ALL passwords? (y/n): ')
    if usersure_inp == 'y':
        with open('Pass.txt','w') as file:
            pass
        print('Passwords deleted successfully. ')
        time.sleep(1)
    else:
        pass

master_name = input('Set name to Password manager: ')
master_pass = input('Set password to Password manager: ')
while True:
    print('------')
    login_name = input('Login Name: ')
    login_pass = input('Login Password: ')
    if login_name == master_name and login_pass == master_pass:
        print('------')
        print('(add) to Add passwords to Passwords manager.')
        print('(delete) to Delete All passwords from Password manager.')
        print('(view) to View all passwords in Password manager. ')
        print('------')
        user_inp = input('(add, delete, view) : ')
        time.sleep(1)
        if user_inp == 'q':
            break
        if user_inp == 'view':
            view_pwd()
        elif user_inp == 'add':
            add_pwd()
            continue
        elif user_inp == 'delete':
            remove_pwd()
        else:
            print('Invalid command..')
    else:
        print('Invalid password and name...')