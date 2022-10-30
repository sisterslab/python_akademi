class Questions:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.index = 0

    def getQuestion(self): #index bilgisini alma
        return self.questions[self.index]
    
    def increase_score(self):
        self.score += 100

    def showQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.index + 1}: {question.question}")

        for i in question.choices:
            print("*** " + i)

        answer = input("Cevabınızı giriniz:")
        if question.check_answer(answer):
            print("Tebrikler, doğru bildiniz :)")
            self.increase_score()
        else:
            print(f"Üzgünüm, yanlış cevap verdiniz. Doğru Cevap: {question.answer}")
        self.index += 1

        if len(self.questions) != self.index:
            self.showQuestion()
        else:
            print("Tebrikler, yarışmayı tamamladınız. Toplam puanınız:", self.score)