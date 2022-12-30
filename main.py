""" MTG card price finder, this is a program made of 3 steps.
Step 1 you place the MTG card in front of the laptop camera and take a snapshot that captures only the name of the card
Step 2 the program uses image to text to take the card name from the image and turn it into a string (text)
Step 3 the program calls the eBay API to check the price of the MTG card (using the text) and returns the top 10 prices
then its up to you if you feel that the card worth your time to sell it on eBay
(perhaps feed only uncommon, rare and gold cards - not common)
"""

# import requests
# import json

"take a snapshot using your laptop camera"

import cv2
# import time
import datetime
from pytesseract import pytesseract
from PIL import Image

cv2.namedWindow("frame", 1)
camera = cv2.VideoCapture(0)

# Set the font and color for text and roi rectangular
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 0, 255)  # red due to BGR default type of image from openCV

# Define the size of the roi w x h
width = 450
height = 450
# and the position of text on the screen measuring from the top-left of the screen
y = 100  # distance from top of screen
x = 250  # distance from left of screen

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Convert the image to grayscale
    # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Convert the image from BGR to RGB
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # blur image (to increase accuracy)
    # blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Otsu's threshold to binarize the image
    # threshold, _ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)
    # invert = 255 - opening

    # frame = cv2.resize(frame, None, fx=1, fy=1)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Draw a rectangle on the image
    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
    # specify the roi (region of interest)
    roi = frame[y: y+height, x: x+width]

    # Perform text extraction
    text = pytesseract.image_to_string(roi, lang='eng', config='--psm 6')
    # text = text.replace('\n', '').replace('\f', '')

    # this command places text on the frame at the position of x & y
    cv2.putText(frame, text, ((y+width), (x+height)), font, 2, color, 2)

    # Display the frame along with the tesseract output
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)  # this must be 1 not 0
    if key == ord("p"):  # Press "p" to take a photo
        # Get the current time
        now = datetime.datetime.now()

        # Construct the file name using the current time
        file_name = now.strftime("H%M%S") + ".png"

        # Save the photo with the timestamp as the file name
        cv2.imwrite(file_name, roi)

        # Opening the image & storing it in an image object
        image_path = '/Users/ygeorgas/mtgchk/'+file_name
        img = Image.open(image_path)

        # Passing the image object to image_to_string() function
        img_text = pytesseract.image_to_string(img, config='--psm 6')
        # text = pytesseract.image_to_string(img_text)

        # Split the string into lines
        # lines = img_text.split('\n')
        # Print the first line
        # print(lines[0], lines[1])
        # print the whole text
        print(img_text)
        # print(text.replace('\n', '').replace('\f', ''))
        # print(text[:-1])

    if key == ord("q"):  # Press "q" to quit
        break

camera.release()
cv2.destroyAllWindows()

'''
# eBAY check price of MTG card

# Set the API endpoint URL and the API key
endpoint_url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
api_key = "YOUR_API_KEY_HERE"

# Set the search parameters
parameters = {
    "q": text,  # search for items with the keyword "iphone"
    "limit": 10,  # retrieve up to 10 items
    "sort": "currentPrice",  # sort the results by current price
}

# Set the headers for the API request
headers = {
    "Authorization": f"Bearer {api_key}",  # include the API key in the authorization header
    "Content-Type": "application/json",  # set the content type to JSON
}

# Send the API request and retrieve the response
response = requests.get(endpoint_url, params=parameters, headers=headers)

# Check the status code to see if the request was successful
if response.status_code == 200:
    # If the request was successful, parse the JSON data
    data = response.json()
    # Iterate through the items in the response and print their prices
    for item in data["itemSummaries"]:
        print(f"Item: {item['title']}, Price:")
'''
