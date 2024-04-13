import pygame
import subprocess

pygame.init()


# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sports & Fitness App Leaderboard")

clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load("gym_background.webp")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define font
font = pygame.font.Font(None, 36)

# Open the file for reading
with open('database.txt', 'r') as file:
    lines = file.readlines()  # Read all lines from the file

# Initialize a dictionary to store data
person_data = {}

# Process each line in the file
for line in lines:
    # Split the line into parts based on whitespace
    parts = line.split()

    # Extract values from parts
    name = parts[0]
    squat_number = int(parts[1])
    press_number = int(parts[2])

    # Store values in the dictionary
    person_data[name] = {'squat': squat_number, 'press': press_number}

# Display the dictionary content
for name, data in person_data.items():
    print(f"Name: {name}, Squat Number: {data['squat']}, Press Number: {data['press']}")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check button clicks
                if button8_rect.collidepoint(event.pos):
                    pygame.quit()

        # Draw background
        screen.blit(background_image, (0, 0))

        # Draw buttons
        button0_rect = pygame.draw.rect(screen, GREEN, (50, 100, 200, 50))
        draw_text("People", font, WHITE, screen, 150, 125)

        button1_rect = pygame.draw.rect(screen, GREEN, (50, 200, 200, 50))
        draw_text("Ananya", font, WHITE, screen, 150, 225)

        button2_rect = pygame.draw.rect(screen, GREEN, (50, 300, 200, 50))
        draw_text("Donna", font, WHITE, screen, 150, 325)

        button5_rect = pygame.draw.rect(screen, GREEN, (300, 100, 200, 50))
        draw_text("Squat", font, WHITE, screen, 400, 125)

        button6_rect = pygame.draw.rect(screen, GREEN, (300, 200, 200, 50))
        draw_text(str(person_data["Ananya"]["squat"]), font, WHITE, screen, 400, 225)

        button7_rect = pygame.draw.rect(screen, GREEN, (300, 300, 200, 50))
        draw_text(str(person_data["Donna"]["squat"]), font, WHITE, screen, 400, 325)

        button5_rect = pygame.draw.rect(screen, GREEN, (550, 100, 200, 50))
        draw_text("Press", font, WHITE, screen, 650, 125)

        button6_rect = pygame.draw.rect(screen, GREEN, (550, 200, 200, 50))
        draw_text(str(person_data["Ananya"]["press"]), font, WHITE, screen, 650, 225)

        button7_rect = pygame.draw.rect(screen, GREEN, (550, 300, 200, 50))
        draw_text(str(person_data["Donna"]["press"]), font, WHITE, screen, 650, 325)

        button8_rect = pygame.draw.rect(screen, GREEN, (550, 400, 200, 50))
        draw_text("Quit", font, WHITE, screen, 650, 425)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
