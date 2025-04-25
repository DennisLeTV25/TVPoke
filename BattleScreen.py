from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 150, 40))
        self.backGround = Image((50, 50), 100, 100, "./imgs/Pokemon Background.png")
        self.attacking = False

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
        
    def elementsToDisplay(self):
        self.elements = [Image((50, 50), 100, 100, "./imgs/Pokemon Background.png")]

        if self.attacking == True:
            y = 60
            x = 0
            for trainer in self.trainers:
                for poke in trainer.pokemon:
                    if poke.stats == True:
                            for i in range(len(poke.moves)):
                                MoveButton((x, y), 20, 10, "Attack")
                                x += 20
                                if x > 25:
                                    y = 40

        y = -50
        #two rows of three
        for trainer in self.trainers:
            x = 20
            y += 70
            side = 1
            if self.trainers.index(trainer) != 0:
                x += 80
                side = -1
            for poke in trainer.pokemon:
                if trainer.pokemon.index(poke) == 0:
                    poke.stats = True
                    x += 15 * side
                    self.elements.append(Image((x, y), 30, 30, poke.img))
                    self.elements.append(Label((x, y + (10 * side)), 30, 15, poke.name))
                    self.elements.append(Label((x, y - (13 * side)), 30, 15, str(poke.hp)))
                    x += 10 * side
                    y -= 5 * side
                else:
                    x += 15 * side
                    y -= 3 * side
                    self.elements.append(Image((x, y), 15, 15, poke.img))
                    self.elements.append(Label((x, y + (7 * side)), 11, 5, poke.name))
                    self.elements.append(Label((x, y - (9 * side)), 30, 15, str(poke.hp)))
        
        # self.elements.append(Rectangle((23, 60), 42, 35, (50, 125, 50)))
        x = 20
        y = 20
        for move in self.trainers[0].pokemon[0].moves:
            self.elements.append(AtkButton(x, y, move))
            y += 15

class AtkButton(Button):
    def __init__(self, x, y,move):
        super().__init__((x, y), 20, 10, move.name)
        self.move = move

    def onClick(self, screen):
        screen.trainers[1].pokemon[0].hp -= self.move.power
        screen.trainers.reverse()
        #do a lot more, like check if there are fainted pokemon, check if someone won

class MoveButton(Button):
    def __init__(self, centerXY, width, height, text):
        super().__init__(centerXY, width, height, text)