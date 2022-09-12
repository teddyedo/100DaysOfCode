class QuestionBrain:
    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        userAnswer = input(
            f"Q.{self.questionNumber}: {currentQuestion.text} (True/False): ")
        self.checkAnswer(userAnswer, currentQuestion.answer)

    def stillHasQuestions(self):
        return len(self.questionList) > self.questionNumber

    def checkAnswer(self, userAnswer, answer):
        if userAnswer.lower() == answer.lower():
            print("That's right!")
            self.score += 1
        else:
            print("That's wrong!")
            print(f"The correct answer was: {answer}.")
        print(f"Your current score is {self.score}/{self.questionNumber}")
