import json
import random


# Just a message to start the game up and introduce the rules etc.
def welcome_UI():
    print('Welcome to the best trivia game on earth!')
    print('These questions will be based on video games.')
    print('There are 3 types of questions. Easy, Medium, and Hard.')
    print('Easy = 5 pts, Medium = 10 pts, and Hard = 15 pts')


# Load the questions from the JSON file
def load_questions(file_path):
    with open(file_path, 'r')as file:
        questions = json.load(file)
    return questions['results']

# Displays questions along with their answer choices
def display_questions(questions):
    # Display the questions on the command line
    for idx, question_data  in enumerate(questions, start=1):
        print(f'Question {idx}: {question_data['question']}')
        answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
        
        # Display answer choices to user on command line
        for i, option in enumerate(answers, start=1):
            print(f'{i}: {option}')
            
        # Checking if the user enters a number out of range of the answer choices
        while True:
            try:
                player_answer = int(input(f'Give an answer choice of 1 through {len(answers)}: '))
                if 1 <= player_answer <= len(answers):
                    break
                else:
                    print(f'Please enter a number between 1 through {len(answers)}')
            except ValueError:
                print('Invalid input. Please enter a valid answer choice.')
        
        # Check if answer is correct that the user entered.
        if answers[player_answer - 1] == question_data['correct_answer']:
            print('Correct Answer...On to the next!')
        else: 
            print('Incorrect! Next question please.')
    
        
    
# For testing
def main():
    file_path = 'questionsdb.json'
    questions = load_questions(file_path)
    random.shuffle(questions)
    welcome = welcome_UI()
    
    welcome # Displays Welcome UI
    display_questions(questions) # Shows the questions and their order
    
    
if __name__ == '__main__':
    main()

