class QuizBrain:
    score = 0
    question_number = 0

    def __init__(self, q_list):
        #self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[QuizBrain.question_number]
        QuizBrain.question_number += 1
        answer = input(f"Q. {QuizBrain.question_number} : {current_question.question} (True/False)?")
        if answer == current_question.answer:
            QuizBrain.score += 1


