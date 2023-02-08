from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

# converting data (set of question and answer) into objets
question_bank=[]
for question in question_data:
    qn_ans=Question(question["question"], question["correct_answer"])
    question_bank.append(qn_ans)

# passing the list of question bank as an object to the quizbrain
random.shuffle(question_bank)
quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    # next_question method gets a question from the question_bank individually and asks for the answer to the user
    quiz.next_question()

print("You've completed the test!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
