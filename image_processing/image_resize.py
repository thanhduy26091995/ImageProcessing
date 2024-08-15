# pylint: disable=E1101
import cv2
import matplotlib.pyplot as plt

# Load the images
image = cv2.imread('image_processing/images.jpg')
if image is None:
    print("Can't load image")

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Scale factor
SCALE_FACTOR_1 = 3.0
SCALE_FACTOR_2 = 1/3.0

height, width = image_rgb.shape[:2]

# Calculate new image dimensions
new_height = int(height * SCALE_FACTOR_1)
new_width = int(width * SCALE_FACTOR_1)

# Resize image
zoomed_image = cv2.resize(src=image_rgb, dsize=(
    new_width, new_height), interpolation=cv2.INTER_CUBIC)

# Calculate new width and height
new_heigh1 = int(height * SCALE_FACTOR_2)
new_width1 = int(width * SCALE_FACTOR_2)

# Scaled image
scaled_image = cv2.resize(src=image_rgb, dsize=(
    new_width1, new_heigh1), interpolation=cv2.INTER_AREA)

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 4))

# Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image Shape:'+str(image_rgb.shape))

# Plot the Zoomed Image
axs[1].imshow(zoomed_image)
axs[1].set_title('Zoomed Image Shape:'+str(zoomed_image.shape))

# Plot the Scaled Image
axs[2].imshow(scaled_image)
axs[2].set_title('Scaled Image Shape:'+str(scaled_image.shape))

# Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()
