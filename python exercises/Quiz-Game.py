questions = [{'Questions':'Is the world round?',
                  'Option':['Yes','No','3.141451','Idk'],
                  'Ans':'1'},
                 {'Questions':'What language is "Nihao"?',
                  'Option':['English','Chinese','Korean','Hindi'],
                  'Ans':'2'}]
def quiz():
    score = 0
    print('Welcome to a short Quiz game made by Akib.')
    print('----------------------------------')
    for question in questions:
        print(question['Questions'])
        for i,option in enumerate(question['Option']):
            print(f'{i+1}){option}')
        user_inp = input('(1,2,3,4) : ')
        if user_inp == question['Ans']:
            print('Correct !! ')
            score += 1
        else:
            print('Wrong ?!')

    print('Quiz Finished!')
    print(f'You got {score}/{len(questions)}')
quiz()
