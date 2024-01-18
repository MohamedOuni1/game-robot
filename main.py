import pygame
import math
from game import Game
import shelve

pygame.init()
#generer la fenetre de notre jeu
pygame.display.set_caption("Poly Robot")
screen =pygame.display.set_mode((1050,1080))


#impoter de charger l'arriére plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

#importer charger notre banniére
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(600, 450))
banner_rect = banner.get_rect()
banner_rect.x =math.ceil(screen.get_width()/5)
banner_rect.y =math.ceil(screen.get_width()/8)


#importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height() /2)


#charger notre jeu
game=Game()
running = True
#boucle tant que cette condition est vrai
while running:
    #appliquer l'arriere plan de notre jeu
    screen.blit(background,(-500,-1700))


    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencé
    else :
    #ajouter mon ecran de bienvenue
        d = shelve.open('score.txt')


        font = pygame.font.Font(pygame.font.match_font('poppins'), 48)
        text_surface = font.render("HIGHSCORE: " + str(d['score']), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (math.ceil(screen.get_width()/3.33 +200), math.ceil(screen.get_height()  /2 +150))
        screen.blit(text_surface, text_rect)
        d.close()
        screen.blit(play_button,play_button_rect)
        screen.blit(banner,banner_rect)



    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fentre
        if event.type==pygame.QUIT :
            running = False
            pygame.quit()
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key]= True

            #detecter si la touche esoace est enclanchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing :
                    game.player.launch_projectile()
                else :
                    # mettre le jeu en mode "lancé"
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key]=False

        elif event.type == pygame.MOUSEBUTTONDOWN :
            #verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos) :
                #mettre le jeu en mode "lancé"
                game.start()
                #jouer le son
                game.sound_manager.play('click')



