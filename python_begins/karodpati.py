# import necessary modules
import random

# define the quiz questions and answers
quiz = {
    'What is the capital of India?': ['A. Delhi', 'B. Mumbai', 'C. Kolkata', 'D. Chennai', 'A'],
    'What is the largest planet in our solar system?': ['A. Jupiter', 'B. Saturn', 'C. Uranus', 'D. Neptune', 'A'],
    'What is the national animal of India?': ['A. Tiger', 'B. Elephant', 'C. Lion', 'D. Leopard', 'A'],
    'Which country gifted the Statue of Liberty to the USA?': ['A. Spain', 'B. France', 'C. Italy', 'D. Germany', 'B'],
    'What is the currency of Japan?': ['A. Yen', 'B. Dollar', 'C. Euro', 'D. Pound', 'A']
}

# define the prize money for each correct answer
prize_money = [0, 1000, 5000, 10000, 50000, 100000]

# shuffle the quiz questions
questions = list(quiz.keys())
random.shuffle(questions)

# start the quiz
print('Welcome to Kaun Banega Crorepati!')
print('You will be asked a series of questions. Answer each question correctly to win money.')

# loop through the questions
for i, question in enumerate(questions, start=1):
    # print the question and answer choices
    print(f'\nQuestion {i}: {question}')
    for choice in quiz[question][:-1]:
        print(choice)
    # get the user's answer
    user_answer = input('Enter your answer (A/B/C/D): ')
    # check if the answer is correct
    if user_answer.upper() == quiz[question][-1]:
        print('Correct answer!')
        # award prize money
        prize = prize_money[i]
        if prize > 0:
            print(f'You have won Rs. {prize}!')
    else:
        print('Sorry, incorrect answer.')
        break

print('\nThanks for playing Kaun Banega Crorepati!')
