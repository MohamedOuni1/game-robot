import pygame
import random
import animation


#creer une classe qui va gérer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprtie):
    def __init__(self,game):
        super().__init__("mummy")
        self.game = game
        self.health=100
        self.max_health=100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 520
        self.loot_amount = 1
        self.velocity = random.randint(1,3)
        self.start_animation()

    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity=random.randint(1,speed)

    def set_loot_amount(self,amount):
        self.loot_amount=amount


    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        #verifier si son nouveau nombre de points
        if self.health<=0 :
            #rapparaitre comme un nouveau monstre
            self.rect.x=1000 +random.randint(0,300)
            self.velocity=random.randint(1,3)
            self.health=self.max_health
            #ajouter le nbre de pts
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est chargé a son max
            if self.game.comet_event.is_full_loaded():
                #retirer le jeu
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)



    def update_health_bar(self,surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 160, self.rect.y + 180, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 160, self.rect.y + 180, self.health, 7])



    def forward(self):
        #le deplacement ne se fait que si il nya pas de collision avec un joueur
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity

        #si le monstre est en collision avec le joueur
        else :
            #infliger des degats(au joueur)
            self.game.player.damage(self.attack)



