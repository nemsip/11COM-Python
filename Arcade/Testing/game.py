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

# define game window
class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BRITISH_RACING_GREEN)

    def on_draw(self):
        arcade.start_render()

GameWindow(1280, 720, "Currently running: " + gameName)

# render ground
# arcade.draw_lrtb_rectangle_filled()







# finish program
arcade.run()