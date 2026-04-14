from PIL import Image, ImageFilter

img  = Image.open("images/buz.jpg")

print(img)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("blur.png", 'png')

# converted_img = img.convert("L")
# converted_img.save("conv.png", 'png')

# keep the aspect ratio with max value
img.thumbnail((400,400))
img.save("thumbnail.jpg")