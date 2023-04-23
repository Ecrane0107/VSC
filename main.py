import random
import os

def read_questions(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    questions = content.split("Question:")
    questions = questions[1:]  # Remove the first empty element

    question_list = []
    for question in questions:
        q_and_a = question.strip().split("Answer:")
        question_text = q_and_a[0].strip()
        answer_text = q_and_a[1].strip()
        question_list.append((question_text, answer_text))
    
    return question_list

def ask_question(question, answer):
    user_answer = input(f"{question} ")
    print()
    show_answer = input("Do you want to see the answer? (yes/no) ")
    print()
    if show_answer.lower() == "yes":
        print(f"The answer is: {answer}")
        print()

    is_correct = input("Did you get it right? (yes/no) ")
    print()
    return is_correct.lower() == "yes"

def main():
    filepath = 'quizgame.txt'
    if not os.path.isfile(filepath):
        print("Invalid file path. Please make sure the file exists and try again.")
        return

    questions = read_questions(filepath)
    
    num_questions = int(input("How many questions do you want to be asked? "))
    print()
    num_correct = 0

    for _ in range(num_questions):
        question, answer = random.choice(questions)
        if ask_question(question, answer):
            num_correct += 1

    score = (num_correct / num_questions) * 100
    print(f"You got {num_correct}/{num_questions} questions right. Your grade is {score}%.")
    print()

if __name__ == '__main__':
    main()
