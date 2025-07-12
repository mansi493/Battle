# import necessary libraries
import random

# player class
class Player:
    """ This class represents a player in the game.
    It includes attributes like name, health, damage, defense,
    and methods for combat, healing items, and special attacks."""
    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.healing_used = False
        self.special_attack = False
        self.xp  = 0
        self.level = 1
          
    def taking_damage(self, ammount):
        """ This method reduces the player's health by the given amount.
        If health goes below or equal to zero, it sets health to zero."""
        self.health -= ammount
        if self.health <= 0:
            self.health = 0
    
    # combat logic 
    def combat(self, player2):
        """ This method handles the combat between two players.
        It includes healing items, special attacks, critical hits, and dodging."""
        turn  = 1
        while self.health>0 and player2.health>0:
            print(f"\n----Round {turn}----\n")
            
            #for player 1 (healing)
            if not self.healing_used:
                use = input(f"{self.name} do you want to use healing item? NOTE: you can use it only once  (y/n): ")
                if use.lower() == 'y':
                    self.healing_items()
                    
            # for player 2 (healing)   
            if not player2.healing_used:
                use2 = input(f"{player2.name} do you want to use healing item? NOTE: you can use it only once  (y/n): ")
                if use2.lower() == 'y':
                    player2.healing_items()
                    
            # critical hit logic for player1
            damage = self.damage
            crit = random.randint(1, 100)
            if crit<=20:
                print(f"Critical Hit by {self.name} ", crit)
                damage *= 2
            
            # critical hit logic for player2
            damage2 = player2.damage
            crit2 = random.randint(1, 100)
            if crit2<=20:
                print(f"Critical Hit by {player2.name} ", crit2)
                damage2 *= 2
                
            # dodge logic for player1
            dodge = random.randint(1, 100)
            if dodge <= 20:
                print(f"{self.name} Dodge the attack!.", dodge)
                damage = 0
                
            # dodge logic for player2
            dodge2 = random.randint(1, 100)
            if dodge2 <= 20:
                print(f"{player2.name} Dodge the attack!.", dodge2)
                damage2 = 0
                
            if self.defense > player2.defense:
                print(f"{self.name} has higher defense value")
                player2.health -= damage
                
            elif player2.defense > self.defense:
                print(f"{player2.name} has higher defense value")
                self.health -= damage2

            else: 
                print("Both have equal defence")
                player2.health -= damage
                self.health -= damage2
            
            # for player1 (special attack)
            if not self.special_attack:
                use1 = input(f"{self.name} want to use special attack? NOTE: you can use it only once (y/n): ")
                if use1.lower() == 'y':
                    self.use_special_attack()
                    
            # for player2 (special attack)
            if not player2.special_attack:
                use2 = input(f"{player2.name} want to use special attack? NOTE: you can use it only once (y/n): ")
                if use2.lower() == 'y':
                    player2.use_special_attack()
            
            print(f"{self.name}'s Health: {self.health} Damage: {self.damage} Defence: {self.defense}")
            print(f"{player2.name}'s Health: {player2.health} Damage: {player2.damage} Defence: {player2.defense}")
            
            turn += 1
    
        if self.health<=0:
            winner = player2.name
            print(f"{player2.name} win the game")
            player2.xp += 10
            while player2.xp >= 100:
                player2.level += 1
                player2.xp -= 100
                player2.damage += 10
                player2.defense += 5
                print(f"{player2.name} leveled up to {player2.level}")
            print(f"{player2.name}'s current xp {player2.xp}")

        elif player2.health<=0:
            winner = self.name
            print(f"{self.name} win the game")
            self.xp += 10
            while self.xp >= 100:
                self.level += 1
                self.xp -= 100
                self.damage += 10
                self.defense += 5
                print(f"{self.name} leveled up to {self.level}")
            print(f"{self.name}'s current xp {self.xp}")
        
        # save the result
        with open("battle_result.txt", 'a') as file:
            file.write(f"Winner is {winner}...\n")
            file.write(f"Total Round is {turn-1}...\n")
            file.write(f"Name: {self.name}, Health: {self.health}, Used Special Attack: {self.special_attack}, Use Heal: {self.healing_used}...\n")
            file.write(f"Name: {player2.name}, Health: {player2.health}, Used Special Attack: {player2.special_attack}, Use Heal: {player2.healing_used}...\n")
    
    # healing items
    def healing_items(self):
        """ This method increases the player's health by a fixed amount.
        It sets healing_used to True to prevent further use of healing items."""
        healing_ammount = 100
        self.health += healing_ammount
        self.healing_used = True
        print(f"{self.name} used healing item")
    
    # special attack
    def use_special_attack(self):
        """ This method increases the player's defense by a fixed amount.
        It sets special_attack to True to prevent further use of special attacks."""
        defense_ammount = 100
        self.defense += defense_ammount
        self.special_attack = True
        print(f"{self.name} used special attack")

# main function
def main():
    """ This function initializes the game and handles rematches.
    It creates two players and starts the combat between them."""
    while True:
        player1 = Player('mansi', 100, 80, 40)
        player2 = Player('jain', 100, 70, 50)
        player1.combat(player2)

        rematch = input("Do you want to rematch? (y/n): ")
        if rematch.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()      