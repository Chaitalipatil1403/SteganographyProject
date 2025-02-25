
import cv2
import os

# Load the image
img = cv2.imread("mypic.jpg")

if img is None:
    raise FileNotFoundError("Image not found. Check the file path.")

height, width, _ = img.shape

# Input message and password
msg = input("Enter secret message: ") + '\0'  # Append a null character at the end
password = input("Enter password: ")

# Create ASCII mappings
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

n, m, z = 0, 0, 0

# Encryption: Store ASCII values in image pixels
for char in msg:
    img[n, m, z] = d[char]
    
    # Move to the next pixel position
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1
            if n >= height:
                raise ValueError("Message too long for the image.")

# Save the encrypted image in PNG format to prevent compression artifacts
cv2.imwrite("Encryptedmsg.png", img)
os.system("start Encryptedmsg.png")

print("Message encrypted successfully!")
