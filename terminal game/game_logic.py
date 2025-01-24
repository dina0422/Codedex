import textwrap

def ask_question(day_mode, question, options, correct_option):
    day_mode_length = len(day_mode)
    wrapped_question = textwrap.fill(question, width=50)
    
    print('-' * (day_mode_length + 5))
    print(f'||{day_mode}||')
    print('-' * (day_mode_length + 5))
    
    print('=' * 50)
    print(wrapped_question)
    print('=' * 50)
    
    for option in options:
        print(option)
    
    valid_options = [option[0] for option in options]  # Extract the first character of each option (e.g., 'a', 'b', 'c')
    
    while True:
        answer = input('Enter your answer: ')
        if answer in valid_options:
            break
        else:
            print(f'Invalid option. Please choose from {", ".join(valid_options)}.')
    
    if answer == correct_option:
        print('Correct!')
        return True
    else:
        print('Incorrect!')
        return False