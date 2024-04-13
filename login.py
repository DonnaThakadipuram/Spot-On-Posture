import pygame
import sys
import subprocess
import requests

# Define the API endpoint URLs for id=1 and id=2
url_id_1 = "https://so-epic-right-now.kintone.com/k/v1/record.json?app=3&id=1"
url_id_2 = "https://so-epic-right-now.kintone.com/k/v1/record.json?app=3&id=2"

# Set the API token in the headers
headers = {
    "X-Cybozu-API-Token": "Dzg8sZPBnT5qaEYvb2rWxciDkazzm08vOL39qVW8"
}

# Function to fetch record data and return as a tuple
def fetch_record_data(url):
    # Send HTTP GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the values for 'coolname' and 'soawesome' from the 'record' dictionary
        record_id = data['record']['Record_number']['value']
        coolname_value = data['record']['username']['value']
        soawesome_value = data['record']['password']['value']

        # Return the record details as a tuple
        return (record_id, coolname_value, soawesome_value)

    else:
        # Print error message if the request was not successful
        print(f"Error fetching record from URL: {url}")
        print("Error:", response.text)
        return None

# List to store tuples of record details
records_list = []

# Fetch and store record data for id=1
record_data = fetch_record_data(url_id_1)
if record_data:
    records_list.append(record_data)

# Fetch and store record data for id=2
record_data = fetch_record_data(url_id_2)
if record_data:
    records_list.append(record_data)

# Function to perform authentication based on username and password
def authentication(username, password):
    for record in records_list:
        if record[1] == username and record[2] == password:
            return True
    return False


# Pygame initialization
pygame.init()
clock = pygame.time.Clock()

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Login to Sports & Fitness App")

# Load background image
background_image = pygame.image.load("gym_background.webp")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Define colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 32)

# Input box properties
user_text = ''
password_text = ''
username_rect = pygame.Rect(200, 200, 400, 40)
password_rect = pygame.Rect(200, 300, 400, 40)
login_button_rect = pygame.Rect(300, 400, 200, 50)
active_username = False
active_password = False


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(surface, rect, color, text, text_color):
    pygame.draw.rect(surface, color, rect)
    draw_text(text, font, text_color, surface, rect.x + 10, rect.y + 10)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if mouse click is inside username input box
            if username_rect.collidepoint(event.pos):
                active_username = True
                active_password = False
            # Check if mouse click is inside password input box
            elif password_rect.collidepoint(event.pos):
                active_username = False
                active_password = True
            else:
                active_username = False
                active_password = False
            # Check if mouse click is inside login button
            if login_button_rect.collidepoint(event.pos):
                print("Login button clicked")
                result = authentication(user_text, password_text)
                if result:
                    print("Login successful")
                    with open('name.txt', 'w') as file:
                        file.write(user_text)
                    subprocess.Popen(["python3", "menu.py"])
                else:
                    print("Incorrect login credentials")
        elif event.type == pygame.KEYDOWN:
            if active_username:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            elif active_password:
                if event.key == pygame.K_BACKSPACE:
                    password_text = password_text[:-1]
                else:
                    password_text += event.unicode

    # Draw background image
    screen.blit(background_image, (0, 0))

    # Draw login button
    draw_button(screen, login_button_rect, GREEN, "Login", WHITE)

    # Draw username input box
    pygame.draw.rect(screen, WHITE, username_rect)  # White background
    username_surface = input_font.render(user_text, True, BLACK)
    screen.blit(username_surface, (username_rect.x + 5, username_rect.y + 10))

    # Draw password input box
    pygame.draw.rect(screen, WHITE, password_rect)  # White background
    password_surface = input_font.render("*" * len(password_text), True, BLACK)  # Display * for password
    screen.blit(password_surface, (password_rect.x + 5, password_rect.y + 10))

    pygame.display.flip()
    clock.tick(60)
