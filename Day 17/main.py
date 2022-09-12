from data import question_data
from question_model import Question
from question_brain import QuestionBrain

questionBank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    questionBank.append(Question(text, answer))

questionBrain = QuestionBrain(questionBank)

while questionBrain.stillHasQuestions():
    questionBrain.nextQuestion()

print(f"The quiz is finished. Your final score is {questionBrain.score}")
