import json


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

def display_questions(questions):
    for idx, question_data  in enumerate(questions, start=1):
        print(f'Question {idx}: {question_data['question']}')







def main():
    file_path = 'questionsdb.json'
    questions = load_questions(file_path)
    display_questions(questions)
    
    
if __name__ == '__main__':
    main()

