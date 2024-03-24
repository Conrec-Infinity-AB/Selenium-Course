from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:5500/docs/index.html")

sleep(2)

# Maximize the browser window
driver.maximize_window()

sleep(3)
# And minimize it
driver.minimize_window()

sleep(3)
# We can also set the browser in fullscreen (Usually F11 key in browser)
driver.fullscreen_window()

sleep(3)
# We can check the browser window, which dimensions it has
# First exit fullscreen mode
driver.maximize_window()

# Get width and height as an dictionary
size = driver.get_window_size()
print (size)

# Get the individual sizes
width = str(driver.get_window_size().get("width"))
height = str(driver.get_window_size().get("height"))
print ("Width: " + width)
print ("Height: " + height)

sleep(3)
# Set the browser window size. Note it does not change the screen resolution
driver.set_window_size(800, 600)

# Get window positions (x, y values)
# Get X and Y coordinates as an dictionary
position = driver.get_window_position()
print(position)

# Get individual values
xPos = str(driver.get_window_position().get('x'))
yPos = str(driver.get_window_position().get('y'))
print("X pos: " + xPos)
print("Y pos: " + yPos)

# Move the window to a specific position on the primary monitor
driver.set_window_position(500, 500)

# Print the coordinates
position = driver.get_window_position()
print(position)


sleep(3)
driver.quit()
