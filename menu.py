import pygame
import subprocess

pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Welcome to Sports & Fitness App")

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
                if button1_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "squat.py"])
                elif button2_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "press.py"])
                elif button3_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "script3.py"])
                elif button4_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "script4.py"])
                elif button8_rect.collidepoint(event.pos):
                    subprocess.Popen(["python", "leaderboard.py"])

        # Draw background
        screen.blit(background_image, (0, 0))

        # Draw buttons
        button0_rect = pygame.draw.rect(screen, GREEN, (50, 100, 200, 50))
        draw_text("Workouts", font, WHITE, screen, 150, 125)

        button1_rect = pygame.draw.rect(screen, GREEN, (50, 200, 200, 50))
        draw_text("Squat", font, WHITE, screen, 150, 225)

        button2_rect = pygame.draw.rect(screen, GREEN, (50, 300, 200, 50))
        draw_text("Overhead Press", font, WHITE, screen, 150, 325)

        button3_rect = pygame.draw.rect(screen, GREEN, (50, 400, 200, 50))
        draw_text("Workout 3", font, WHITE, screen, 150, 425)

        button4_rect = pygame.draw.rect(screen, GREEN, (50, 500, 200, 50))
        draw_text("Workout 4", font, WHITE, screen, 150, 525)

        button8_rect = pygame.draw.rect(screen, GREEN, (550, 100, 200, 50))
        draw_text("Next", font, WHITE, screen, 650, 125)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
