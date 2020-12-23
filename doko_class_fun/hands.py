import random
from .constants import CARDS, BACK, WIDTH, HEIGHT, RESIZE_CARD, PAD_CARDOVERLAP, PAD_SIDE, PAD_STACK
from .cards import Card, Trick, Stacks

class Hands:
    def __init__(self, set_cards):
        self.set = set_cards
        self.hands = []
        self.tricks = Trick()
        self.stacks = [[],[],[],[]]
        self.num_cards = len(self.set)//4
    
    def shuffle_deal_cards(self):
        Set = self.set[:]
        random.shuffle(Set)
        #print(Set)
        #Set = ['Ace_Diamonds']*24
        #Set.append('Queen_Clubs')
        #Set.extend(['Ten_Hearts']*24)
        #Set.append('Queen_Clubs')
        #Set = ['King_Diamonds', 'Queen_Spades', 'King_Hearts', 'Ace_Clubs', 'Queen_Hearts', 'Ten_Spades', 'Queen_Diamonds', 'Jack_Spades', 'Ace_Diamonds', 'Nine_Spades', 'Ten_Diamonds', 'Jack_Clubs', 
        #       'King_Spades', 'King_Clubs', 'Nine_Diamonds', 'Ten_Diamonds', 'King_Diamonds', 'Queen_Clubs', 'Nine_Spades', 'Queen_Spades', 'Jack_Spades', 'Ten_Clubs', 'Ace_Clubs', 'Nine_Clubs', 
        #       'King_Clubs', 'Ace_Hearts', 'Ace_Hearts', 'Nine_Hearts', 'Ace_Diamonds', 'Jack_Diamonds', 'Queen_Clubs', 'Nine_Clubs', 'King_Spades', 'King_Hearts', 'Jack_Clubs', 'Ten_Clubs', 
        #       'Nine_Hearts', 'Jack_Diamonds', 'Ten_Spades', 'Queen_Hearts', 'Jack_Hearts', 'Ace_Spades', 'Ten_Hearts', 'Jack_Hearts', 'Ace_Spades', 'Ten_Hearts', 'Queen_Diamonds', 'Nine_Diamonds']
        #Set = ['Ace_Clubs','King_Clubs','Queen_Clubs','Queen_Spades','King_Spades','Jack_Spades','Nine_Hearts','Ace_Hearts','Ten_Clubs','Nine_Clubs','Nine_Hearts','Ace_Spades',
        #       'Ten_Spades','Nine_Spades','King_Hearts','King_Diamonds','Queen_Diamonds','Ace_Diamonds','Jack_Diamonds','King_Spades','King_Clubs','Ace_Clubs','Ten_Diamonds','King_Diamonds',
        #       'Jack_Clubs','Ten_Clubs','Nine_Clubs','Ace_Spades','Queen_Hearts','Jack_Hearts','Ten_Hearts','Ace_Diamonds','Nine_Diamonds','Jack_Clubs','Ten_Spades','Queen_Hearts',
        #       'Jack_Diamonds','Queen_Clubs','Queen_Spades','Jack_Spades','Nine_Spades','Ace_Hearts','King_Hearts','Jack_Hearts','Ten_Hearts','Queen_Diamonds','Ten_Diamonds','Nine_Diamonds']
        self.hands = ([Set[i:i + self.num_cards] for i in range(0, len(Set), self.num_cards)])
        
    def sort_cards(self, order):
        for i in range(4):
            self.hands[i] = sorted(self.hands[i], key = lambda x: order.index(x.name))
            self.recalculate_pos(i)
    
    def create_cards(self):      
        for i in range(4):
            for ind,x in enumerate(self.hands[i]):
                if(i == 0):
                    pos_x = WIDTH//2 - (RESIZE_CARD[0] + len(self.hands[i])*PAD_CARDOVERLAP[0])//2 + PAD_CARDOVERLAP[0]*ind
                    pos_y = HEIGHT - RESIZE_CARD[1] - PAD_SIDE
                    self.hands[i][ind] = Card(pos_x, pos_y, x, CARDS[x], 0, (ind != len(self.hands[i])-1)*PAD_CARDOVERLAP[0])
                    if(ind == len(self.hands[i])-1):
                        pos_x = pos_x + PAD_STACK[0]
                        self.stacks[i] = Stacks(pos_x, pos_y, 0)
                elif(i == 1):
                    pos_x = PAD_SIDE
                    pos_y = HEIGHT//2 - (RESIZE_CARD[0] - len(self.hands[i])*PAD_CARDOVERLAP[1])//2 - PAD_CARDOVERLAP[1]*ind
                    self.hands[i][ind] = Card(pos_x, pos_y, x, BACK, 1, (ind != len(self.hands[i])-1)*PAD_CARDOVERLAP[1])
                    if(ind == 0):
                        pos_y = pos_y + PAD_STACK[1]
                        self.stacks[i] = Stacks(pos_x, pos_y, 1)
                elif(i == 2):
                    pos_x = WIDTH//2 - (RESIZE_CARD[0] + len(self.hands[i])*PAD_CARDOVERLAP[0])//2 + PAD_CARDOVERLAP[0]*ind
                    pos_y = PAD_SIDE
                    self.hands[i][ind] = Card(pos_x, pos_y, x, BACK, 2, (ind != len(self.hands[i])-1)*PAD_CARDOVERLAP[0])
                    if(ind == 0):
                        pos_x = pos_x - PAD_STACK[2]
                        self.stacks[i] = Stacks(pos_x, pos_y, 2)
                else:
                    pos_x = WIDTH - RESIZE_CARD[1] - PAD_SIDE
                    pos_y = HEIGHT//2 - (RESIZE_CARD[0] + len(self.hands[i])*PAD_CARDOVERLAP[1])//2 + PAD_CARDOVERLAP[1]*ind
                    self.hands[i][ind] = Card(pos_x, pos_y, x, BACK, 3, (ind != len(self.hands[i])-1)*PAD_CARDOVERLAP[1])
                    if(ind == 0):
                        pos_y = pos_y - PAD_STACK[3]
                        self.stacks[i] = Stacks(pos_x, pos_y, 3)
                        
    def check_throw(self, rules):
        check_throw = [0,0,0,0]
        for i in range(4):
            if(((self.hands[i][0].name == 'Ace_Diamonds' or self.hands[i][0].name == 'Ten_Diamonds' or self.hands[i][0].name == 'King_Diamonds' or self.hands[i][0].name == 'Nine_Diamonds') and not rules.current_game.count('Piglets')) or [x.name for x in self.hands[i]].count('King') > 4):
                check_throw[i] = 1
        return check_throw
                            
    def recalculate_pos(self, player):
        for ind,_ in enumerate(self.hands[player]):
            if(player == 0):
                self.hands[0][ind].x_pos = WIDTH//2 - (RESIZE_CARD[0] + len(self.hands[0])*PAD_CARDOVERLAP[0])//2 + PAD_CARDOVERLAP[0]*ind
                self.hands[0][ind].y_pos = HEIGHT - RESIZE_CARD[1] - PAD_SIDE
                self.hands[0][ind].occlude = (ind != len(self.hands[0])-1)*PAD_CARDOVERLAP[1]
            elif(player == 1):
                self.hands[1][ind].x_pos = 0 + PAD_SIDE
                self.hands[1][ind].y_pos = HEIGHT//2 - (RESIZE_CARD[0] - len(self.hands[1])*PAD_CARDOVERLAP[1])//2 - PAD_CARDOVERLAP[1]*ind
            elif(player == 2):
                self.hands[2][ind].x_pos = WIDTH//2 - (RESIZE_CARD[0] + len(self.hands[2])*PAD_CARDOVERLAP[0])//2 + PAD_CARDOVERLAP[0]*ind
                self.hands[2][ind].y_pos = 0 + PAD_SIDE
            else:
                self.hands[3][ind].x_pos = WIDTH - RESIZE_CARD[1] - PAD_SIDE
                self.hands[3][ind].y_pos = HEIGHT//2 - (RESIZE_CARD[0] + len(self.hands[3])*PAD_CARDOVERLAP[1])//2 + PAD_CARDOVERLAP[1]*ind
                 
    def draw_cards(self, win):
        for i in range(4):
            for ind,_ in enumerate(self.hands[i]):
                self.hands[i][ind].draw(win)
            if(len(self.stacks[i].player_stack) > 0):
                self.stacks[i].draw(win)
        self.tricks.draw(win)
        
    def choose_play_card(self, pos):
        for ind1,x in enumerate(self.hands[0]):
            bound1 = (x.get_area()[0] < pos[0] and x.get_area()[2] > pos[0] and x.get_area()[1] < pos[1] and x.get_area()[3] > pos[1])
            bound2 = (x.get_area()[0] < pos[0] and x.get_area()[4] > pos[0] and x.get_area()[1] < pos[1] and x.get_area()[5] > pos[1])
            if((bound1 or bound2) and not x.chosen):
                x.choose()
                for ind2,y in enumerate(self.hands[0]):
                    if(ind1 != ind2 and y.chosen):
                        y.choose()
            elif((bound1 or bound2) and x.chosen):
                return True, x, x.x_pos, x.y_pos
        return False, [], [], []
    
    def enemy_call(self, rules, player, call_border):
        if(round(random.random()*.52) and sum([self.num_cards - len(x) for x in self.hands]) <= call_border):
            if(rules.teams[player][4] == 'RE' or rules.teams[player][4] == 'CONTRA'):
                rules.teams[player][5] = [rules.teams[player][4],'']
                rules.teams[player][4] = rules.call[0]
                rules.teams[player][1] = True
            elif(rules.call[rules.call.index(rules.teams[player][4])+1] != 'Black'):
                rules.teams[player][5][1] = rules.teams[player][4]
                rules.teams[player][4] = rules.call[rules.call.index(rules.teams[player][4])+1]
            else:
                rules.teams[player][5][1] = rules.teams[player][4]
            return call_border + 4
        else:
            return call_border
                
    def enemy_pick(self, player, rules):
        if(self.tricks.card_trick):
            indexes1 = []
            indexes2 = []
            trick_color = self.tricks.get_trick_color(rules)
            for ind1,x in enumerate(self.hands[player]):
                for ind2,i in enumerate(rules.current_values):
                    if(i[rules.cards.index(x.name)] == 1 and ind2 == trick_color):
                        if(ind2 > 0 and rules.current_values[ind2-1][rules.cards.index(x.name)] == 0):
                            indexes1.append(ind1)
                        else:
                            indexes2.append(ind1)
                        break
                    elif(ind2 > trick_color):
                        break
            if(indexes1 or indexes2):
                if(indexes1):   
                    ind = random.choice(indexes1)
                    pick = self.hands[player][ind]
                else:
                    ind = random.choice(indexes2)
                    pick = self.hands[player][ind]
            else:
                pick = random.choice(self.hands[player])
        else:
            pick = random.choice(self.hands[player])
        pick.img = CARDS[pick.name]
        return pick, pick.x_pos, pick.y_pos
    
    def enemy_tactic(self, rules, player):
        if(rules.teams[player][3] == 'Poverty'):
            pick = 'Poverty'
        elif(rules.teams[player][2] == 'Wedding'):
            pick = 'Wedding'
        else:
            if(round(random.random()*.52)):
                pick = random.choice(rules.games_possible)
            else:
                pick = 'Healthy'
        return pick
    
    def choose_pov_card(self, pos, poverty_choice):
        for x in self.hands[0]:
            bound1 = (x.get_area()[0] < pos[0] and x.get_area()[2] > pos[0] and x.get_area()[1] < pos[1] and x.get_area()[3] > pos[1])
            bound2 = (x.get_area()[0] < pos[0] and x.get_area()[4] > pos[0] and x.get_area()[1] < pos[1] and x.get_area()[5] > pos[1])
            if((bound1 or bound2) and not x.chosen and [True for y in self.hands[0] if y.chosen].count(True) < len(poverty_choice.cards) and not (x.chosen_pos[0] == pos[0] and x.chosen_pos[1] == pos[1])):
                x.choose()
                x.chosen_pos = pos                              
            if((bound1 or bound2) and x.chosen and not (x.chosen_pos[0] == pos[0] and x.chosen_pos[1] == pos[1])):
                x.choose()
                x.chosen_pos = pos  

    def poverty_switch(self, rules, player_count, poverty_choice):
        poor_player = [ind for ind,x in enumerate(rules.teams) if x[3] == 'Poverty'][0]
        rich_player = (poor_player + player_count) % 4
        for x in poverty_choice.cards:
            if(rich_player == 0):
                x.img = CARDS[x.name]
            else:
                x.img = BACK
            x.player = rich_player
        self.hands[rich_player].extend(poverty_choice.cards)
        poss_fail_back = [x for x in self.hands[rich_player] if rules.current_values[0][rules.cards.index(x.name)] == 0]
        card_back = []
        if(len(poss_fail_back) == len(poverty_choice.cards)):
            card_back = poss_fail_back
        elif(len(poss_fail_back) > len(poverty_choice.cards)):
            card_back = random.sample(poss_fail_back,len(poverty_choice.cards))
        else:
            poss_trump_back = [x for x in self.hands[rich_player] if rules.current_values[0][rules.cards.index(x.name)] == 1]
            poss_fail_back.extend(random.sample(poss_trump_back, len(poverty_choice.cards) - len(poss_fail_back)))
            card_back = poss_fail_back
        for x in card_back:
            if(poor_player == 0):
                x.img = CARDS[x.name]
            else:
                x.img = BACK
            x.player = poor_player
        self.hands[poor_player].extend(card_back)
        for x in card_back:
            self.hands[rich_player].remove(x)
        self.sort_cards(rules.current_order)
        self.recalculate_pos(poor_player)
        rules.current_game = 'Poverty'
            
            
        
        