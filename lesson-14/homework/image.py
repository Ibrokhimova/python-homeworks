from PIL import Image
import numpy as np
import os
img_path = "images/birds.jpg"
image = Image.open(img_path)
image_np = np.array(image)
flipped_h = np.fliplr(image_np)
flipped_v = np.flipud(image_np)
flipped_both = np.flipud(np.fliplr(image_np))
noise = np.random.randint(-20, 21, image_np.shape, dtype='int16')
noisy_image = np.clip(image_np.astype('int16') + noise, 0, 255).astype('uint8')
brightened = image_np.copy()
brightened[:, :, 0] = np.clip(brightened[:, :, 0] + 40, 0, 255)

masked = image_np.copy()
h, w = image_np.shape[:2]
center_x, center_y = w // 2, h // 2
half_size = 50  
masked[center_y - half_size:center_y + half_size,
       center_x - half_size:center_x + half_size] = [0, 0, 0]

Image.fromarray(flipped_both).save("images/birds_flipped.jpg")
Image.fromarray(noisy_image).save("images/birds_noisy.jpg")
Image.fromarray(brightened).save("images/birds_brightened.jpg")
Image.fromarray(masked).save("images/birds_masked.jpg")
