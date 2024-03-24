import cv2

# Provide the full path to your JFIF image file
image_path = "sun.jpg"

# Try to read the image
img = cv2.imread(image_path)

# Check if the image is loaded successfully
if img is None:
    print(f"Error: Unable to load JFIF image from {image_path}")

    # Print additional information for troubleshooting
    print(f"OpenCV error: {cv2.imread(image_path, cv2.IMREAD_UNCHANGED)}")
    
    # Exit the program or add additional error handling as needed
    exit()

# Display the original image
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Rotate the image
angle = 45  # specify the rotation angle
rows, cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated_image = cv2.warpAffine(img, rotation_matrix, (cols, rows))

# Display the rotated image
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)

# Flip the image horizontally
flipped_image_horizontal = cv2.flip(img, 1)

# Display the horizontally flipped image
cv2.imshow("Flipped Image (Horizontal)", flipped_image_horizontal)
cv2.waitKey(0)

# Flip the image vertically
flipped_image_vertical = cv2.flip(img, 0)

# Display the vertically flipped image
cv2.imshow("Flipped Image (Vertical)", flipped_image_vertical)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()