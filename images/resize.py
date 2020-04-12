from PIL import Image

image = Image.open('ts36.jpg')
#image.show()
new_image = image.thumbnail((600,400))
print(image.size)
print(image.format)
print("done sir!")
image.save('s1.jpg')
