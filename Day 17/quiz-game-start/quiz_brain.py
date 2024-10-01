class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    
    
    
    def next_question1(self):
        
        play = True
    
        while self.question_number < len(self.question_list):    
    
            while play:
                user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}?  ")
                self.question_number +=1
                if user_answer == self.question_list[self.question_number].answer:
                    print("correct")
                elif user_answer == "end game":
                    play = False
                else:
                    print("incorrect")
            

            
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        return user_answer
        
        
    def is_correct(self, answer):
        
        if answer == self.question_list[self.question_number].answer:
            
            self.score += 1
            print(f"correct! your score is {self.score}")
        else:
            print(f"incorrect! your score is {self.score}")
        
        
        

        
        