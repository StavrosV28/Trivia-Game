import json
import random


# Just a message to start the game up and introduce the rules etc.
def welcome_UI():
    print('Welcome to the best trivia game on earth!')
    print()
    print('These questions will be based on video games.')
    print()
    print('There are 3 types of question difficulties. Easy, Medium, and Hard.')
    print()
    print('Easy = 3 pts, Medium = 5 pts, and Hard = 10 pts')
    print()
    


# Load the questions from the JSON file
def load_questions(file_path):
    with open(file_path, 'r')as file:
        questions = json.load(file)
    return questions['results']
    
    
# Displays questions along with their answer choices
def display_questions(questions):
    player_score = 0
    difficulty_level = {
        'easy': 3,
        'medium': 5,
        'hard': 10
    }
    
    # Display the questions on the command line
    for index, question_data  in enumerate(questions, start=1):
        print(f'Question {index}: {question_data['question']}')
        answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
        
        # Display answer choices to user on command line
        for i, option in enumerate(answers, start=1):
            print(f'{i}: {option}')
        
        question_difficulty = question_data['difficulty']
        
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
            if question_difficulty == 'easy':
                player_score += 3
                print(f'You gained 3 points')
                print()
            elif question_difficulty == 'medium':
                player_score += 5
                print('You gained points')
                print()
            elif question_difficulty == 'hard':
                player_score += 10
                print('You gained 10 points')
                print()
        else: 
            print(f'Incorrect! The correct answer was {question_data['correct_answer']}.')

        
    
# For testing
def main():
    file_path = 'questionsdb.json'
    questions = load_questions(file_path)
    random.shuffle(questions)
    welcome = welcome_UI()
    
    # Asking user to see how many questions they would like to answer from the database of questions.
    while True:
        try:
            questions_num = int(input(f'How many questions would you like to answer? (1-{len(questions)}): '))
            if 1 <= questions_num <= len(questions):
                break
            else:
                print(f'Please enter a number between 1 through {len(questions)}')
        except ValueError:
            print('Out of range! Please enter a valid range...')
    
    # Slice the questions up to the desired amount of questions the player wants
    selected_questions = questions[:questions_num]
    
    welcome # Displays Welcome UI
    display_questions(selected_questions) # Shows the questions and their order
    print('Thanks for playing!')
    
if __name__ == '__main__':
    main()

