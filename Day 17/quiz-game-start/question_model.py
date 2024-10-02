class Question():
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
    def ask(self):
        respone = input(self.text)
        if respone == self.answer:
            print("correct")
            
q_1 = Question("what is your name", "joe")

