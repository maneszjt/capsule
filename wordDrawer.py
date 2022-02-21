# importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

wordsInScript = list()
fileName = "test.txt"

openFile = open(fileName)
for word in openFile.read().split():    
    wordsInScript.append(word)
openFile.close()

def drawImage(word):
    myFont = ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 175)
    
    # open an image
    img = Image.open('base.jpg')

    # call Draw method to add 2D graphics to an image
    I1 = ImageDraw.Draw(img)

    # add text to image
    I1.text((540, 540), word, fill="red")

    # display edited image
    img.show()

    # save the edited image
    img.save(f"./output/{word}.jpg")

for words in wordsInScript:
    drawImage(words)

print("The list of words is: ", wordsInScript)
