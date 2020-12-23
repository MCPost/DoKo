
class Rules:
    def __init__(self):
        self.current_order = []
        self.current_values = []
        self.current_game = ''
        self.with_nines = False
        self.with_poverty = False
        self.with_piglets = False
        self.with_catch10 = False
        self.with_karlchen_caught = False
        self.with_karlchen_made = False
        self.with_foxlast = False
        self.with_meatless = False
        self.with_solostarts = True
        self.with_solooverthrow = True
        self.number_poverty = 4
        self.games_possible = ['Queen Solo', 'Jack Solo']
        self.games_order = ['Queen Solo', 'Jack Solo', 'Meatless Solo', 'Poverty', 'Wedding', 'Healthy']
        self.teams = [[],[],[],[]]
        self.call = ['90','60','30','Black']

        self.cards = ["Ace_Clubs","King_Clubs","Queen_Clubs","Jack_Clubs","Ten_Clubs","Nine_Clubs",
                     "Ace_Spades","King_Spades","Queen_Spades","Jack_Spades","Ten_Spades","Nine_Spades",
                     "Ace_Hearts","King_Hearts","Queen_Hearts","Jack_Hearts","Ten_Hearts","Nine_Hearts",
                     "Ace_Diamonds","King_Diamonds","Queen_Diamonds","Jack_Diamonds","Ten_Diamonds","Nine_Diamonds"]
        
        self.points = [11, 4, 3, 2, 10, 1, 11, 4, 3, 2, 10, 1, 11, 4, 3, 2, 10, 1, 11, 4, 3, 2, 10, 1]
        
        self.order_norm = [[0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                           [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                           [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [4, 2, 16, 12, 3, 1, 4, 2, 15, 11, 3, 1, 4, 2, 14, 10, 17, 1, 8, 6, 13, 9, 7, 5],
                           [16, 2, 8, 14, 20, 3, 9, 15, 21, 18, 22, 19, 23, 0, 4, 1, 5, 6, 10, 7, 11, 12, 13, 17]]
        
        self.order_piglets = [[0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                              [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                              [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                              [4, 2, 16, 12, 3, 1, 4, 2, 15, 11, 3, 1, 4, 2, 14, 10, 17, 1, 18, 6, 13, 9, 7, 5],
                              [18, 16, 2, 8, 14, 20, 3, 9, 15, 21, 22, 19, 23, 0, 4, 1, 5, 6, 10, 7, 11, 12, 13, 17]]
        
        self.order_solo_queen = [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                 [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                                 [5, 3, 9, 2, 4, 1, 5, 3, 8, 2, 4, 1, 5, 3, 7, 2, 4, 1, 5, 3, 6, 2, 4, 1],
                                 [2, 8, 14, 20, 0, 4, 1, 3, 5, 6, 10, 7, 9, 11, 12, 16, 13, 15, 17, 18, 22, 19, 21, 23]]
        
        self.order_solo_jack =  [[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                                 [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                                 [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
                                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                                 [5, 3, 2, 9, 4, 1, 5, 3, 2, 8, 4, 1, 5, 3, 2, 7, 4, 1, 5, 3, 2, 6, 4, 1],
                                 [3, 9, 15, 21, 0, 4, 1, 2, 5, 6, 10, 7, 8, 11, 12, 16, 13, 14, 17, 18, 22, 19, 20, 23]]
        
        self.order_solo_meatless =  [[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                                     [6, 4, 3, 2, 5, 1, 6, 4, 3, 2, 5, 1, 6, 4, 3, 2, 5, 1, 6, 4, 3, 2, 5, 1,],
                                     [0, 4, 1, 2, 3, 5, 6, 10, 7, 8, 9, 11, 12, 16, 13, 14, 15, 17, 18, 22, 19, 20, 21, 23]]
        
        
    def determine_teams(self, hand):
        for i in range(4):
            if([True for x in hand.hands[i] if x.name == 'Queen_Clubs'].count(True) > 0):
                if([True for x in hand.hands[i] if x.name == 'Queen_Clubs'].count(True) > 1):
                    self.teams[i] = ['RE', False, 'Wedding', '', 'RE', []]
                else:
                    self.teams[i] = ['RE', False, '', '', 'RE', []]
            else:
                self.teams[i] = ['CONTRA', False,'','', 'CONTRA', []]
            if(self.with_poverty and [True for x in hand.hands[i] if self.current_values[0][self.cards.index(x.name)] == 1].count(True) < self.number_poverty):
                self.teams[i][3] = 'Poverty'
                    
    def teams_update(self, hand, pick, player):
        if(pick):
            if(self.current_game.count('Solo') == 0):
                if(pick):
                    if(pick.name == "Queen_Clubs" and not self.teams[player][1]):
                        self.teams[player][1] = True
                        if([True for i in self.teams if i[0] == 'RE' and i[1]].count(True) > 1):
                            for i in self.teams:
                                if(i[0] == 'CONTRA' and not i[1]):
                                    i[1] = True
                for i in range(4):
                    if(any([x for x in hand.stacks[i].fox_player]) and self.teams[i][1]):
                        for ind,j in enumerate(hand.stacks[i].fox_player):
                            if(j):
                                for h in j:
                                    if(self.teams[h][1] and self.teams[i][0] == self.teams[h][0]):
                                        hand.stacks[i].special_point[ind].remove('Fox')
                                        hand.stacks[i].prepare_special_point_img(ind)
                                        hand.stacks[i].fox_player[ind].remove(h)
        else:
            if(self.current_game.count('Poverty') == 1 and not any([True for i in self.teams if i[3] == 'Rich'])):
                self.teams[player][0] = 'RE'
                self.teams[player][1] = True
                self.teams[player][3] = 'Rich'
                self.teams[player][4] = 'RE'
                for i in range(4):
                    self.teams[i][1] = True
            elif(self.current_game.count('Wedding') == 1 and not any([True for i in self.teams if i[2] == 'Bride']) and (hand.num_cards-len(hand.hands[player])) < 5):
                if((hand.num_cards-len(hand.hands[player])) < 4 and [ind for ind, i in enumerate(self.teams) if i[2] == 'Wedding'][0] != player):
                    self.teams[player][0] = 'RE'
                    self.teams[player][1] = True
                    self.teams[player][2] = 'Bride'
                    self.teams[player][4] = self.teams[[ind for ind, i in enumerate(self.teams) if i[2] == 'Wedding'][0]][4]
                    self.teams[player][5] = self.teams[[ind for ind, i in enumerate(self.teams) if i[2] == 'Wedding'][0]][5]
                    for i in range(4):
                        self.teams[i][1] = True
                elif(hand.num_cards-len(hand.hands[player]) == 4):
                    ind = [ind for ind, i in enumerate(self.teams) if i[2] == '']
                    for i in ind:
                        self.teams[i][1] = True
    
    def determine_game(self, hand, poss_game, turn):
        if(poss_game.count('Healthy') < 4):
            game_ord_ind = [self.games_order.index(x) for x in poss_game]
            if(self.games_order[min(game_ord_ind)] == 'Queen Solo' or self.games_order[min(game_ord_ind)] == 'Jack Solo' or self.games_order[min(game_ord_ind)] == 'Meatless Solo'):
                solo_plyr = (turn + game_ord_ind.index(min(game_ord_ind))) % 4
                if(self.games_order[min(game_ord_ind)] == 'Queen Solo'):
                    self.current_order = [self.cards[i] for i in self.order_solo_queen[-1]]
                    self.current_values = self.order_solo_queen
                    self.current_game = 'Queen Solo' 
                elif(self.games_order[min(game_ord_ind)] == 'Jack Solo'):
                    self.current_order = [self.cards[i] for i in self.order_solo_jack[-1]]
                    self.current_values = self.order_solo_jack
                    self.current_game = 'Jack Solo' 
                elif(self.games_order[min(game_ord_ind)] == 'Meatless Solo'):
                    self.current_order = [self.cards[i] for i in self.order_solo_meatless[-1]]
                    self.current_values = self.order_solo_meatless
                    self.current_game = 'Meatless Solo' 
                hand.sort_cards(self.current_order)
                self.teams[solo_plyr] = ['RE', True, '', '', 'RE', []]
                self.teams[(solo_plyr + 1) % 4] = ['CONTRA', True, '', '', 'CONTRA', []]
                self.teams[(solo_plyr + 2) % 4] = ['CONTRA', True, '', '', 'CONTRA', []]
                self.teams[(solo_plyr + 3) % 4] = ['CONTRA', True, '', '', 'CONTRA', []]
                if(self.with_solostarts):
                    return solo_plyr, False
                else:
                    return turn, False
            elif(self.games_order[min(game_ord_ind)] == 'Poverty'):
                self.teams[(turn + game_ord_ind.index(min(game_ord_ind))) % 4][0] = 'RE'
                self.teams[(turn + game_ord_ind.index(min(game_ord_ind))) % 4][1] = True
                self.teams[(turn + game_ord_ind.index(min(game_ord_ind))) % 4][4] = 'RE'
                if(self.current_game.count('Piglets') > 0):
                    self.current_game = 'Poverty with Piglets'
                else:
                    self.current_game = 'Poverty'
                return turn, True
            else:
                self.teams[(turn + game_ord_ind.index(min(game_ord_ind))) % 4][1] = True
                if(self.current_game.count('Piglets') > 0):
                    self.current_game = 'Wedding with Piglets'
                else:
                    self.current_game = 'Wedding'
                return turn, False
        else:
            return turn, False
        
    def call_update(self, player):
        for i in range(4):
            if(i != player and self.teams[i][0] == self.teams[player][0]):
                self.teams[i][4] = self.teams[player][4]
                self.teams[i][5] = self.teams[player][5]
            
    def piglets(self, win, buttons, pick, player):
        if(pick):
            if(self.with_piglets and self.current_game.count('Piglets') > 0 and pick.name == 'Ace_Diamonds'):
                buttons.draw_game(win, ['Piglets!!!'], player)
                
    def determine_game_points(self, hand, print_to_console = False):
        player_card_points = [x.count(self) for x in hand.stacks]
        RE_player = ' | '.join([f'Player {ind}: {player_card_points[ind]} card points' for ind,x in enumerate(self.teams) if x[0] == 'RE'])
        RE_call = [x[5] for x in self.teams if x[0] == 'RE' and x[5]]
        CONTRA_player = ' | '.join([f'Player {ind}: {player_card_points[ind]} card points' for ind,x in enumerate(self.teams) if x[0] == 'CONTRA'])
        CONTRA_call = [x[5] for x in self.teams if x[0] == 'CONTRA' and x[5]]
        RE_CONTRA_card_points = [sum([player_card_points[ind] for ind,x in enumerate(self.teams) if x[0] == 'RE']), sum([player_card_points[ind] for ind,x in enumerate(self.teams) if x[0] == 'CONTRA'])]
        
        winning_threshold = 120
        if(RE_call):
            RE_call = RE_call[0]
            if(RE_call[1]):
                if(RE_call[1] == '90' or RE_call[1] == '60' or RE_call[1] == '30'):
                    winning_threshold = 240 - int(RE_call[1])
                else:
                    winning_threshold = 239
        if(CONTRA_call):
            CONTRA_call = CONTRA_call[0]
            if(CONTRA_call[1]):
                if(CONTRA_call[1] == '90' or CONTRA_call[1] == '60' or CONTRA_call[1] == '30'):
                    winning_threshold = int(CONTRA_call[1])
                else:
                    winning_threshold = 0
        
        # GAME POINTS
        if(RE_CONTRA_card_points[0] > winning_threshold):
            Winning = ['RE','120 (+1)']
            special_point_sign = ['+','-']
            game_point_sign = [1,-1]
        else:
            Winning = ['CONTRA','CONTRA (+1)','120 (+1)']
            special_point_sign = ['-','+']
            game_point_sign = [-1,1]
            
        if(min(RE_CONTRA_card_points) < 90):
            Winning.append('<90 (+1)')
            if(winning_threshold < 91 or winning_threshold > 149):
                Winning.append('called < 90 (+1)')
        if(min(RE_CONTRA_card_points) < 60):
            Winning.append('<60 (+1)')
            if(winning_threshold < 61 or winning_threshold > 179):
                Winning.append('called < 60 (+1)')
        if(min(RE_CONTRA_card_points) < 30):
            Winning.append('<30 (+1)')
            if(winning_threshold < 31 or winning_threshold > 209):
                Winning.append('called < 30 (+1)')
        if(min(RE_CONTRA_card_points) == 0):
            Winning.append('Black (+1)')
            if(winning_threshold < 1 or winning_threshold > 238):
                Winning.append('called Black (+1)')
                
        # SPECIAL POINTS
        RE_special_points = []
        CONTRA_special_points = []
        for i in range(4):
            for j in hand.stacks[i].special_point:
                if(j):
                    for h in j:
                        if(self.teams[i][0] == 'RE'):
                            RE_special_points.append(h + f' ({special_point_sign[0]}1)')
                        else:
                            CONTRA_special_points.append(h + f' ({special_point_sign[1]}1)')
        
        if(Winning[0] == 'RE'):                    
            Game_points = len(Winning[1:]) + len(RE_special_points) - len(CONTRA_special_points)
        else:
            Game_points = len(Winning[1:]) - len(RE_special_points) + len(CONTRA_special_points)
        
        Call_Factor = []
        if(RE_call):
            Game_points *= 2
            Call_Factor.append('RE (x2)')
        if(CONTRA_call):
            Game_points *= 2
            Call_Factor.append('CONTRA (x2)')
        
        Player_Game_points = [0,0,0,0]
        for i in range(4):
            if(self.teams[i][0] == 'RE'):
                Player_Game_points[i] = Game_points*game_point_sign[0]
            else:
                Player_Game_points[i] = Game_points*game_point_sign[1]
        
        cur_game_str = (f'{Winning[0]} wins this {self.current_game}\n'
                        f'RE points: {RE_CONTRA_card_points[0]}   ({RE_player})   Called: {" ".join(RE_call)}\n'
                        f'CONTRA points: {RE_CONTRA_card_points[1]}    ({CONTRA_player})   Called: {" ".join(CONTRA_call)}\n'
                        f'Game points: {" + ".join(Winning[1:])} | Special points: {" + ".join(RE_special_points)} + {" + ".join(CONTRA_special_points)} | {" x ".join(Call_Factor)}\n\n')
        #                f'Player 0: {Player_Game_points[0]}  |  Player 1: {Player_Game_points[1]}  |  Player 2: {Player_Game_points[2]}  |  Player 3: {Player_Game_points[3]}\n\n')
        if(print_to_console):        
            print(cur_game_str) 
                        
        return Player_Game_points, cur_game_str
 
 
        