import pygame
import random

#créer une classe pour gérer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self,comet_event):
        super().__init__()
        #definir l'image associé à cette comette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity =random.randint(5,20)
        self.rect.x = random.randint(20,800)
        self.rect.y =  -random.randint(0,800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        #verifier si le nbre de comets est de 0
        if len(self.comet_event.all_comets) ==0 :
            print("l'evenement est fini ")
            #remettre la barre a 0
            self.comet_event.reset_percent()
            #apparaitre les 2 monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()


    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("Sol")
            #retirer la boule de feu
            self.remove()

            #si il nya plus de boule de feu
        if len(self.comet_event.all_comets)==0 :
             print("L'evenenment est fini")
             self.comet_event.reset_percent()
             self.comet_event.fall_mode=False

            #verifier si la boule touche le joueur
        if self.comet_event.game.check_collision(
                self,self.comet_event.game.all_players
        ):
            print("le joueur touché !!!")
            #returer la boule de feu
            self.remove()
            #subir 20 pts de degats
            self.comet_event.game.player.damage(20)


