import time
import datetime

from selenium import webdriver

# path of downloaded exe for chromedriver
driver = webdriver.Chrome(r"C:\Users\user\.wdm\drivers\chromedriver\win32\98.0.4758.80\chromedriver.exe") 

driver.get('http://127.0.0.1:5000/')

file = r"C:\Users\Guy\Desktop\hey.txt"

def interact(data):
    time.sleep(1) # Let the user actually see something!

    hash_box = driver.find_element_by_name('hash')

    hash_box.send_keys(str(data))

    # Find login button
    submit_button = driver.find_element_by_name('enter')

    # Click login
    submit_button.click()

    time.sleep(1) # Let the user actually see something!

    #driver.quit()

def read_in_chunks(file_object, chunk_size=32):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

a = datetime.datetime.now()
with open(file, 'rb') as f:
    for piece in read_in_chunks(f):
        interact(piece)

driver.quit()
b = datetime.datetime.now()
print(b-a)
