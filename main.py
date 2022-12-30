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

cv2.namedWindow("frame", 1)
camera = cv2.VideoCapture(0)

# Set the font and color
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 0, 255)  # Blue

# Define the size of the region and the position of its top-left corner
width = 650
height = 650
x = 400
y = 400

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # blur image
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Otsu's threshold to binarize the image
    # threshold, _ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    # specify the roi (region of interest)
    #roi = threshold[y:y + height, x:x + width]

    # frame = cv2.resize(frame, None, fx=1, fy=1)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform text extraction
    text = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
    # text = text.replace('\n', '').replace('\f', '')

    cv2.putText(invert, text, (200, 200), font, 2, color, 2)

    # Display the frame along with the tesseract output
    cv2.imshow("Frame", thresh)
    cv2.imshow("Frame", opening)
    cv2.imshow("Frame", invert)

    key = cv2.waitKey(1)  # this must be 1 not 0
    if key == ord("p"):  # Press "p" to take a photo
        # Get the current time
        now = datetime.datetime.now()

        # Construct the file name using the current time
        file_name = now.strftime("H%M%S") + ".png"

        # Save the photo with the timestamp as the file name
        cv2.imwrite(file_name, invert)

    if key == ord("q"):  # Press "q" to quit
        break

camera.release()
cv2.destroyAllWindows()



'''
"extract text from snapshot"

from PIL import Image
from pytesseract import pytesseract


# and the image we would be using
image_path = "/Users/ygeorgas/mtgchk/card1.png"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
#pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img, config='--psm 6')
#text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text)
#print(text.replace('\n', '').replace('\f', ''))

#print(text[:-1])

'''
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
