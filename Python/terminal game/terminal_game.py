import os #to refresh terminal screen
from game_logic import ask_question
import textwrap

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def start_menu():
    clear_screen()
    print('===========================')
    print('||  🎣 PHISH NO MORE 🎣  ||')
    print('===========================')
    print('||[1] Start Game         ||')
    print('||[2] instructions       ||')
    print('||[3] Exit Game          ||')
    print('===========================')

    option = input('Select an option: ')    

    if option == '1':
        start_game()
    elif option == '2':
        instructions()
    elif option == '3':
        exit()
    else:
        print('Invalid option. Please try again.')
        start_menu()
        
def instructions():
    clear_screen()
    print('================================================')
    print('||               INSTRUCTIONS                 ||')
    print('================================================')
    print('||1. Answer the questions                     ||')
    print('||2. Avoid the phishing [❌=💔]||')
    print('||3. Have fun!                                ||')
    print('===============================================')
    
    input('Press Enter to return to the main menu...')
    start_menu()

def start_game():
    clear_screen()
    intro ='Welcome to Phish No More! Your goal is to navigate through a day[4 questions] in the life of a professional and avoid phishing attempts.'
    wrapped_intro = textwrap.fill(intro, width=50)
    print('-------------------')
    print('|| STARTING GAME ||')
    print('-------------------')
    
    print('=' * 50)
    print(wrapped_intro)
    print('=' * 50)
    input('Press Enter to start the game...')
    game()

def game():
    lives = '💚💚💚'
    correct_answers = 0
    clear_screen()
    print('==================')
    print('|| GAME STARTED ||')
    print('==================')
    
    questions = [
        {
            'day_mode' : '🌅 MORNING ROUTINE',
            'question': '1. You opened your ✉️ email and received an urgent message from your bank. What do you do?',
            'options': ['a. Click the link to verify your account', 'b. Ignore the email', 'c. Call the bank to verify the email'],
            'correct_option': 'c'
        },
        {
            'day_mode' : '🍴 LUNCH BREAK',
            'question': '2. You receive a 📞phone call from someone who sounds exactly like your CFO, asking for immediate access to sensitive financial documents due to a "system failure." What do you do?',
            'options': ['a. Provide the access immediately', 'b. Hang up and call the CFO to verify the request'],
            'correct_option': 'b'
        },
        {
            'day_mode' : '💻 AFTERNOON MEETING',
            'question': '3. An ✉️ email arrives from what seems to be your HR department, inviting you to an afternoon meeting about "New Company Policies." The email includes an attachment labeled "Meeting_Agenda.pdf" that you are encouraged to open.',
            'options': ['a. Open the attachment', 'b. Forward the email to your HR department to verify the meeting'],
            'correct_option': 'b'
        },
        {
            'day_mode' : '🏠 END OF DAY REFLECTION',
            'question': '4. You receive an ✉️ email claiming to be from a well-known company offering you a job. It includes an attachment labeled "Job Offer Details" that you can review.',
            'options': ['a. Open the attachment to review the job offer.', 'b. Research the company online to verify if they have an active job listing before opening any attachments.'],
            'correct_option': 'b'
        }
    ]
    
    for q in questions:
        clear_screen()
        print(f'Current Lives: {lives}')
        if ask_question(q['day_mode'], q['question'], q['options'], q['correct_option']):
            correct_answers += 1
        else:
            lives = lives[:-1]
            if not lives:
                game_over()
                return
    
    if len(lives) == 3:
        congrats()
    else:
        motivation(correct_answers)
    
def game_over():
    clear_screen()
    print('=======================')
    print('||  😵GAME OVER😵   ||')
    print('=======================')
    
    input('Press Enter to return to the main menu...')
    start_menu()
    
def congrats():
    clear_screen()
    print('===========================')
    print('||  👏CONGRATULATIONS!👏  ||')
    print('|| You finished the game  ||')
    print('||    with all lives!     ||')
    print('===========================')

    input('Press Enter to return to the main menu...')
    start_menu()

def motivation(correct_answers):
    clear_screen()
    print('=========================================')
    print('||            🤞GOOD TRY!🤞            ||')
    print('=========================================')
    print(f'|| You answered {correct_answers} questions correctly. ||')
    print('|| Keep practicing and                 ||')
    print('|| you will get better!                ||')
    print('=========================================')

    input('Press Enter to restart the game...')
    start_game()
    
start_menu()

