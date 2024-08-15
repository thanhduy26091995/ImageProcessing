# pylint: disable=E1101
import cv2
import matplotlib.pyplot as plt

# Read the images
img = cv2.imread("image_processing/images.jpg")
if img is None:
    print("No image found")

# Convert BGR to RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Image rotation parameter
center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)
ANGLE = -90
SCALE = 1

# Get roration matrix 2D creates a matrix needed for transformation
rotation_matrix = cv2.getRotationMatrix2D(center, ANGLE, SCALE)

rotation_image = cv2.warpAffine(
    image_rgb, rotation_matrix, (img.shape[1], img.shape[0]))

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(7, 4))

# Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')

# Plot the Rotated image
axs[1].imshow(rotation_image)
axs[1].set_title('Image Rotation')

# Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()
