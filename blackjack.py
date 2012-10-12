import random

class Deck:
    cards = ["Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
             "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
             "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
             "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
             "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
             "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
             "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
             "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
             "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds",
             "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
             "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
             "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
             "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
             "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
             "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
             "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
             "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
             "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds",
             "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
             "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
             "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
             "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
             "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
             "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
             "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
             "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
             "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds", 
             "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
             "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
             "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
             "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
             "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
             "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
             "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
             "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
             "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds", 
             "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
             "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
             "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
             "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
             "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
             "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
             "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
             "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
             "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds"]
    
    def shuffle(self):
        random.shuffle(self.cards) 


class Game:
    deck = Deck()
    type = 0
    players = []
    dealer = []

    def reset(self):
        if (len(self.deck.cards) < 52):
            self.deck.cards = ["Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
                 "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
                 "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
                 "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
                 "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
                 "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
                 "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
                 "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
                 "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds",
                 "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
                 "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
                 "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
                 "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
                 "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
                 "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
                 "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
                 "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
                 "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds",
                 "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
                 "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
                 "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
                 "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
                 "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
                 "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
                 "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
                 "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
                 "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds", 
                 "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
                 "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
                 "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
                 "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
                 "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
                 "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
                 "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
                 "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
                 "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds", 
                 "Ace_of_Hearts", "2_of_Hearts", "3_of_Hearts", "4_of_Hearts", "5_of_Hearts", "6_of_Hearts", 
                 "7_of_Hearts", "8_of_Hearts", "9_of_Hearts", "10_of_Hearts", "Jack_of_Hearts", "Queen_of_Hearts", 
                 "King_of_Hearts", "Ace_of_Clubs", "2_of_Clubs", "3_of_Clubs", "4_of_Clubs", "5_of_Clubs", "6_of_Clubs", 
                 "7_of_Clubs", "8_of_Clubs", "9_of_Clubs", "10_of_Clubs", "Jack_of_Clubs", "Queen_of_Clubs", 
                 "King_of_Clubs", "Ace_of_Spades", "2_of_Spades", "3_of_Spades", "4_of_Spades", "5_of_Spades", 
                 "6_of_Spades", "7_of_Spades", "8_of_Spades", "9_of_Spades", "10_of_Spades", "Jack_of_Spades", 
                 "Queen_of_Spades", "King_of_Spades", "Ace_of_Diamonds", "2_of_Diamonds", "3_of_Diamonds", 
                 "4_of_Diamonds", "5_of_Diamonds", "6_of_Diamonds", "7_of_Diamonds", "8_of_Diamonds", 
                 "9_of_Diamonds", "10_of_Diamonds", "Jack_of_Diamonds", "Queen_of_Diamonds", "King_of_Diamonds"]
        self.dealer = []
        for x in self.players:
            x.cards = []
            x.outcome = ""
            x.done = False
            x.bust = False
            
    
    def setup(self):
        print "Welcome to Blackjack"
        print "Is this a simulated game or real game? (1 = Sim, 2 = Real)"

        choice = self.gameType()

        if choice == 1:
            self.players.append(Player("Player 1"))
            self.players.append(Player("Player 2"))
            self.players.append(Player("Player 3"))
            self.players.append(Player("Player 4"))
            self.players.append(Player("Player 5"))
            self.players.append(Player("Player 6"))
            self.players.append(Player("Player 7"))
        print "Game starts NOW!!"



    def gameType(self):
        choice = raw_input()

        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        else:
            print "That is not a valid input, pleaes enter 1 or 2"
            return gameType(self)

    
    def dealCards(self):
        for x in range(0,2):
            for x in self.players:
                x.cards.append(self.deck.cards.pop(0))
            self.dealer.append(self.deck.cards.pop(0))
            
    def allPlayersDone(self):
        for x in self.players:
            if x.done == False:
                return False
        return True
    
    def hitPlayer(self, player):
        temp = self.deck.cards.pop(0)
        player.cards.append(temp)

    def addCards(self, cards):
        temp = 0
        for x in cards:
            if x[0:1] == "2":
                temp += 2
            elif x[0:1] == "3":
                temp += 3
            elif x[0:1] == "4":
                temp += 4
            elif x[0:1] == "5":
                temp += 5
            elif x[0:1] == "6":
                temp += 6
            elif x[0:1] == "7":
                temp += 7
            elif x[0:1] == "8":
                temp += 8
            elif x[0:1] == "9":
                temp += 9
            elif x[0:1] == "1":
                temp += 10
            elif x[0:1] == "J":
                temp += 10
            elif x[0:1] == "Q":
                temp += 10
            elif x[0:1] == "K":
                temp += 10
            elif x[0:1] == "A":
                if temp+11 > 21:
                    temp += 1
                else:
                    temp += 11
        return temp

    def addCard(self, card):
        if card[0:1] == "2":
            return 2
        elif card[0:1] == "3":
            return 3
        elif card[0:1] == "4":
            return 4
        elif card[0:1] == "5":
            return 5
        elif card[0:1] == "6":
            return 6
        elif card[0:1] == "7":
            return 7
        elif card[0:1] == "8":
            return 8
        elif card[0:1] == "9":
            return 9
        elif card[0:1] == "1":
            return 10
        elif card[0:1] == "J":
            return 10
        elif card[0:1] == "Q":
            return 10
        elif card[0:1] == "K":
            return 10
        elif card[0:1] == "A":
            return 11
        

    def hitOrStay(self, player):
        total = self.addCards(player.cards)
        dealerFirst = self.addCard(self.dealer[0])
        choice = ""
        if total >= 22:
            print player.name, "busted with", total, player.cards
            player.bust = True
            player.done = True
        elif total == 21:
            print player.name, "hits 21!", player.cards
            player.done = True
        else:
            choice = random.choice(["Stay", "Hit"])

        # PLAY LIKE DEALER
        # if player.done == False:
        #     if total > 16:
        #         print player.name, "chose to stay with", total, player.cards
        #         player.done = True
        #     else:
        #         self.hitPlayer(player)

        # PLAY LIKE DEALER + Certain conditions
        if player.done == False:
            if total > 16:
                print player.name, "chose to stay with", total, player.cards
                player.done = True
            elif (dealerFirst < 6 and total > 13):
                print player.name, "chose to stay with", total, player.cards
                player.done = True
            else:
                self.hitPlayer(player)

        # if dealer has 6 or less and if player has 11 or less, hit, otherwise stay. If dealer 
        # has more than 6 showing, random choice. 
        # if player.done == False:
        #     if (dealerFirst < 7):
        #         print "Dealer shows a ", dealerFirst
        #         if (total > 11):
        #             print player.name, "chose to stay with", total, player.cards
        #             player.done = True
        #         else:
        #             self.hitPlayer(player)
        #     elif choice == "Stay":
        #         print player.name, "chose to stay with", total, player.cards
        #         player.done = True
        #     elif choice == "Hit":
        #         self.hitPlayer(player)

        # only take hit if safe to
        # if player.done == False:
        #     if total < 12:
        #         self.hitPlayer(player)
        #     else:
        #         print player.name, "chose to stay with", total, player.cards
        #         player.done = True

        # only take hit if safe to, but on 12's and 13's make a logical
        # choice based on what dealer is showing. 
        # if player.done == False:
        #     if total < 12:
        #         self.hitPlayer(player)
        #     elif (total == 12 or total == 13) and dealerFirst < 7:
        #         if choice == "Stay":
        #             print player.name, "chose to stay with", total, player.cards
        #             player.done = True
        #         elif choice == "Hit":
        #             self.hitPlayer(player)
        #     elif dealerFirst < 7:
        #         print player.name, "chose to stay with", total, player.cards
        #         player.done = True
        #     else:
        #         if choice == "Stay":
        #             print player.name, "chose to stay with", total, player.cards
        #             player.done = True
        #         elif choice == "Hit":
        #             self.hitPlayer(player)

        # random decision to hit or stay 
        # if player.done == False:
        #     if choice == "Stay":
        #         print player.name, "chose to stay with", total, player.cards
        #         player.done = True
        #     elif choice == "Hit":
        #         self.hitPlayer(player)

            
    def dealerPlay(self):
        total = self.addCards(self.dealer)

        if total <= 16:
            self.dealer.append(self.deck.cards.pop(0))
            self.dealerPlay()

    def oneGame(self):
        print "GAMESTART"
        self.deck.shuffle()

        self.dealCards()
        
        while not self.allPlayersDone():
            for x in self.players:
                while x.done == False:
                    self.hitOrStay(x)
        self.dealerPlay()
        dealerTotal = self.addCards(self.dealer)
        
        for x in self.players:
            temp = self.addCards(x.cards)
            if (temp == 21 and len(x.cards) == 2 and dealerTotal != 21):
                x.outcome = "Blackjack"
            elif (dealerTotal > 21) & (temp < 22):
                x.outcome = "Won"
            elif temp > 21:
                x.outcome = "Lost"
            elif temp > dealerTotal:
                x.outcome = "Won"
            elif temp == dealerTotal:
                x.outcome = "Push"
            else:
                x.outcome = "Lost"
        print "Dealer shows", dealerTotal, self.dealer
        for x in self.players:
            temp2 = self.addCards(x.cards)
            print x.name + " has " + x.outcome, "with", temp2
        print "GAMEEND"
        print "\n"
        
class Player:
    name = ""
    cards = []
    done = False
    bust = False
    outcome = ""

    def __init__(self, name):
        self.name = name


test = Game()

counter = 0
won = 0
blackjacks = 0
lost = 0
tied = 0
test.setup()
while counter != 100000:
    test.oneGame()
    for x in test.players:
        if x.outcome == "Blackjack":
            won += 1
            blackjacks += 1
        elif x.outcome == "Won":
            won += 1
        elif x.outcome == "Lost":
            lost += 1
        else:
            tied += 1
    test.reset()
    counter += 1

print counter*len(test.players), "games played"
print "------------------------------------------\n"
print "Won:", won
print "Lost:", lost
print "Tied:", tied
print "Blackjacks:", blackjacks, "out of", counter*len(test.players), "games (", (blackjacks/(counter*len(test.players)+0.0)*100), "% )"
print "Win Percentage:", (won/(won+lost+0.0)*100),"%"
print "Lose Percentage:", (lost/(won+lost+0.0)*100),"%"
print "Tie Percentage:", (tied/(won+lost+tied+0.0)*100),"%"