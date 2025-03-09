import re
import os
class player:
    def __init__(self):
        self.name=" "
        self.sympol=" "
    def chooseName(self):
        self.name =input("📝 Please enter your  name: ").strip()
        while not self.nameValidator(self.name):
            self.name =input("📝 Please enter valid name containing only letters: ").strip()
             
              
    @staticmethod
    def nameValidator(name):
        name_regex = re.compile(r"^[a-zA-Z].*")
        return bool(name_regex.match(name))   
    

    def chooseSympol(self):
        self.sympol=input(f"{self.name}  choose one letter only: ").upper()
        while not self.isSingleCharacter(self.sympol):
            self.sympol=input("Please Choose a single letter: ").upper()

            
         
    @staticmethod
    def isSingleCharacter(char):
        return len(char)== 1 and char.isalpha()
    

class menu:
    def __init__(self):
        pass

    def display_mainMenu(self):
        print("💡 Welcome to the 🚀 Tic-Tac-Toe Game! 🎮")
        print("📌 1️⃣  Start Game ✅")
        print("📌 2️⃣  End Game ❌")
        while True:
            choice = input("Please enter your choice (1/2): ")
            if  choice not in ("1", "2"):
                print("⚠️ You must choose 1 or 2 only! Try again.")
                continue
        
            return choice  


        
    def display_gameMenu(self):
        print("📌 1️⃣  Restart Game ♻️")
        print("📌 2️⃣  Exit Game ❌")
        print("===========================\n")
        while True:
            choice = input("Please enter your choice (1/2): ").strip()
            
            if choice not in ("1", "2"):
                print("⚠️ You must choose 1 or 2 only! Try again.")
                continue
            
            return choice
        

class Board:
    def __init__(self):
        self.board=[str(i+1) for i in range(9) ]


    def displayBoard(self):
        print("\n🎮 Current Board State:\n")
        for i in range(0, 9, 3):
            print(f"  {self.board[i]}  |  {self.board[i+1]}  |  {self.board[i+2]}  ")
            if i < 6:
                print("-----|-----|-----")
        print("\n")


    def updateBoard(self,choice,symbol):
        if self.isValidMove(choice) : 
            self.board[choice-1]=symbol
            return True  
        else:
            return False


    def isValidMove(self,choice):
        return self.board[choice-1].isdigit()
    
    def resetBoard(self):
        self.board=[str(i+1) for i in range(9) ]



class Game:
    def __init__(self):
        self.board=Board()
        self.players=[player(),player()]
        self.menu= menu()
        self.currentPlayerINdex=0

    def startGame(self):
        choice=self.menu.display_mainMenu()
        if choice == "1":
            self.setupPlayers()
            self.clear_console()
            self.playGame()
        else:
            self.quitGame()

    def setupPlayers(self):
        for index,player in enumerate(self.players,start=1):
            print(f"Player {index}: Enter Your Details")
            player.chooseName()
            player.chooseSympol()             
            print("-"*50)
    def playGame(self):
        while True:
            player.name,player.sympol=self.play_turn()
            if self.check_win(player.name,player.sympol) or self.check_draw():
                choice =self.menu.display_gameMenu()
                if(choice == "1"):
                    self.restartGame()
                else:
                    self.quitGame()
                    break
            

 

    def check_win(self,playerName,playerSympol):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]  
        ]

        for a, b, c in winning_combinations:
            if self.board.board[a] == self.board.board[b] == self.board.board[c]:
                self.clear_console()
                print(f"\n🎉🎊 Congratulations, {playerName}! 🎊🎉")
                print(f"🏆 {playerName} wins the game with '{playerSympol}'! 🏆")  
                return self.board.board[a]  

        return False  
    def check_draw(self):
        for cell in self.board.board:
            if cell.isdigit():
                return False
        self.clear_console()    
        print("\n🤝 It's a Draw! No one wins this time. 🔄")    
        return True               
    def play_turn(self):
        player=self.players[self.currentPlayerINdex]
        self.clear_console()
        self.board.displayBoard()
        print(f"\n🎲 {player.name}'s Turn ({player.sympol})")
        while True:
            try:
                    choice = int(input("📍 Choose an available cell (1-9): "))
                    if 1<=choice <=9 and self.board.updateBoard(choice,player.sympol):
                        print(f"✅ Move registered! {player.name} placed '{player.sympol}' in cell {choice}.\n")
                        break
                    else:
                        print("❌ Invalid move! That cell is already taken or out of range. Try again.\n")
            except ValueError:
                print("⚠️ Invalid input! Please enter a number between 1 and 9.\n")

        self.switch_player()
        return player.name,player.sympol    
            
    def switch_player(self):
        self.currentPlayerINdex= 1- self.currentPlayerINdex         
           

                    


    def quitGame(self):
        exit()
    def restartGame(self):
        self.clear_console()
        print("\n🔄 Restarting the game... Get ready! 🎮")
        print("===================================")
        self.board.resetBoard()
        self.currentPlayerINdex=0
        self.startGame()    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear') 
  
    


game= Game()
game.startGame()

