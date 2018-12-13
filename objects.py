import arcade

class DialogueObjects(arcade.Sprite):
    """Is an object that stores a message"""
    def __init__(self, image, scaling, message, SCREEN_WIDTH, TEXT_BOX_HEIGHT, key = False):
        super().__init__(image, scaling)
        self.message = message
        self.scaling = scaling
        self.screen_width = SCREEN_WIDTH
        self.text_height = TEXT_BOX_HEIGHT
        self.key = key
        
    def deliverMessage(self, color):
        """Delivers the object's message when interacted with"""
        # displays a rectangle of a certain color at the bottom of the screen.
        #arcade.start_render()

        arcade.draw_rectangle_filled(self.screen_width//2, self.text_height//2, self.screen_width, self.text_height, color)
        
        # displays text inside the rectangle.
        arcade.draw_text(self.message, 20, self.text_height - 35, arcade.color.WHITE, 16)
        #debug


    def isColliding(self, player):
        """Takes a player and returns true if this object is in contact with the player"""
        direction = player.direction
        if direction[1] == 'LEFT':
            if abs(player.left - super().right) < player.scale and abs(super().top - player.top) < 4 * player.scale:
                return True
        elif direction[1] == 'RIGHT':
            if abs(super().left - player.right) < player.scale and abs(super().top - player.top) < 4 * player.scale:
                return True
        if direction[0] == 'DOWN':
            if abs(super().top - player.bottom) < player.scale and abs(super().right - player.right) < 4 * player.scale:
                return True
        elif direction[0] == 'UP':
            if abs(super().bottom - player.top) < player.scale and abs(super().right - player.right) < 4 * player.scale:
                return True
        else: 
            return False
