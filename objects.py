import arcade


class DialougeObjects(arcade.Sprite):
    """Is an object that stores a message"""
    def __init__(self, image, scaling, message):
        super().__init__(image, scaling)
        self.message = message
        self.scaling = scaling

    def deliverMessage(self, key):
        """Delivers the object's message when interacted with"""
        if key:
            return self.message

    def isColliding(self, player):
        """Takes a player and returns true if this object is in contact with the player"""
        
        if abs(super().right - player.right) <= 8 * player.scale and abs(super().top - player.top) < 6 * player.scale:
            return True
        elif abs(super().top - player.top) <= 8 * player.scale and abs(super().right - player.right) < 8 * player.scale:
            return True
        else: 
            return False
