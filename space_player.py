from pygame.constants import K_DOWN,K_UP,K_f,K_s,K_LEFT,K_RIGHT
from pygame_player import PyGamePlayer
import pygame,sys, random
from pygame.locals import *
class SpacePlayer(PyGamePlayer):
    def __init__(self, force_game_fps=80    , run_real_time=False):
        """
        Example class for playing Pong
        """
        super(SpacePlayer, self).__init__(force_game_fps=force_game_fps, run_real_time=run_real_time)
        self.last_score = 0.0

    def get_keys_pressed(self, screen_array, feedback, terminal):
        # TODO: put an actual learning agent here

        return []

    def get_feedback(self):
        # import must be done here because otherwise importing would cause the game to start playing
        from MyApps import score, blueDestroy, greyDestroy, collideAsteroid, collideBullet, uselessShield, useFulShield, Shooting, uselessBullet

        # get the difference in score between this and the last run
        score_change = 0

	if(collideAsteroid==True):
		print("Collide Asteroid")
		score_change = -3
	elif(collideBullet==True):
		print("Collide Bullet")
		score_change = -3
	elif(uselessBullet==True):
		print("uselessBullet")
		score_change = -1
	elif(blueDestroy==True):
		print("blue Destroy")
		score_change = 2
	elif(greyDestroy==True):
		print("grey Destroy")
		score_change = 1
	else:
		score_change = 0

	self.last_score = score
        return float(score_change), score_change != 0

    def start(self):
        super(SpacePlayer, self).start()

        import MyApps


if __name__ == '__main__':
    player = SpacePlayer()
    player.start()
