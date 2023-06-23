# TO DO LIST
def display_task():
    if not tasks:
        print('To-Do List is empty.')
    else:
        for i, task in enumerate(tasks):
            print(f'\n{i+1}. {task[0]}')
            if task[1] == False:
                print('✘ Unfinished Task\n')
            if task[1] == True:
                print('✔ Finished Task\n ')


def add_task(user_task):
    tasks.append([user_task, False])
    print('Your Task has been Added !')


def tick_task(user_tick):
    user_tick = int(user_tick)
    if tasks[user_tick-1][1] == False:
        tasks[user_tick-1][1] = True
        print('Task Ticked ✔ !')
    else:
        print('Task is already Ticked')

def untick_task(user_untick):
    user_untick = int(user_untick)
    if tasks[user_untick - 1][1] == True:
        tasks[user_untick - 1][1] = False
        print('Task Crossed ✘ !')
    else:
        print('Task is already Crossed.')


def delete_task(user_dlt):
    user_dlt = int(user_dlt)
    remove_task = tasks[user_dlt-1]
    tasks.remove(remove_task)
    print('Task Deleted ! ')


tasks = []

def todo_list():
    print('Welcome to a TO-DO list programme by Akib. ')
    print('[1]  Displays Tasks in your To-Do list.')
    print('[2]  Adds Task in your To-Do list. ')
    print('[3]  Ticks Task in your To-Do list.')
    print('[4]  Crosses/Unticks Task in your To-Do list. ')
    print('[5]  Deletes Task in your To-Do list. \n')
    while True:
        user_input = input('Type Command [1, 2 , 3, 4 & 5]: ')
        if user_input == '1':
            display_task()

        elif user_input == '2':
            user_task = input('Enter Tasks: ')
            add_task(user_task)

        elif user_input == '3':
            user_tickinp = input('Type the number of the task you want to Tick ✔ : ')
            tick_task(user_tickinp)

        elif user_input == '4':
            user_untick = input('Type the number of the task you want to Cross/Untick ✘ :')
            untick_task(user_untick)
        elif user_input == '5':
            user_dltinp = input('Type the number of the task you want to Delete: ')
            delete_task(user_dltinp)

        else:
            print('Type only [1, 2, 3 & 4]')


todo_list()