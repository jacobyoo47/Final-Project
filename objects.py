import arcade

class InteractObjects(arcade.Sprite):
    """Is an object that stores a message"""
    def __init__(self, image, scaling, message, otherMessage = None, hasItem = None, lock = False, door = False, breakable = False, disappears = False):
        super().__init__(image, scaling)
        self.message = message
        self.scaling = scaling
        self.otherMessage = otherMessage
        self.hasItem = hasItem
        self.lock = lock
        self.door = door
        self.breakable = breakable
        self.disappears = disappears

    def changeMessage(self):
        self.message = self.otherMessage

    def deliverMessage(self, color):
        """Delivers the object's message when interacted with"""
        # displays a rectangle of a certain color at the bottom of the screen.
        #arcade.start_render()

        arcade.draw_rectangle_filled(self.screen_width//2, self.text_height//2, self.screen_width, self.text_height, color)
        
        # displays text inside the rectangle.
        arcade.draw_text(self.message, 20, self.text_height - 35, arcade.color.WHITE, 16)


    def unlock(self):
        """Changes sprite image based if a key is brought to it"""
        
        self.texture = arcade.load_texture("Images/OpenDoor.png", mirrored = True, scale = self.scaling)

    def broken(self):
        """Changes sprite image based on if a crowbar is used on it (for crates)"""

        self.texture = arcade.load_texture("Images/broken_scraps.png", mirrored = True, scale = self.scaling)

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

class Switch(arcade.Sprite):
    def __init__(self, scaling, orientation = 'LEFT'):
        self.scaling = scaling
        self.orientation = orientation
        self.message = None

        if self.orientation != 'BROKEN':
            super().__init__('Images/lever_left.png', scaling)
            self.message = 'A lever, but it\'s missing the handle.'
        else:
            super().__init__('Images/lever_broken.png', scaling)

    def toggleSwitch(self):
        if self.orientation != 'BROKEN':
            if self.orientation == 'LEFT':
                self.texture = arcade.load_texture("Images/lever_neutral.png",scale = self.scaling)
                self.orientation = 'NEUTRAL'
            elif self.orientation == 'NEUTRAL':
                self.texture = arcade.load_texture("Images/lever_right.png", scale = self.scaling)
                self.orientation = 'RIGHT'
            else:
                self.texture = arcade.load_texture("Images/lever_left.png", scale = self.scaling)
                self.orientation = 'LEFT'


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
        