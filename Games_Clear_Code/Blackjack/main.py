import pygame
from deck import Deck

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 680
FPS = 60  # Frame rate limit

class Game:
    def __init__(self):
        # Initialize pygame and set up the game window
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Black Jack')
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize the deck and load card images
        self.deck = Deck()
        self.deck.load_images()
        self.card_images = self.deck.card_images
        self.cards = self.deck.cards  # Access the list of card data (values, suits)

        # Initialize card positions
        self.card_positions = [(x, 50) for x in range(50, len(self.card_images) * 90, 90)]  # Spacing for cards
  
    def setup(self):
        """Any additional setup can go here."""
        pass
  
    def run(self):
        while self.running:
            # Delta time for smooth movement
            dt = self.clock.tick(FPS) / 1000

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    # Handle window resizing
                    new_width, new_height = event.w, event.h
                    pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

            # Update (add game logic here)

            # Draw
            self.display_surface.fill('black')  # Fill the screen with black

            # Draw the cards
            for i, card_image in enumerate(self.card_images):
                x, y = self.card_positions[i]  # Get the x and y position for each card
                self.display_surface.blit(card_image, (x, y))  # Draw the card image at the specified position

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
