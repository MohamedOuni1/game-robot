import pygame
from projectile import Projectile
import animation

#creer une premiere classe qui va represetnter notre joueur
class Player(animation.AnimateSprtie) :

    def __init__(self,game):
        super().__init__('player')
        self.game = game
        self.health=100
        self.max_health=100
        self.attack=20
        self.velocity=15
        self.all_projectiles=pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x=400
        self.rect.y=500


    def damage(self,amount):
        if self.health - amount > amount:
            self.health -= amount
        else :
            #si le joueur n'a plus de points de vie
            self.game.game_over()

    def update_anmation(self):
        self.animate()


    def update_health_bar(self, surface):
        # dessier notre barre de vie******************
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 160, self.rect.y + 150, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 160, self.rect.y + 150, self.health, 7])


    def launch_projectile(self):
        # creer une nouuvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))
        #demarrer l'animation de lancer
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play('tir')


    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self,self.game.all_monsters) :
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -=self.velocity


