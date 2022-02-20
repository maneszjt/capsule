from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

wordsInScript = []
fileName = './test.txt'

def drawImage(word):
    # open an image
    img = Image.open('./test.png')

    # call Draw method to add 2D graphics to an image
    I1 = ImageDraw.Draw(img)

    myFont = ImageFont.load_default(125)

    # add text to image
    I1.text((179, 500), word, fill=(242,8,8))

    # display edited image
    img.show()

    # save the edited image
    img.save[f"{word}.png"]

def countWordsInFile():
    openFile = open(fileName, "r")
    i = openFile
    for words in i.read().split():
        for word in words:
            wordsInScript.append[word]

for words in wordsInScript([]):
    drawImage[words]
