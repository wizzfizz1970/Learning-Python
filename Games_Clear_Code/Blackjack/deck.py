import pygame
import os

class Deck:
    def __init__(self):
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        self.cards = self.generate_deck()
        self.card_images = []

    def generate_deck(self):
        """Create the deck with file paths for each card."""
        # Define the base path for the images
        base_path = os.path("Blackjack/images/card/PNG-cards-1.3/")
        
        return [
            {'value': value, 'suit': suit, 'file': os.path.join(base_path, f"{value}_of_{suit}.png")}
            for suit in self.suits
            for value in self.values
        ]

    def load_images(self):
        """Load card images into the card_images list."""
        for card in self.cards:
            try:
                image = pygame.image.load(card['file']).convert_alpha()
                self.card_images.append(image)
            except FileNotFoundError:
                print(f"Error: {card['file']} not found.")

    def shuffle(self):
        """Shuffle the deck (this is a placeholder for future functionality)."""
        import random
        random.shuffle(self.cards)
