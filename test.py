from datetime import date, timedelta
   # Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def drawImage(single_date):
    # Open an Image
    img = Image.open('assets/template.png')

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype('assets/Futura Bold.otf', 100)

    # Add text for the day and month "Thu 20 Jan."
    I1.text((151, 203), single_date.strftime('%a %d %b.'), fill=(0, 0, 0), font=myFont)
    # Add text for the year "2022"
    I1.text((151, 310), single_date.strftime('%Y'), fill=(0, 0, 0), font=myFont)


    # filename per date to be saved
    output_filename = f"{single_date.strftime('%d-%m-%Y')}.png"

    # Save the edited image
    img.save(f"output_images/{output_filename}")

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)



start_date = date(2022, 1, 1)
end_date = date(2022, 1, 7)
for single_date in daterange(start_date, end_date):
    drawImage(single_date)