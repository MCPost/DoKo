import pygame
import pygame_menu
import random
from doko_class_fun.constants import WIDTH, HEIGHT, CARDS, MOVE_STEPS, BUTTON_COLOR, GREEN, BUTTON_POSITION, BACK
from doko_class_fun.hands import Hands
from doko_class_fun.cards import Poverty_Choice
from doko_class_fun.rules import Rules
from doko_class_fun.buttons import Buttons

FPS = 60

diagnostic_mode = True

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Doppelkopf')
pygame.init()

surface_menu = pygame.display.set_mode((WIDTH, HEIGHT))
def start_the_game():
    pygame_menu.Menu.disable(menu)
  
menu = pygame_menu.Menu(600, 600, 'Welcome to Doppelkopf',theme=pygame_menu.themes.THEME_BLUE)
menu.add_selector('Nines: ', [('No',),('Yes',)], selector_id='Nines')
menu.add_selector('Poverty: ', [('No',),('Yes',)], selector_id='Poverty')
menu.add_selector('Piglets: ', [('No',),('Yes',)], selector_id='Piglets')
menu.add_selector('Catch10: ', [('No',),('Yes',)], selector_id='Catch10')
menu.add_selector('Karlchen Caught: ', [('No',),('Yes',)], selector_id='Karlchen Caught')
menu.add_selector('Karlchen Made: ', [('No',),('Yes',)], selector_id='Karlchen Made')
menu.add_selector('Fox Last: ', [('No',),('Yes',)], selector_id='Foxlast')
menu.add_selector('Meatless: ', [('No',),('Yes',)], selector_id='Meatless')
menu.add_button('Play', start_the_game)

def main():
    clock = pygame.time.Clock()
    
    quit_game = False
    
    rules = Rules()
    buttons = Buttons()
    Player_Game_points = [[0,0,0,0]]

    menu.mainloop(surface_menu)
    rules.with_nines = menu.get_input_data()['Nines'][1]
    rules.with_poverty = menu.get_input_data()['Poverty'][1]
    rules.with_piglets = menu.get_input_data()['Piglets'][1]
    rules.with_catch10 = menu.get_input_data()['Catch10'][1]
    rules.with_karlchen_caught = menu.get_input_data()['Karlchen Caught'][1]
    rules.with_karlchen_made = menu.get_input_data()['Karlchen Made'][1]
    rules.with_foxlast = menu.get_input_data()['Foxlast'][1]
    rules.with_meatless = menu.get_input_data()['Meatless'][1]
    if(rules.with_meatless):
        rules.games_possible.append('Meatless Solo')
    
    
    set_cards = list(CARDS.keys())*2
    if(not rules.with_nines):
        for s in set_cards:
            if "Nine" in s:
                set_cards.remove(s)
    
    ## New Game
    game_run = True
    while game_run:
        
        hand = Hands(set_cards)
        hand.shuffle_deal_cards()
        hand.create_cards()
        
        if(rules.with_piglets and [True for x in hand.hands if str(x).count('Ace_Diamonds') > 1]):
            rules.current_order = [rules.cards[i] for i in rules.order_piglets[-1]]
            rules.current_values = rules.order_piglets
            rules.current_game = 'Normal Game with Piglets'
        else:
            rules.current_order = [rules.cards[i] for i in rules.order_norm[-1]]
            rules.current_values = rules.order_norm
            rules.current_game = 'Normal Game'
        
        throw_possible = hand.check_throw(rules)
        
        if(diagnostic_mode):
            print(rules.current_game)
        
        hand.sort_cards(rules.current_order)
        rules.determine_teams(hand)
        turn = random.randint(0,3)
        if(diagnostic_mode):
            print(rules.teams)
        run = determine = pov_enemy_choice = True
        pressed_throw = pressed_wed = pressed_pov = pressed_QS = pressed_JS = pressed_MS = pressed_H = player_take = taken = pressed_back = False
        pos = (0,0)
        player_count = move_count = wait_count = call_count = next_turn = 0
        poss_game = []
        while run:
            clock.tick(FPS)
            
            WIN.fill(GREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game_run = False
                    quit_game = True
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    
            if((turn + next_turn) % 4 > 0 and next_turn < 4):
                if(wait_count == 0):
                    if(throw_possible[(turn + next_turn) % 4]):
                        poss_game.append('Throw')
                    else:
                        poss_game.append(hand.enemy_tactic(rules, (turn + next_turn) % 4))
                    wait_count += 1
                elif(0 < wait_count < round(FPS*0.5)):
                    wait_count += 1
                else:
                    wait_count = 0
                    next_turn += 1
            
            if((turn + next_turn) % 4 == 0 and next_turn < 4):
                ## Add buttons
                if(throw_possible[0]):
                    pressed_throw = buttons.draw(WIN, pos, BUTTON_POSITION['THROW'], BUTTON_COLOR['THROW'], 'THROW')
                if(rules.teams[0][3] == 'Poverty' and not pressed_pov):
                    pressed_pov = buttons.draw(WIN, pos, BUTTON_POSITION['POVERTY'], BUTTON_COLOR['WED_POV'], 'POVERTY')           
                if(rules.teams[0][2] == 'Wedding'):
                    pressed_wed = buttons.draw(WIN, pos, BUTTON_POSITION['WEDDING'], BUTTON_COLOR['WED_POV'], 'WEDDING')          
                pressed_QS = buttons.draw(WIN, pos, BUTTON_POSITION['QUEEN_SOLO'], BUTTON_COLOR['SOLO'], 'QUEEN SOLO')
                pressed_JS = buttons.draw(WIN, pos, BUTTON_POSITION['JACK_SOLO'], BUTTON_COLOR['SOLO'], 'JACK SOLO')
                if(rules.with_meatless):
                    pressed_MS = buttons.draw(WIN, pos, BUTTON_POSITION['MEATLESS_SOLO'], BUTTON_COLOR['SOLO'], 'MEATLESS SOLO')
                else:
                    pressed_MS = False
                pressed_H = buttons.draw(WIN, pos, BUTTON_POSITION['HEALTHY'], BUTTON_COLOR['HEALTHY'], 'HEALTHY')
                if(pressed_throw or pressed_pov or pressed_wed or pressed_QS or pressed_JS or pressed_MS or pressed_H):
                    if(pressed_throw):
                        poss_game.append('Throw')
                    if(pressed_pov):
                        poss_game.append('Poverty')
                    if(pressed_wed):
                        poss_game.append('Wedding')
                    if(pressed_QS):
                        poss_game.append('Queen Solo')
                    if(pressed_JS):
                        poss_game.append('Jack Solo')
                    if(pressed_MS):
                        poss_game.append('Meatless Solo')
                    if(pressed_H):
                        poss_game.append('Healthy')
                    next_turn += 1
            
            if(next_turn > 3):
                if determine:
                    if(poss_game.count('Throw') > 0 and rules.with_solooverthrow and not poss_game.count('Solo') > 0):
                        pov = False
                        run = False
                        quit_game = True
                    else:
                        turn, pov = rules.determine_game(hand, poss_game, turn)
                    determine = False
                if(pov):
                    for x in rules.teams:
                        x[0] = x[4] = 'CONTRA'
                    poor_player = [ind for ind,x in enumerate(rules.teams) if x[3] == 'Poverty'][0]
                    rules.teams[poor_player][0] = rules.teams[poor_player][4] = 'RE'
                    if(len(hand.hands[poor_player]) == hand.num_cards):
                        pov_cards = [x for x in hand.hands[poor_player] if rules.current_values[0][rules.cards.index(x.name)] == 1]
                        for x in pov_cards:
                            hand.hands[poor_player].remove(x)
                        poverty_choice = Poverty_Choice(pov_cards, poor_player)
                        hand.recalculate_pos(poor_player)
    
                    if((poor_player + player_count) % 4 == 0 and wait_count == 0 and move_count == 0 and poor_player != 0):
                        if(player_take):
                            hand.choose_pov_card(pos, poverty_choice)
                            if([True for x in hand.hands[0] if x.chosen].count(True) > len(poverty_choice.cards)-1):
                                pressed_back = buttons.draw(WIN, pos, BUTTON_POSITION['BACK_POVERTY'], BUTTON_COLOR['POSSIBLE_GAME'], 'Give Back')
                            if(pressed_back):
                                card_back = [x for x in hand.hands[0] if x.chosen]
                                for x in card_back:
                                    x.img = BACK
                                    x.player = poor_player
                                hand.hands[poor_player].extend(card_back)
                                for x in card_back:
                                    hand.hands[0].remove(x)
                                hand.sort_cards(rules.current_order)
                                hand.recalculate_pos(poor_player)
                                rules.teams_update(hand,[],0)
                                rules.current_game = 'Poverty'
                                run = False
                        else:
                            pov_enemy_choice = False
                            poverty_choice.draw(WIN)
                            pressed_take = buttons.draw(WIN, pos, BUTTON_POSITION['TAKE_POVERTY'], BUTTON_COLOR['POSSIBLE_GAME'], 'Take it')
                            pressed_pass = buttons.draw(WIN, pos, BUTTON_POSITION['PASS_POVERTY'], BUTTON_COLOR['POSSIBLE_GAME'], 'Pass')
                            if(pressed_take):
                                for x in poverty_choice.cards:
                                    x.img = CARDS[x.name]
                                    x.player = 0
                                hand.hands[0].extend(poverty_choice.cards)
                                hand.sort_cards(rules.current_order)
                                hand.recalculate_pos(poor_player)
                                player_take = True
                            if(pressed_pass):
                                pov_enemy_choice = True
                        hand.draw_cards(WIN)
                        pygame.display.update()
                    
                    if(pov_enemy_choice):
                        if(move_count == MOVE_STEPS):
                            if(wait_count < round(FPS*0.3)):
                                wait_count += 1
                            else:
                                taken = poverty_choice.choose_pass(WIN, (poor_player+player_count) % 4)
                                player_count += 1
                                move_count = 0
                                wait_count = 0
                        else:
                            if(wait_count == 0):
                                poverty_choice.choose_pass(WIN, (poor_player+player_count) % 4)
                                hand.draw_cards(WIN)
                                pygame.display.update()
                                wait_count += 1
                            elif(0 < wait_count < round(FPS*0.01)):
                                wait_count += 1
                            else:
                                wait_count = 0
                                move_count += 1
                                          
                    if(taken or player_count > 3):
                        if(taken):
                            hand.poverty_switch(rules, player_count, poverty_choice)
                            rules.teams_update(hand,[],(poor_player+player_count) % 4)
                            taken = run = False
                            next_turn += 1
                        else: 
                            run = False
                            quit_game = True
                else:
                    run = False
                continue
                    
            hand.draw_cards(WIN)
            buttons.draw_game(WIN, poss_game, turn)
            pygame.display.update() 
            
            # Pause to look at Points   
     
        if(quit_game):
            run = False
            quit_game = False
        else:
            run = True
        
        if(diagnostic_mode):
            print('before:',rules.teams)
        
        if(rules.current_game.count('Wedding') > 0):
            call_border = 17
        else:
            call_border = 5
        wait_count = move_count = game_count = 0
        played = trick_end = end_game = False
        next_turn = True
        pos = (0,0)
        player_pick = []
        enemy_pick = []
        while run:
            clock.tick(FPS)
            
            WIN.fill(GREEN)
            
            ## Add buttons
            if(sum([hand.num_cards - len(x) for x in hand.hands]) <= call_border):
                press_call = buttons.draw(WIN, pos, BUTTON_POSITION['RE_CONTRA'], BUTTON_COLOR['CALL'][call_count], rules.teams[0][4])
                if(press_call):
                    if(press_call and rules.teams[0][4] == 'RE' or rules.teams[0][4] == 'CONTRA'):
                        rules.teams[0][5] = [rules.teams[0][4],'']
                        rules.teams[0][4] = rules.call[0]
                        rules.teams[0][1] = True
                    elif(press_call and rules.call[rules.call.index(rules.teams[0][4])+1] != 'Black'):
                        rules.teams[0][5][1] = rules.teams[0][4]
                        rules.teams[0][4] = rules.call[rules.call.index(rules.teams[0][4])+1]
                    elif(press_call and rules.teams[0][4] is 'Black'):
                        rules.teams[0][5][1] = 'Black'
                        call_border += 4
                    pos = (0,0)
                    rules.teams[0][1] = True
                    call_count += 1
                    call_border += 4
                    rules.call_update(0)
                    rules.teams_update(hand, [], 0)
            
            if(end_game):
                cur_Game_points, cur_game_str = rules.determine_game_points(hand)
                Player_Game_points.append([x+y for x,y in zip(Player_Game_points[-1], cur_Game_points)])
                buttons.end_screen(WIN, Player_Game_points, cur_game_str)
                pygame.display.update()
                #run = False
            else:
                buttons.draw_called(WIN, rules)
                hand.draw_cards(WIN)
                rules.piglets(WIN, buttons, player_pick, turn)
                rules.piglets(WIN, buttons, enemy_pick, turn)
                pygame.display.update()
            
            if(turn > 0 and next_turn):
                if(move_count == 0 and wait_count == 0):
                    call_border = hand.enemy_call(rules, turn, call_border)
                    rules.call_update(turn)
                    enemy_pick, enemy_pos_x, enemy_pos_y = hand.enemy_pick(turn, rules)
                    rules.teams_update(hand, enemy_pick, turn)
                    hand.tricks.card_trick.append(enemy_pick)
                    hand.tricks.player_trick.append(turn)
                    hand.hands[turn].remove(enemy_pick)
                    hand.recalculate_pos(turn)
                
                if(move_count == MOVE_STEPS):
                    if(wait_count < round(FPS*0.3)):
                        wait_count += 1
                    else:
                        turn = (turn+1) % 4
                        move_count = 0
                        if(len(hand.tricks.player_trick) == 4):
                            trick_end = True
                        wait_count = 0
                else:
                    if(wait_count == 0):
                        hand.tricks.move(turn, enemy_pos_x, enemy_pos_y)
                        hand.draw_cards(WIN)
                        wait_count += 1
                    elif(0 < wait_count < round(FPS*0.01)):
                        wait_count += 1
                    else:
                        wait_count = 0
                        move_count += 1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game_run = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN and not played:
                    pos = pygame.mouse.get_pos()
                    played, player_pick, player_pos_x, player_pos_y = hand.choose_play_card(pos)
                    
            
            if(played and turn == 0 and next_turn):
                if(move_count == 0 and wait_count == 0):
                    rules.teams_update(hand, player_pick, turn)
                    hand.tricks.card_trick.append(player_pick)
                    hand.tricks.player_trick.append(turn)
                    hand.hands[turn].remove(player_pick)
                    hand.recalculate_pos(turn)
                
                if(move_count == MOVE_STEPS):
                    if(wait_count < round(FPS*0.3)):
                        wait_count += 1
                    else:
                        turn = turn+1 % 4
                        move_count = 0
                        played = False
                        if(len(hand.tricks.player_trick) == 4):
                            trick_end = True
                        wait_count = 0
                else:
                    if(wait_count == 0):
                        hand.tricks.move(turn, player_pos_x, player_pos_y)
                        hand.draw_cards(WIN)
                        wait_count += 1
                    elif(0 < wait_count < round(FPS*0.01)):
                        wait_count += 1
                    else:
                        wait_count = 0
                        move_count += 1
                
            if(trick_end):
                if(move_count == 0  and wait_count == 0):
                    next_turn = False
                    if(wait_count < round(FPS*1.5)):
                        wait_count += 1
                    wait_count = 0
                    turn = hand.tricks.get_highest(rules, hand)
                    hand.stacks[turn].img.append(hand.tricks.img)
                    hand.stacks[turn].player_stack.append(hand.tricks.card_trick[:])
                    hand.tricks.card_trick.clear()
                    hand.tricks.player_trick.clear()
                    rules.teams_update(hand,[],turn)
                    if(diagnostic_mode):
                        print('after:',rules.teams)
                    
                if(move_count == MOVE_STEPS):
                    trick_end = False
                    next_turn = True
                    move_count = 0
                    game_count += 1
                else:
                    if(wait_count == 0):
                        hand.stacks[turn].move()
                        hand.draw_cards(WIN)
                        wait_count += 1
                    elif(0 < wait_count < round(FPS*0.01)):
                        wait_count += 1
                    else:
                        wait_count = 0
                        move_count += 1
                    
                
            if(game_count == hand.num_cards):
                end_game = True
                next_turn = False
                     
    pygame.quit()

main()


