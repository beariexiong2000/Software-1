# player status panel

class Player:
    def __init__(self, name, age):  
        self.name = name            
        self.age = age              
        self.team = []
        self.trust_score = 0
        self.identity = "Master.Xuanzang" 

    def show_status(self): 
        print("Player Profile & Status")
        print(f"Player Name: {self.name} (Age: {self.age})")
        print(self.identity)
        print(f"Team Trust Score: {self.trust_score}")
