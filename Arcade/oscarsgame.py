import arcade
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.invincible_countdown = None
        arcade.set_background_color(arcade.color.MEDIUM_AQUAMARINE)
        self.setup()

    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", 0.7)
        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = SCREEN_HEIGHT / 2
        self.coin_list = arcade.SpriteList()
        self.score = 0
        self.game_over = False

        for n in range(30):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
            coin.center_x = random.randint(0, SCREEN_WIDTH)
            coin.center_y = random.randint(0, SCREEN_HEIGHT)
            coin.change_x = random.randint(-5, 5)
            coin.change_y = random.randint(-5, 5)
            self.coin_list.append(coin)
            self.bomb = arcade.Sprite(":resources:images/tiles/bomb.png")
            self.bomb.change_angle = 1
            self.time = 0
            self.bonus_list = arcade.SpriteList()
            self.bonus_countdown = 3

            self.bonus2_list = arcade.SpriteList()
            self.bonus2_countdown = 3

            self.invincible_countdown = 0

            self.bonus3_list = arcade.SpriteList()
            self.bonus3_countdown = 3
            self.speedincrease_countdown = 0

    def on_draw(self):
        self.clear()
        self.player.draw()
        self.coin_list.draw()
        self.bonus_list.draw()
        self.bomb.draw()
        self.bonus2_list.draw()
        self.bonus3_list.draw()
        arcade.draw_text(f"Score: {self.score} ", 25, 25, arcade.color.BLACK, 15)

        # arcade.draw_text(f"Timer: {self.time} ", 30, SCREEN_HEIGHT - 30, arcade.color.BLACK, 15)

        arcade.draw_line(0, SCREEN_HEIGHT, SCREEN_WIDTH - (SCREEN_WIDTH * self.time / 20),
                         SCREEN_HEIGHT, arcade.color.LIME, 30)

        if self.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 60, SCREEN_WIDTH,
                             anchor_x='center')

            arcade.draw_text("Press R to restart", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60, arcade.color.BLACK, 30,
                             SCREEN_WIDTH, anchor_x='center')

    def on_update(self, delta_time):
        global PLAYER_SPEED

        self.time += delta_time

        self.bonus_countdown -= delta_time
        if self.bonus_countdown < 0:
            bonus = arcade.Sprite(":resources:images/items/gemRed.png", 0.5)
            bonus.center_x = random.randint(0, SCREEN_WIDTH)
            bonus.center_y = random.randint(0, SCREEN_HEIGHT)
            bonus.change_x = random.randint(-5, 5)
            bonus.change_y = random.randint(-5, 5)
            self.bonus_list.append(bonus)
            self.bonus_countdown = 3

        self.bonus2_countdown -= delta_time
        if self.bonus2_countdown < 0:
            bonus = arcade.Sprite(":resources:images/items/gemBlue.png", 0.5)
            bonus.center_x = random.randint(0, SCREEN_WIDTH)
            bonus.center_y = random.randint(0, SCREEN_HEIGHT)
            bonus.change_x = random.randint(-5, 5)
            bonus.change_y = random.randint(-5, 5)
            self.bonus2_list.append(bonus)
            self.bonus2_countdown = 3

        self.bonus3_countdown -= delta_time
        if self.bonus3_countdown < 0:
            bonus = arcade.Sprite(":resources:images/items/gemYellow.png", 0.5)
            bonus.center_x = random.randint(0, SCREEN_WIDTH)
            bonus.center_y = random.randint(0, SCREEN_HEIGHT)
            bonus.change_x = random.randint(-5, 5)
            bonus.change_y = random.randint(-5, 5)
            self.bonus3_list.append(bonus)
            self.bonus3_countdown = 3


        if self.game_over:
            return

        self.player.update()
        self.coin_list.update()
        self.bomb.update()

        self.bomb.center_x = SCREEN_WIDTH/2 + 300 * math.cos(self.bomb.angle * math.pi / 180)
        self.bomb.center_y = SCREEN_HEIGHT/2 + 300 * math.sin(self.bomb.angle * math.pi / 180)

        if arcade.check_for_collision(self.player, self.bomb):
            if self.invincible_countdown <= 0:
                self.game_over = True

        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in hit_list:
            coin.color = arcade.color.RED
            coin.kill()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player, self.bonus_list)
        for bonus in hit_list:
            self.time -= 3
            bonus.kill()

        hit_list = arcade.check_for_collision_with_list(self.player, self.bonus2_list)
        for bonus in hit_list:
            
            self.invincible_countdown = 3
            self.player.color = arcade.color.BLUE
            bonus.kill()

        hit_list = arcade.check_for_collision_with_list(self.player, self.bonus3_list)
        for bonus in hit_list:
            self.speedincrease_countdown = PLAYER_SPEED + 5
            self.player.color = arcade.color.CYAN
            bonus.kill()

        if self.speedincrease_countdown <= 0:
            self.player.color = arcade.color.WHITE
            PLAYER_SPEED = PLAYER_SPEED - 5

        if len(self.coin_list) == 0:
            self.game_over = True

        if self.time > 20:
            self.game_over = True

        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH
        if self.player.top > SCREEN_HEIGHT:
            self.player.top = SCREEN_HEIGHT
        if self.player.bottom < 0:
            self.player.bottom = 0

        for coin in self.coin_list:
            if coin.left < 0:
                coin.left = 0
                coin.change_x = -coin.change_x
            if coin.right > SCREEN_WIDTH:
                coin.right = SCREEN_WIDTH
                coin.change_x = -coin.change_x
            if coin.top > SCREEN_HEIGHT:
                coin.top = SCREEN_HEIGHT
                coin.change_y = -coin.change_y
            if coin.bottom < 0:
                coin.bottom = 0
                coin.change_y = -coin.change_y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        if key == arcade.key.W or key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        if key == arcade.key.S or key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED
        if key == arcade.key.Z:
            self.player.color = arcade.color.RED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.player.change_x = 0
        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.player.change_x = 0
        if key == arcade.key.W or key == arcade.key.UP:
            self.player.change_y = 0
        if key == arcade.key.S or key == arcade.key.DOWN:
            self.player.change_y = 0
        if key == arcade.key.Z:
            self.player.color = arcade.color.WHITE
        if key == arcade.key.R and self.game_over:
            self.setup()


MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Best Game Ever")
arcade.run()