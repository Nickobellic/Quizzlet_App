import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = html.unescape(self.current_question.text)
        return f"Q{self.question_number}:{question}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer.lower()
        if user_answer == 0 and correct_answer == 'false':
            return True
        elif user_answer == 1 and correct_answer == 'true':
            return True
        else:
            return False

