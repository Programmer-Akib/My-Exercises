import  time


def login():
    name = input('Set name for diary: ')
    password = input('Set password for diary: ')
    correct1 = 0
    while True:
        user_name = input('Enter Login name: ')
        user_pass = input('Enter Login password: ')
        if user_name == name and user_pass == password:
            print('Correct credentials.')
            correct1 += 1
            break
        else:
            print('Incorrect credentials, please try again.\n')
            signup_choice = input('Would you like to change Name and Password? (y/n) : ')
            if signup_choice.lower() == 'y':
                new_name = input('Enter new User name: ')
                new_pass = input('Enter new User password: ')
                name = new_name
                password = new_pass

    return correct1

def write():
    user_confirm = input('Would you like to write in your diary? (y/n) : ')
    if user_confirm == 'n':
        pass
    else:
        user_write = input('Write in your diary:\n')
        with open('Diary.txt','w')as diary:
            diary.write('\n')
            diary.write(user_write)
        print('Writings have been saved..')
        time.sleep(.5)
def view():
    userview_inp = input('Would you like to View inside your diary? (y/n) : ')
    if userview_inp == 'n':
        pass
    else:
        with open('Diary.txt','r')as diary:
            content = diary.read()
            print('Your writings are --')
            print(content)
            time.sleep(.5)

def add():
    userview_inp = input('Would you like to Add to diary? (y/n) : ')
    if userview_inp == 'n':
        pass
    else:
        user_add = input('Add in your diary :\n')
        with open('Diary.txt','a')as diary:
            diary.write('\n')
            diary.write(user_add)
        print('Your writings have been added!')
        time.sleep(.5)

def remove():
    user_removeinp = input("Would you like to Remove All writings in your diary? (y/n) : ")
    if user_removeinp == 'n':
        pass
    else:
        time.sleep(1)
        user_dltconfirm = input('Are you sure? (y/n) : ')
        if user_dltconfirm == 'n':
            pass
        else:
            with open('Diary.txt','w')as diary:
                diary.write('')
            print('You have remove everything inside of your diary! ')
            time.sleep(.5)

correct = login()
if correct == 1:
    print('Welcome to a simple diary program made by Akib.. ')
    time.sleep(1)
    while True:
        write()
        print('----')

        view()
        print('----')

        add()
        print('----')

        remove()
        print('----')

        user_quit = input('Would you like to quit? ("q" to Quit program / "n" to not quit) : ')
        if user_quit == 'n':
            pass
        else:
            break