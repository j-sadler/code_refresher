from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

#for question in question_data:

number = 1

for question in question_data:
    
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


def make_list(q_list):
    bank = []
    for question in q_list:
        
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        bank.append(new_question)
        
    return bank

test_bank = make_list(question_data)

#(question_bank)  

quiz = QuizBrain(test_bank)
#quiz.next_question1()
#quiz.continue_game()

while quiz.still_has_questions():
    answer = quiz.next_question()
    quiz.is_correct(answer)

