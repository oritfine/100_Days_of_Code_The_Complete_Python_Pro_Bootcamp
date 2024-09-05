from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

if __name__ == '__main__':

    question_bank = []
    for q in question_data:
        question_bank.append(Question(q['text'], q['answer']))

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completes the quiz!")
    print(f"You final scored was: {quiz.score}/{quiz.question_number}")
