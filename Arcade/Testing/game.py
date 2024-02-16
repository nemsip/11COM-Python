# game.py
# --------------
# Resources:
# https://www.youtube.com/watch?v=2qP1M1Nf__w
# https://www.youtube.com/watch?v=yCTUzf-Exbc - 11:38
# --------------

# imports
import arcade

# define placeholders
gameName = "placeholder.Generic.gameName"
playerName = "placeholder.Generic.playerName"
healthAmount = "placeholder.health.healthAmount"
damageAmount = "placeholder.health.damageAmount"
combatPower = "placeholder.combat.combatPower"

# Constant vars
SCREEN_TITLE = gameName

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20






# finish program
arcade.run()