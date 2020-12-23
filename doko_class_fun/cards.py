import pygame
import random
from .constants import CHOSEN, WIDTH, HEIGHT, BACK, MOVE_STEPS, RESIZE_CARD, PAD_SIDE

class Card:
    def __init__(self, x_pos, y_pos, name, img, player, occlude):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.img = img
        self.player = player
        self.occlude = occlude
        self.chosen = False
        self.chosen_pos = (0,0)
        
    def get_area(self):
        if(self.chosen):
            if(self.occlude == 0):
                return self.x_pos, self.y_pos, self.x_pos + self.img.get_width(), self.y_pos + self.img.get_height(), self.x_pos + self.img.get_width(), self.y_pos + self.img.get_height()
            else:
                return self.x_pos, self.y_pos, self.x_pos + self.occlude, self.y_pos + self.img.get_height(), self.x_pos + self.img.get_width(), self.y_pos + CHOSEN
        else:
            if(self.occlude == 0):
                return self.x_pos, self.y_pos, self.x_pos + self.img.get_width(), self.y_pos + self.img.get_height(), self.x_pos + self.img.get_width(), self.y_pos + self.img.get_height()
            else:
                return self.x_pos, self.y_pos, self.x_pos + self.occlude, self.y_pos + self.img.get_height(), self.x_pos + self.occlude, self.y_pos + self.img.get_height()
    
    def choose(self):
        if(not self.chosen):
            self.y_pos -= CHOSEN
            self.chosen = True
        else:
            self.y_pos += CHOSEN
            self.chosen = False
    
    def draw(self, win):
        if(self.player == 0):
            win.blit(self.img, (self.x_pos,self.y_pos))
        elif(self.player == 1):
            win.blit(pygame.transform.rotate(self.img,90), (self.x_pos,self.y_pos))
        elif(self.player == 2):
            win.blit(self.img, (self.x_pos,self.y_pos))
        else:
            win.blit(pygame.transform.rotate(self.img,-90), (self.x_pos,self.y_pos))
                
    def __repr__(self):
        return self.name
    
    
    
class Trick:
    def __init__(self):
        self.card_trick = []
        self.player_trick = []
        self.img = BACK
        
    def move(self, num, pos_x, pos_y):
        if(num == 0):
            self.card_trick[-1].x_pos += ((WIDTH//2 - self.card_trick[-1].img.get_width()//2) - pos_x)/MOVE_STEPS
            self.card_trick[-1].y_pos += ((HEIGHT//2  - round(self.card_trick[-1].img.get_height()*0.1)) - pos_y)/MOVE_STEPS
        elif(num == 1):
            self.card_trick[-1].x_pos += ((WIDTH//2 - self.card_trick[-1].img.get_width()) - pos_x)/MOVE_STEPS
            self.card_trick[-1].y_pos  = HEIGHT//2 - self.card_trick[-1].img.get_height()//2
        elif(num == 2):
            self.card_trick[-1].x_pos  = WIDTH//2  - self.card_trick[-1].img.get_width()//2
            self.card_trick[-1].y_pos += ((HEIGHT//2  - round(self.card_trick[-1].img.get_height()*0.9)) - pos_y)/MOVE_STEPS
        elif(num == 3):
            self.card_trick[-1].x_pos += (WIDTH//2 - pos_x)/MOVE_STEPS
            self.card_trick[-1].y_pos  = HEIGHT//2 - self.card_trick[-1].img.get_height()//2
    
    def get_trick_color(self, rules):
        for ind, x in enumerate(rules.current_values):
            if(x[rules.cards.index(self.card_trick[0].name)] == 1):
                return ind
           
    def get_highest(self, rules, hand):
        trick_color = self.get_trick_color(rules)
        card_val = [rules.current_values[trick_color][rules.cards.index(x.name)] * rules.current_values[-2][rules.cards.index(x.name)] for x in self.card_trick]
        highest_card_ind = self.check_special_rules(card_val, rules, hand)
        return self.player_trick[highest_card_ind]
        
    def check_special_rules(self, card_val, rules, hand):
        special_point = []
        if(rules.with_catch10 and [True for i in self.card_trick if i.name =='Ten_Hearts'].count(True) == 2 and not (any([True for j in self.card_trick if j.name == 'Ace_Diamonds']) and rules.current_game == 'Normal with Piglets') and not rules.current_game.count('Solo') > 0):
            special_point.append('Catch10')
            highest_card_ind = [ind for ind,x in enumerate(card_val) if x == max(card_val)][1]
        else:
            highest_card_ind = card_val.index(max(card_val))
            
        if(not rules.current_game.count('Solo') > 0 and any([True for ind,j in enumerate(self.card_trick) if j.name == 'Ace_Diamonds' and not ind == card_val.index(max(card_val)) and not (rules.teams[self.player_trick[ind]][0] == rules.teams[self.player_trick[card_val.index(max(card_val))]][0] and rules.teams[self.player_trick[card_val.index(max(card_val))]][1])])):
            if([True for ind,j in enumerate(self.card_trick) if j.name == 'Ace_Diamonds' and not ind == card_val.index(max(card_val)) and not (rules.teams[self.player_trick[ind]][0] == rules.teams[self.player_trick[card_val.index(max(card_val))]][0] and rules.teams[self.player_trick[card_val.index(max(card_val))]][1])].count(True) > 1):
                fox_ind = [ind for ind,i in enumerate(self.card_trick) if i.name == 'Ace_Diamonds' and not ind == card_val.index(max(card_val))]
                hand.stacks[self.player_trick[highest_card_ind]].fox_player.append([self.player_trick[i] for i in fox_ind])
                special_point.append('Fox')
            else:
                hand.stacks[self.player_trick[highest_card_ind]].fox_player.append([self.player_trick[[ind for ind,i in enumerate(self.card_trick) if i.name == 'Ace_Diamonds' and not ind == card_val.index(max(card_val))][0]]])
            special_point.append('Fox')
        else:
            hand.stacks[self.player_trick[highest_card_ind]].fox_player.append([])
        if(sum([rules.points[rules.cards.index(i.name)] for i in self.card_trick]) > 39):
            special_point.append('DoKo')
        if(not rules.current_game.count('Solo') > 0 and len(hand.hands[0]) == 0):
            if(rules.with_karlchen_caught and any([True for ind,j in enumerate(self.card_trick) if j.name == 'Jack_Clubs' and not ind == card_val.index(max(card_val)) and not (rules.teams[self.player_trick[ind]][0] == rules.teams[self.player_trick[card_val.index(max(card_val))]][0] and rules.teams[self.player_trick[card_val.index(max(card_val))]][1])])):
                special_point.append('Karlchen caught')
            elif(rules.with_karlchen_made and any([True for ind,j in enumerate(self.card_trick) if j.name == 'Jack_Clubs' and (ind == card_val.index(max(card_val)) or rules.teams[self.player_trick[ind]][0] == rules.teams[self.player_trick[card_val.index(max(card_val))]][0])])):
                special_point.append('Karlchen made')
            elif(rules.with_foxlast and any([True for ind,j in enumerate(self.card_trick) if j.name == 'Ace_Diamonds' and ind == card_val.index(max(card_val))])):
                special_point.append('Fox last')
        
        self.img = self.prepare_special_point_img(special_point)
            
        hand.stacks[self.player_trick[highest_card_ind]].special_point.append(special_point)
            
        return highest_card_ind  
    
    def prepare_special_point_img(self, special_point):
        if(special_point):
            img = []
            for x in special_point:
                if(x == 'Catch10'):
                    img.append(self.card_trick[[ind for ind,j in enumerate(self.card_trick) if j.name == 'Ten_Hearts'][0]].img.copy())
                elif(x == 'Fox' or x == 'Fox last'):
                    img.append(self.card_trick[[ind for ind,j in enumerate(self.card_trick) if j.name == 'Ace_Diamonds'][0]].img.copy())
                elif(x == 'DoKo'):
                    img.append(self.card_trick[random.choice([ind for ind,j in enumerate(self.card_trick) if not j.name == 'Ace_Diamonds'])].img.copy())
                elif(x == 'Karlchen caught' or x == 'Karlchen made'):
                    img.append(self.card_trick[[ind for ind,j in enumerate(self.card_trick) if j.name == 'Jack_Clubs'][0]].img.copy())
            if(len(special_point) > 0):
                if(len(special_point) > 1):
                    for ind,i in enumerate(img[1:]):
                        for x in range(0, img[0].get_width()):
                            for y in range(15*(ind+1), img[0].get_height()):
                                img[0].set_at((x,y), i.get_at((x,y - 15*(ind+1))))
            return img[0]
        else:
            return BACK
    
    def draw(self, win):
        for x in self.card_trick:
            win.blit(x.img, (x.x_pos, x.y_pos))


        
class Stacks:
    def __init__(self, x_pos, y_pos, player):
        self.player_stack = []
        self.x_pos_end = x_pos
        self.y_pos_end = y_pos
        self.img = []
        self.fox_player = []
        self.special_point = []
        self.player = player
        self.x_pos_stack = []
        self.y_pos_stack = []
        
    def prepare_special_point_img(self, index):
        if(self.special_point[index]):
            img = []
            for x in self.special_point[index]:
                if(x == 'Catch10'):
                    img.append(self.player_stack[index][[ind for ind,j in enumerate(self.player_stack[index]) if j.name == 'Ten_Hearts'][0]].img.copy())
                elif(x == 'Fox' or x == 'Fox last'):
                    img.append(self.player_stack[index][[ind for ind,j in enumerate(self.player_stack[index]) if j.name == 'Ace_Diamonds'][0]].img.copy())
                elif(x == 'DoKo'):
                    img.append(self.player_stack[index][random.choice([ind for ind,j in enumerate(self.player_stack[index]) if not j.name == 'Ace_Diamonds'])].img.copy())
                elif(x == 'Karlchen caught' or x == 'Karlchen made'):
                    img.append(self.player_stack[index][[ind for ind,j in enumerate(self.player_stack[index]) if j.name == 'Jack_Clubs'][0]].img.copy())
            if(len(self.special_point[index]) > 0):
                if(len(self.special_point[index]) > 1):
                    for ind,i in enumerate(img[1:]):
                        for x in range(0, img[0].get_width()):
                            for y in range(15*(ind+1), img[0].get_height()):
                                img[0].set_at((x,y), i.get_at((x,y - 15*(ind+1))))
            self.img[index] = img[0]
        else:
            self.img[index] = BACK
        
    def move(self):
        if(len(self.x_pos_stack) < len(self.player_stack)):
            self.x_pos_stack.append(WIDTH//2 - self.img[-1].get_width()//2)
            self.y_pos_stack.append(HEIGHT//2 - self.img[-1].get_height()//2)
        if(self.player == 0):
            self.x_pos_stack[-1] += ((self.x_pos_end  + (len(self.player_stack)-1)*20) - (WIDTH//2 - self.img[-1].get_width()//2))/MOVE_STEPS
            self.y_pos_stack[-1] += (self.y_pos_end - (HEIGHT//2 - self.img[-1].get_height()//2))/MOVE_STEPS
        elif(self.player == 1):
            self.x_pos_stack[-1] += (self.x_pos_end - (WIDTH//2 - self.img[-1].get_width()//2))/MOVE_STEPS
            self.y_pos_stack[-1] += ((self.y_pos_end + (len(self.player_stack)-1)*20) - (HEIGHT//2 - self.img[-1].get_width()//2))/MOVE_STEPS
        elif(self.player == 2):
            self.x_pos_stack[-1] += ((self.x_pos_end  - (len(self.player_stack)-1)*20) - (WIDTH//2 - self.img[-1].get_width()//2))/MOVE_STEPS
            self.y_pos_stack[-1] += (self.y_pos_end - (HEIGHT//2 - self.img[-1].get_height()//2))/MOVE_STEPS
        else:
            self.x_pos_stack[-1] += (self.x_pos_end - (WIDTH//2 - self.img[-1].get_width()//2))/MOVE_STEPS
            self.y_pos_stack[-1] += ((self.y_pos_end - (len(self.player_stack)-1)*20) - (HEIGHT//2 - self.img[-1].get_width()//2))/MOVE_STEPS
    
    def draw(self, win):
        for ind,_ in enumerate(self.player_stack):
            if(self.player == 0):
                win.blit(self.img[ind], (self.x_pos_stack[ind], self.y_pos_stack[ind]))
            elif(self.player == 1):
                win.blit(pygame.transform.rotate(self.img[ind],90), (self.x_pos_stack[ind], self.y_pos_stack[ind]))
            elif(self.player == 2):
                win.blit(self.img[ind], (self.x_pos_stack[ind], self.y_pos_stack[ind]))
            else:
                win.blit(pygame.transform.rotate(self.img[ind],-90), (self.x_pos_stack[ind], self.y_pos_stack[ind]))
                
    def count(self, rules):
        if(len(self.player_stack) > 0):
            return sum([rules.points[rules.cards.index(j.name)] for i in self.player_stack for j in i])
        else:
            return 0

        
class Poverty_Choice:
    def __init__(self, pov_cards, player):
        self.cards = pov_cards
        self.poor_player = player
        self.img = BACK
        self.x_y_ends = [(WIDTH//2 - RESIZE_CARD[0]//2, HEIGHT - 2.5*RESIZE_CARD[1] - PAD_SIDE), 
                         (1.5*RESIZE_CARD[1] + PAD_SIDE, HEIGHT//2 - RESIZE_CARD[0]//2), 
                         (WIDTH//2 - RESIZE_CARD[0]//2, 1.5*RESIZE_CARD[1] + PAD_SIDE),
                         (WIDTH - 1.5*RESIZE_CARD[0] - RESIZE_CARD[1] - PAD_SIDE, HEIGHT//2 - RESIZE_CARD[1]//2)]
        self.x_pos = self.x_y_ends[player][0]
        self.y_pos = self.x_y_ends[player][1]
        
    def move(self,player):
        self.x_pos += round((self.x_y_ends[(player+1) % 4][0] - self.x_y_ends[player][0])/(MOVE_STEPS+1))
        self.y_pos += round((self.x_y_ends[(player+1) % 4][1] - self.x_y_ends[player][1])/(MOVE_STEPS+1))
        if(abs(self.x_pos - self.x_y_ends[(player+1) % 4][0]) <= abs(round((self.x_y_ends[(player+1) % 4][0] - self.x_y_ends[player][0])/(MOVE_STEPS+1))) and abs(self.y_pos - self.x_y_ends[(player+1) % 4][1]) <= abs(round((self.x_y_ends[(player+1) % 4][1] - self.x_y_ends[player][1])/(MOVE_STEPS+1)))):
            return True
        else:
            return False
                                
    def draw(self, win):
        for ind,_ in enumerate(self.cards):
            win.blit(self.img, (self.x_pos + ind*15, self.y_pos))
        
    def choose_pass(self, win, player):
        stopped = self.move(player)
        self.draw(win)
        if(stopped):
            if(random.randint(0,1)):  #random.randint(0,1)
                return True
            else:
                return False
    
    
    