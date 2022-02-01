from datetime import date, timedelta
   # Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def drawImage():
    # Open an Image
    img = Image.open('/Users/zac/generative nft test/input/page/template.png')

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype('/Users/zac/Downloads/Futura Bold/Futura Bold.otf', 125)

    # Add Text to an image
    I1.text((151, 203), "`single date`", fill=(255, 255, 255))

    # Display edited image
    img.show()

    # Save the edited image
    img.save("`single_date`.png")

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2022, 1, 1)
end_date = date(2022, 1, 7)
for single_date in daterange(start_date, end_date):
    drawImage()