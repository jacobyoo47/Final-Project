import arcade
import scripts

class DialogueObjects(arcade.Sprite):
    """Is an object that stores a message"""
    def __init__(self, image, scaling, message, SCREEN_WIDTH, TEXT_BOX_HEIGHT):
        super().__init__(image, scaling)
        self.message = message
        self.scaling = scaling
        self.screen_width = SCREEN_WIDTH
        self.text_height = TEXT_BOX_HEIGHT
        
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
        
        if abs(super().right - player.right) <= 8 * player.scale and abs(super().top - player.top) < 6 * player.scale:
            return True
        elif abs(super().top - player.top) <= 8 * player.scale and abs(super().right - player.right) < 8 * player.scale:
            return True
        else: 
            return False
