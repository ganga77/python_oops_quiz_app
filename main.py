from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



for questions in question_bank:
    questions = QuizBrain(question_bank)
    questions.next_question()

print(f"Final score is {QuizBrain.score}/{len(question_bank)}")
