from datetime import date, timedelta
   # Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

   # notes to tomer
   # so i imagine the training part of the process would go here

def drawImage(single_date):
    # and then i imagine the generative part (one image at a time) would go here
    # not sure how to do that and i'm not certain exactly how the python would be split
    # i imagine there would need to be a solid training cycle — 100 images at, say, 50 epochs each
    # or alternatively we could do decades — feed it, like, magazine pics or film posters or whatever from the 70s for the 70s and so on
    # the upscale 4x in Looking Glass v1.3 would get the output to 1024 but the template.png is 1080x1080 but i suppose that's more fixable in the template
    # i'm open to doing a series of batch runs rather than one individual run
    # eg. do the 70s, then the 80s, then the 90s, then the 00s, then the 10s, then the 20s to, like, the end of this year for each of the days
    # i thought this would be a generative process upon mint but i suspect it will actually be easier to precreate the image assets
    # and then we just pull 'today's' NFT from an array, or something, to bid upon
    # based off a Nouns fork — https://nouns.notion.site/Explore-Nouns-a2a9dceeb1d54e10b9cbf3f931c2266f
   
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
