import arcade
import random
import math

PLAYER_MOVEMENT_SPEED = 10
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1050
stopMovement = 0

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.NAPIER_GREEN)

        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", 0.7)
        self.player.center_x = SCREEN_WIDTH/2
        self.player.center_y = SCREEN_WIDTH/2

        self.coin_list = arcade.SpriteList()

        self.YouWin = ""

        self.randomCoinNum = random.randint(20, 1000)

        for n in range(self.randomCoinNum):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.7)
            coin.center_x = random.randint(0, SCREEN_WIDTH)
            coin.center_y = random.randint(0, SCREEN_HEIGHT)
            coin.change_x = random.randint(-5, 5)
            coin.change_y = random.randint(-5, 5)
            coin.time_until_die = float('inf')
            self.coin_list.append(coin)

        self.score = 0

        self.welcomeText = "Hello! Welcome to the Game!"

        self.time = 0

        self.win = False

        self.bomb = arcade.Sprite(":resources:images/tiles/bomb.png", 0.7)
        self.bomb.change_angle = 0.001

def on_draw(self):
        self.clear()
        self.player.draw()
        self.coin_list.draw()

        self.bomb.draw()

        if self.player.change_x == 0 and self.player.change_y == 0:
            arcade.draw_text(self.welcomeText, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLUE_BELL, 30,
                             anchor_x="center")
        else:
            self.welcomeText = ""


        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.BLACK, 14)
        self.coin_list.update()

        arcade.draw_text(self.YouWin, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLACK, 30,
                         anchor_x="center")

        def on_update(self, delta_time):
            self.player.update()
            self.bomb.update()

            self.bomb.center_x = SCREEN_WIDTH/2 + 200 * math.cos(self.bomb.angle * math.pi / 180)
            self.bomb.center_y = SCREEN_HEIGHT/2 + 200 * math.sin(self.bomb.angle * math.pi / 180)

            hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for coin in hit_list:
                coin.color = arcade.color.RED
                coin.time_until_die = 0.3

            if self.score == self.randomCoinNum:
                self.win = True
                self.YouWin = "Game over! You Win!\nPress 'Q' to Quit"

            for coin in self.coin_list:
                coin.time_until_die -= delta_time
                if coin.time_until_die <= 0:
                    coin.kill()
                    self.score += 1

                if coin.left < 0:
                    coin.left = stopMovement
                    coin.change_x = -coin.change_x
                if coin.right > SCREEN_WIDTH:
                    coin.right = SCREEN_WIDTH
                    coin.change_x = -coin.change_x
                if coin.top > SCREEN_HEIGHT:
                    coin.top = SCREEN_HEIGHT
                    coin.change_y = -coin.change_y
                if coin.bottom < 0:
                    coin.bottom = stopMovement
                    coin.change_y = -coin.change_y

            if self.player.left < 0:
                self.player.left = stopMovement
            if self.player.right > SCREEN_WIDTH:
                self.player.right = SCREEN_WIDTH
            if self.player.top > SCREEN_HEIGHT:
                self.player.top = SCREEN_HEIGHT
            if self.player.bottom < 0:
                self.player.bottom = stopMovement

        def on_key_press(self, key, modifiers):
            if key == arcade.key.UP or key == arcade.key.W:
                self.player.change_y = PLAYER_MOVEMENT_SPEED

            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.player.change_x = -PLAYER_MOVEMENT_SPEED

            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player.change_x = PLAYER_MOVEMENT_SPEED

            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.player.change_y = -PLAYER_MOVEMENT_SPEED

            if self.win == True and key == arcade.key.Q:
                arcade.close_window()

        def on_key_release(self, key, modifiers):
            if key == arcade.key.UP or key == arcade.key.W:
                self.player.change_y = stopMovement

            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.player.change_x = stopMovement

            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player.change_x = stopMovement

            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.player.change_y = stopMovement

MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Best Game Ever")
arcade.run()
