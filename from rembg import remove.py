from rembg import remove
from PIL import Image

# Step 1: Load your image
input_path = "C:/Users/Abu Junaid/Desktop/python/output/d.png "  # Replace with your image filename
output_path = "C:/Users/Abu Junaid\Desktop/python/output.png"   # Output will be saved as PNG with transparent background

# Step 2: Open the image file
with open(input_path, "rb") as inp_file:
    input_data = inp_file.read()

# Step 3: Remove background
output_data = remove(input_data)

# Step 4: Save the new image
with open(output_path, "wb") as out_file:
    out_file.write(output_data)

print("Background removed! Saved as", output_path)

