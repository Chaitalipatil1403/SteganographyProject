import cv2

def decrypt_message(image_path, password):
    # Load the encrypted image
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError("Error: Unable to load the image. Check the file path.")

    height, width, _ = img.shape

    # Create ASCII mapping
    c = {i: chr(i) for i in range(256)}

    # Get the passcode from the user
    pas = input("Enter passcode for Decryption: ")

    if password != pas:
        print("Not a valid key. Access Denied.")
        return

    message = ""
    n, m, z = 0, 0, 0

    while n < height:
        char_code = int(img[n, m, z])  # Extract ASCII value
        if char_code == 0:  # Stop if null character is reached
            break
        message += c.get(char_code, '?')  # Convert ASCII to character

        # Move to the next pixel position
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= width:
                m = 0
                n += 1

    print("Decrypted message:", message)

# Example usage
decrypt_message("Encryptedmsg.png", "123")
