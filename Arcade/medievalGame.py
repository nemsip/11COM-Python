import arcade

PLAYER_MOVEMENT_SPEED = 5

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.NAPIER_GREEN)

        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", 0.7)
        self.player.center_x = 525
        self.player.center_y = 350

        self.key_down = False

        # Create a viewport instance
        self.view_bottom = 0
        self.view_left = 0

    def on_draw(self):
        self.clear()
        self.player.draw()

    def on_update(self, delta_time):
        self.player.update()

        # Update the viewport to center on the player
        changed = False

        # Scroll left
        left_boundary = self.view_left + 200
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + self.width - 200
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + self.height - 200
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + 200
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                self.width + self.view_left,
                                self.view_bottom,
                                self.height + self.view_bottom)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = -PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = 0

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = 0

MyGame(1050, 700, "Best Game Ever")
arcade.run()