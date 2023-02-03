# 問答程式
class Question:
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer


test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n"
]

questions = [
    Question(test[0], "c"),
    Question(test[1], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
    print("你得到" + str(score) + "分,共" + str(len(questions)) + "題")


run_test(questions)
