import json
import random
import html


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
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return questions['results']
    
    
# Displays questions along with their answer choices
def display_questions(questions):
    score_map = {'easy': 3, 'medium': 5, 'hard': 10}
    player_score = 0
    
    # Display the questions on the command line
    for index, question_data  in enumerate(questions, start=1):
        print('-' * 50)
        # question_text will decode the HTML entities from the JSON file
        question_text = html.unescape(question_data['question'])
        print(f'Question {index}: {question_text}')
        
        answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
        answers = [html.unescape(ans) for ans in answers]
        random.shuffle(answers)
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
            points = score_map.get(question_data['difficulty'], 0)
            player_score += points
            print(f'You gained {points} points. Total score: {player_score}\n')
        else:
            print(f'Incorrect. The correct answer was: {question_data["correct_answer"]}\n')
            
    print(f'Your total score was: {player_score}')
        
        
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
    
    welcome = welcome_UI # Displays Welcome UI
    
    welcome
    display_questions(selected_questions) # Shows the questions and their order
    print('Thanks for playing!')
    
if __name__ == '__main__':
    main()

