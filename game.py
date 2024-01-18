from player import Player
from  monster import Monster
from comet_event import CometFallEvent
import pygame
import shelve

from sounds import SoundManager

# erreur 400 vid 7/10  ( fi awel 18 minutes )

#creer une 2nd classe qui va representer notre jeu
class Game :
    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player=Player(self)
        self.all_players.add(self.player)
        #generer l'evenement
        self.comet_event = CometFallEvent(self)

        #groupe de monstre
        self.all_monsters=pygame.sprite.Group()


        #gerer le score
        self.sound_manager = SoundManager()

        #mettre le score à 0
        self.font = pygame.font.SysFont("monospace",30)

        self.score = 0
        self.pressed={}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def add_score(self,points=1):
        self.score += points

    def game_over(self):
        #remettre le jeu à neuf , retirer les monstres , remettre le joueur a 100% de vie

        self.all_monsters=pygame.sprite.Group()
        self.comet_event.all_comets=pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False


        d = shelve.open('score.txt')
        if(self.score > d['score']):
            d['score'] = self.score
        d.close()
        self.score=0
        #joueur le son
        self.sound_manager.play('game_over')



    def update(self, screen):
        #afficher le nbre des montres sur l'écran
        score_text = self.font.render(f"Nombre des robots tués  : {self.score}",1,(255,255,255))
        screen.blit(score_text,(30, 160))

        #afficher le score sur l'écran
        #score_text = self.font.render(f"Votre score  : {self.score *15} ",1,(255,255,255))
        #screen.blit(score_text,(200, 200))


        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)


        # actualier la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        #actualiser l'animation du joueur
        self.player.update_anmation()

        # recuperer les proj du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()


        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des image de mon grp de monstre
        self.all_monsters.draw(screen)

        #nhabtou béha les boules de feu
        #recuperer les comets de notre jeu
        for comet in self.comet_event.all_comets :
            comet.fall()
        #appliquer l'ensemble des images de mon grp
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueurer souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width(): #fih ghalta dhaherli
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self,sprite,group):
         return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)




    def spawn_monster(self):
        monster=Monster(self)
        self.all_monsters.add(monster)

