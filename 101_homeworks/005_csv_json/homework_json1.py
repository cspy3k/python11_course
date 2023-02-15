import json

# answer_question() - function to take one question as an argument
# return user picked answer
def answer_question(question):
    while True:
        input(f'1.{question[0]} 2.{question[1]}\n'
              f'3.{question[2]} 4.{question[3]}')
        user_choice = input('Your answer? -> ')
        if user_choice.lower() == 'exit':
            print('Good bye')
            quit()
        if user_choice in '1234':
            return question[int(user_choice) - 1]
        else:
            print('Choice is out of range. Try again or type "exit" to quit.')


# check_answer() - function takes right answer and user answer
# campares them and return True or False
def check_answer(answer, user_answer):
    if user_answer == answer:
        return True
    return False

# start_quiz() - function to start quiz
def start_quiz(topic, data):
    quiz = data[topic]
    score = 0
#    print(quiz)
    for question in quiz.values():
        print(question.get('question'))
        user_answer = answer_question(question.get('options'))
        if check_answer(question.get('answer'), user_answer):
            score += 1
    print(f'You answered {score} questions right!')
# main() - function to control quiz process
def main(data):
    print('Hello, welcome to our quiz!')
    print(f'You can choose from {len(data.keys())}topics.')
#    counter = 1
    for topic in data.keys():
        print('*', topic)
    while True:
        quiz_topic = input('Type topic name to continue or "exit" to quit. ->')
        if quiz_topic.lower() == 'exit':
            print('Good bye!')
            quit()
        if quiz_topic.lower() in data.keys():
            start_quiz(quiz_topic.lower(), data)
            if input('Another quiz? y/n '.lower == 'y'):
                main(data)
            else:
                print('Good bye!')
                quit()
        else:
            print(f'There is "{quiz_topic}" topic.')

with open('data/quiz.json', 'r', encoding='UTF-8') as file:
    quiz_data = json.load(file).get('quiz')
print(quiz_data)

main(quiz_data)