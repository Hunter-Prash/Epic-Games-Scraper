from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import datetime

def get_free_games():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.epicgames.com/store/en-US/free-games")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-2u323'))
        )
        
        games = []
        elements = driver.find_elements(By.CLASS_NAME, 'css-n446gb')
        
        for element in elements:
            game_link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            games.append(f"{game_link}")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    driver.quit()
    
    # Extract the game's name from the URL
    final_list=[]
    for i in games:
        temp=[]
        temp=i.split('/')
        final_list.append(temp[-1])
    
    return final_list

print(get_free_games())



def save_to_file(games_list, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write("FREE GAMES THIS WEEK:\n\n")
            for i in games_list:
                file.write(f"{i}\n")
        print(f"Games list saved to {file_path}")
    except OSError as e:
        print(f"Error saving file: {e}")

# Define the file path 
file_name = "free-games-list.txt"
# Update this to the correct Google Drive path
google_drive_folder = "G:\\My Drive"  # Folder path
file_path = os.path.join(google_drive_folder, file_name)

games = get_free_games()
save_to_file(games, file_path)


test_file=open(r'C:\Users\pctec\OneDrive\Desktop\Python Script\test.txt','a')
test_file.write(f'{datetime.time}-The script ran \n')