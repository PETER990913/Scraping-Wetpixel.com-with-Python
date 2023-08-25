from PIL import Image
image_paths = ["image1.jpg", "image2.jpg", ..., "image20.jpg"]  
images = [Image.open(path) for path in image_paths]
widths, heights = zip(*(img.size for img in images))
# max_width = max(widths)
# total_height = sum(heights)
# combined_image = Image.new("RGB", (max_width, total_height))
# y_offset = 0
# for img in images:
#     combined_image.paste(img, (0, y_offset))
#     y_offset += img.size[1]
# combined_image.save("combined_image.jpg")  # Replace with the desired output file path and format
max_width = sum(img.width for img in images)
max_height = max(img.height for img in images)
combined_image = Image.new("RGB", (max_width, max_height))
x_offset = 0
for img in images:
    combined_image.paste(img, (x_offset, 0))
    x_offset += img.width
combined_image.save("combined_image.bmp")