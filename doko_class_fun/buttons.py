import pygame
from .constants import BUTTON_COLOR, CUR_GAME_POSITION, CUR_CALL_POSITION, POSSIBLE_GAME_POSITION


class Buttons:
    def __init__(self):
        pygame.init()
        self.button_font = pygame.font.Font("freesansbold.ttf",9)
        self.game_font = pygame.font.Font("freesansbold.ttf",11)
    
    def draw(self, win, pos, button_pos, button_color, name):
        if((button_pos[0] < pos[0] < (button_pos[0]+button_pos[2])) and (button_pos[1] < pos[1] < (button_pos[1]+button_pos[3]))):
            pygame.draw.rect(win, button_color, button_pos)
            pressed = True
        else:
            pygame.draw.rect(win, button_color, button_pos)  
            pressed = False 
        textSurf, textRect = self.text_objects(name, self.button_font)
        textRect.center = ((button_pos[0]+(button_pos[2]/2)), (button_pos[1]+(button_pos[3]/2)))
        win.blit(textSurf, textRect)
        return pressed
    
    def draw_called(self, win, rules):
        if(rules.current_game.count('Solo') == 1):
            player_ind = [ind for ind,x in enumerate(rules.teams) if x[0] == 'RE'][0]
            pygame.draw.rect(win, BUTTON_COLOR['SOLO'], CUR_GAME_POSITION[player_ind])
            textSurf, textRect = self.text_objects(rules.current_game, self.game_font)
            textRect.center = ((CUR_GAME_POSITION[player_ind][0]+(CUR_GAME_POSITION[player_ind][2]/2)), (CUR_GAME_POSITION[player_ind][1]+(CUR_GAME_POSITION[player_ind][3]/2)))
            win.blit(textSurf, textRect)
        
        if(rules.current_game.count('Poverty') == 1):
            player_ind = [ind for ind,x in enumerate(rules.teams) if x[3] == 'Poverty'][0]
            pygame.draw.rect(win, BUTTON_COLOR['SOLO'], CUR_GAME_POSITION[player_ind])
            textSurf, textRect = self.text_objects('Poverty', self.game_font)
            textRect.center = ((CUR_GAME_POSITION[player_ind][0]+(CUR_GAME_POSITION[player_ind][2]/2)), (CUR_GAME_POSITION[player_ind][1]+(CUR_GAME_POSITION[player_ind][3]/2)))
            win.blit(textSurf, textRect)
            player_ind = [ind for ind,x in enumerate(rules.teams) if x[3] == 'Rich'][0]
            pygame.draw.rect(win, BUTTON_COLOR['SOLO'], CUR_GAME_POSITION[player_ind])
            textSurf, textRect = self.text_objects('Rich', self.game_font)
            textRect.center = ((CUR_GAME_POSITION[player_ind][0]+(CUR_GAME_POSITION[player_ind][2]/2)), (CUR_GAME_POSITION[player_ind][1]+(CUR_GAME_POSITION[player_ind][3]/2)))
            win.blit(textSurf, textRect)
        
        if(rules.current_game.count('Wedding') == 1):
            player_ind = [ind for ind,x in enumerate(rules.teams) if x[2] == 'Wedding'][0]
            pygame.draw.rect(win, BUTTON_COLOR['SOLO'], CUR_GAME_POSITION[player_ind])
            textSurf, textRect = self.text_objects('Wedding', self.game_font)
            textRect.center = ((CUR_GAME_POSITION[player_ind][0]+(CUR_GAME_POSITION[player_ind][2]/2)), (CUR_GAME_POSITION[player_ind][1]+(CUR_GAME_POSITION[player_ind][3]/2)))
            win.blit(textSurf, textRect)
            player_ind = [ind for ind,x in enumerate(rules.teams) if x[2] == 'Bride']
            if(player_ind):
                pygame.draw.rect(win, BUTTON_COLOR['SOLO'], CUR_GAME_POSITION[player_ind[0]])
                textSurf, textRect = self.text_objects('Bride', self.game_font)
                textRect.center = ((CUR_GAME_POSITION[player_ind[0]][0]+(CUR_GAME_POSITION[player_ind[0]][2]/2)), (CUR_GAME_POSITION[player_ind[0]][1]+(CUR_GAME_POSITION[player_ind[0]][3]/2)))
                win.blit(textSurf, textRect)
            
        for player_ind in range(4):
            if(rules.teams[player_ind][5] and rules.teams[player_ind][1]):
                pygame.draw.rect(win, BUTTON_COLOR['CALL'][player_ind], CUR_CALL_POSITION[player_ind])
                textSurf, textRect = self.text_objects(' '.join(rules.teams[player_ind][5]), self.game_font)
                textRect.center = ((CUR_CALL_POSITION[player_ind][0]+(CUR_CALL_POSITION[player_ind][2]/2)), (CUR_CALL_POSITION[player_ind][1]+(CUR_CALL_POSITION[player_ind][3]/2)))
                win.blit(textSurf, textRect)
                
    def draw_game(self, win, poss_game, player):
        for ind,x in enumerate(poss_game):
            pygame.draw.rect(win, BUTTON_COLOR['POSSIBLE_GAME'], POSSIBLE_GAME_POSITION[(player + ind) % 4])
            textSurf, textRect = self.text_objects(x, self.game_font)
            textRect.center = ((POSSIBLE_GAME_POSITION[(player + ind) % 4][0]+(POSSIBLE_GAME_POSITION[(player + ind) % 4][2]/2)), (POSSIBLE_GAME_POSITION[(player + ind) % 4][1]+(POSSIBLE_GAME_POSITION[(player + ind) % 4][3]/2)))
            win.blit(textSurf, textRect)
            
    def text_objects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()
    
    def end_screen(self, win, Player_Game_points, cur_game_str):
        textSurf, textRect = self.text_objects(cur_game_str, self.game_font)
        #textRect.center = ((CUR_CALL_POSITION[player_ind][0]+(CUR_CALL_POSITION[player_ind][2]/2)), (CUR_CALL_POSITION[player_ind][1]+(CUR_CALL_POSITION[player_ind][3]/2)))
        win.blit(textSurf, textRect)
        
        
    