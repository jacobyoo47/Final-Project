"""
Sprite move between different rooms.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_rooms
"""
import math
import arcade
import os
import objects

#For the dialogue stuff
TEXT_BOX_HEIGHT = 100

#Scaling all the images on the screen
SPRITE_SCALING = 5
SPRITE_NATIVE_SIZE = 8
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 30
SCREEN_HEIGHT = SPRITE_SIZE * 16

#Game states
GAME = 0
DIALOGUE = 1

#Inherent traits of player
MOVEMENT_SPEED = 5

class Player(arcade.Sprite):
    def __init__(self):
        """creates the character Sprite"""
        #The parent init method
        super().__init__("Images/CharacterRight.png", SPRITE_SCALING)
        
        #Motion variables
        self.leftMotion = False
        self.rightMotion = False
        self.upMotion = False
        self.downMotion = False

        #Directional Facing
        self.direction = ["UP", "RIGHT"]

        #Interacting Variables
        self.useObject = False
    
    def update_animation(self):
        """Adding images that show which direction the character is facing"""
        if self.direction[1] == 'LEFT':
            self.texture = arcade.load_texture("Images/CharacterRight.png", mirrored = True, scale = SPRITE_SCALING)
        elif self.direction[1] == 'RIGHT':
            self.texture = arcade.load_texture("Images/CharacterRight.png", scale = SPRITE_SCALING)

class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self, ):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.portal_list = None
        self.object_list = None
        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None

class Portal(arcade.Sprite):
    """
    This class represents the portals on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.portal_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Images/RogueSprites/block1.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("Images/RogueSprites/block1.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("Images/RogueSprites/block1.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.
    # Make a portal
    portal = Portal("gold_portal.png", SPRITE_SCALING)
    portal.left = 5 * SPRITE_SIZE
    portal.bottom = 6 * SPRITE_SIZE
    room.portal_list.append(portal)

    #Adding interactable objects
    box = objects.DialogueObjects("Images/Sign.png", SPRITE_SCALING, "A boring, brown, container. ", SCREEN_WIDTH, TEXT_BOX_HEIGHT)
    box.left = 2 * SPRITE_SIZE
    box.bottom = 13 * SPRITE_SIZE
    #Adding this object to the wall_list so that it can be drawn and have collision
    room.wall_list.append(box)
    room.object_list.append(box)

    #Same as the above
    box2 = objects.DialogueObjects("Images/Sign.png", SPRITE_SCALING, "Another daft box. ", SCREEN_WIDTH, TEXT_BOX_HEIGHT)
    box2.left = 4 * SPRITE_SIZE
    box2.bottom = 13 * SPRITE_SIZE
    room.wall_list.append(box2)
    room.object_list.append(box2)


    # Load the background image for this level.
    room.background = arcade.load_texture("Images/floor1.jpg")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.portal_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("Images/RogueSprites/block1.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH -  SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("Images/RogueSprites/block1.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("Images/RogueSprites/block1.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)

    #Setting the background of the room
    room.background = arcade.load_texture("Images/floor1.jpg")

    return room


class MyGame(arcade.Window):
    """ Main application class. """
    
    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        #Setting the state of the game
        self.state = GAME

        #The object that has a message with it
        self.current_message = None

        # Set up the player
        self.rooms = None
        self.score = 0
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.useObject = None
        self.total_time = 0.0

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.score = 0
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        #Setting the state of the game
        self.state = GAME

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def draw_game(self):
        """
        Render the screen.
        """

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.
        self.rooms[self.current_room].portal_list.draw()

        #Draws all player sprites
        self.player_list.draw()

    def draw_dialogue(self):
        """Draws the dialogue over the screen"""
        self.draw_game()
        self.current_message.deliverMessage(arcade.color.DARK_BLUE)

    def on_draw(self):
        """Draws the things on the screen"""
        arcade.start_render()

        if self.state == GAME:
            self.draw_game()

        elif self.state == DIALOGUE:
            self.draw_dialogue()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        
        
        if self.state == GAME:
            ## MOVEMENT:
            if key == arcade.key.UP:
                #The direction is made so that we'll know what object the player will interact with
                self.player_sprite.direction[0] = "UP"
                #This boolean is used for the program to remember that this key was pressed and is held down
                self.player_sprite.upMotion = True
                #Changing the velocity of the player
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.direction[0] = "DOWN"
                self.player_sprite.downMotion = True
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.direction[1] = "LEFT"
                self.player_sprite.leftMotion = True
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.direction[1] = "RIGHT"
                self.player_sprite.rightMotion = True
                self.player_sprite.change_x = MOVEMENT_SPEED

            ## PLAYER INTERACTIONS:
            elif key == arcade.key.Z:
                self.player_sprite.useObject = True

        #Exiting the diaglogue stage
        elif self.state == DIALOGUE:
            if key == arcade.key.Z:
                self.player_sprite.useObject = False
                self.state = GAME

        

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        ## MOVEMENT:
        if self.state == GAME:
            #Handles if two opposing keys are being pressed
            #UP and DOWN key
            if self.player_sprite.upMotion and self.player_sprite.downMotion:
                #If UP is released, move down
                if key == arcade.key.UP:
                    #Make the upMotion boolean false bc not moving up anymore
                    self.player_sprite.upMotion = False
                    #Change the direction the player is facing
                    self.player_sprite.direction[0] = 'DOWN'
                    #Changing the velocity of the object
                    self.player_sprite.change_y = -MOVEMENT_SPEED
                #If DOWN is released, move up
                elif key == arcade.key.DOWN:
                    self.player_sprite.downMotion = False
                    self.player_sprite.direction[0] = 'UP'
                    self.player_sprite.change_y = MOVEMENT_SPEED
                #This will handle any other key being released
                elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
                    self.player_sprite.rightMotion = False
                    self.player_sprite.leftMotion = False
                    self.player_sprite.change_x = 0
            #RIGHT and DOWN key 
            elif self.player_sprite.leftMotion and self.player_sprite.rightMotion:
                #If RIGHT is released, move left
                if key == arcade.key.RIGHT:
                    self.player_sprite.rightMotion = False
                    self.player_sprite.direction[1] = 'LEFT'
                    self.player_sprite.change_x = -MOVEMENT_SPEED
                #If LEFT is released, move right
                elif key == arcade.key.LEFT:
                    self.player_sprite.leftMotion = False
                    self.player_sprite.direction[1] = 'RIGHT'
                    self.player_sprite.change_x = MOVEMENT_SPEED
                #Handle all other key being pressed
                elif key == arcade.key.UP or key == arcade.key.DOWN:
                    self.player_sprite.upMotion = False
                    self.player_sprite.downMotion = False
                    self.player_sprite.change_y = 0

            #Normal movement with only one key being held down
            elif key == arcade.key.UP or key == arcade.key.DOWN:
                self.player_sprite.upMotion = False
                self.player_sprite.downMotion = False
                self.player_sprite.change_y = 0
            elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.player_sprite.rightMotion = False
                self.player_sprite.leftMotion = False
                self.player_sprite.change_x = 0
            

            ## PLAYER INTERACTIONS
            elif key == arcade.key.Z:
                self.player_sprite.useObject = False


    def update(self, delta_time):
        """ Movement and game logic """
        ## TIME:
        self.total_time += delta_time

        #Changing the sprite to face direction it's direction
        self.player_sprite.update_animation()

        #Normalizing diagonal movement.\:
        #Diagonal speed will be 5 
        #If the player has upward movement
        if self.player_sprite.upMotion:
            if self.player_sprite.rightMotion and self.player_sprite.change_x > 0:
                x = math.sqrt(MOVEMENT_SPEED**2/2)
                y = math.sqrt(MOVEMENT_SPEED**2/2)
            elif self.player_sprite.leftMotion and self.player_sprite.change_x < 0:
                x = -1 * math.sqrt(MOVEMENT_SPEED**2/2)
                y = math.sqrt(MOVEMENT_SPEED**2/2)
        #If the player has downward movement
        if self.player_sprite.downMotion:
            if self.player_sprite.rightMotion and self.player_sprite.change_x > 0:
                x = math.sqrt(MOVEMENT_SPEED**2/2)
                y = -1 * math.sqrt(MOVEMENT_SPEED**2/2)
            elif self.player_sprite.leftMotion and self.player_sprite.change_x < 0:
                x = -1 * math.sqrt(MOVEMENT_SPEED**2/2)
                y = -1 * math.sqrt(MOVEMENT_SPEED**2/2)
    
        #Collision list for portals
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].portal_list)

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH

        #PORTAL INTERACTION
        elif self.current_room == 0 and len(hit_list) > 0 and self.player_sprite.useObject == True: # len(hit_list) > 0 should be changed later on to be more specific
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        #Object Interaction
        for items in self.rooms[self.current_room].object_list:
            if items.isColliding(self.player_sprite) and self.player_sprite.useObject:
                #Ensuring there is no movement after interacting with an object
                self.player_sprite.change_x = 0
                self.player_sprite.change_y = 0
                self.player_sprite.rightMotion = False
                self.player_sprite.leftMotion = False
                self.player_sprite.upMotion = False
                self.player_sprite.downMotion = False
                #Changing the state of the game
                self.current_message = items
                self.state = DIALOGUE
        

        

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()