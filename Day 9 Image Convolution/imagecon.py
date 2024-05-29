import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def load_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=1)  # Load image and convert to grayscale
    image = tf.image.convert_image_dtype(image, tf.float32)  # Convert to float32
    image = tf.squeeze(image)  # Remove the single channel dimension
    return image.numpy()  # Convert to NumPy array

def normalize(img):
    img = img - np.mean(img)
    img = img / np.std(img)
    return img

def convolve2d(image, kernel):
    output = np.zeros_like(image)
    image_padded = np.pad(image, [
        (kernel.shape[0] // 2, kernel.shape[0] // 2),
        (kernel.shape[1] // 2, kernel.shape[1] // 2)
    ], mode='constant', constant_values=0)

    for x in range(image.shape[1]):     # Loop over every pixel of the image
        for y in range(image.shape[0]):
            output[y, x] = (kernel * image_padded[y:y+kernel.shape[0], x:x+kernel.shape[1]]).sum()
    
    return output

# Load the full image and the cropped part
full_image_path = '/mnt/data/full_image.jpg'
cropped_part_path = '/mnt/data/cropped_part.jpg'
full_image = load_image(full_image_path)
cropped_part = load_image(cropped_part_path)

# Normalize the images
full_image_normalized = normalize(full_image)
cropped_part_normalized = normalize(cropped_part)

# Perform 2D convolution
convolution_result = convolve2d(full_image_normalized, cropped_part_normalized)

# Find the position of the highest value in the convolution result
y, x = np.unravel_index(np.argmax(convolution_result), convolution_result.shape)

# The top-left corner of the matching region in the full image
top_left = (x, y)
# The bottom-right corner of the matching region in the full image
bottom_right = (x + cropped_part.shape[1], y + cropped_part.shape[0])

# Draw a rectangle around the matched region (optional)
matched_image = np.stack([full_image] * 3, axis=-1)  # Convert grayscale to RGB for visualization
matched_image = matched_image.astype(np.uint8)
matched_image[y:bottom_right[1], x] = [0, 255, 0]
matched_image[y:bottom_right[1], bottom_right[0]] = [0, 255, 0]
matched_image[y, x:bottom_right[0]] = [0, 255, 0]
matched_image[bottom_right[1], x:bottom_right[0]] = [0, 255, 0]

# Show the result
plt.subplot(121), plt.imshow(full_image, cmap='gray'), plt.title('Full Image')
plt.subplot(122), plt.imshow(matched_image), plt.title('Detected Match')
plt.show()

# Return the position of the cropped part
(top_left, bottom_right)
