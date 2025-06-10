from PIL import Image
import numpy as np
import os

def load_image(path):
    return np.array(Image.open(path))

def save_image(image_np, path):
    Image.fromarray(image_np).save(path)

def flip_image(image_np, horizontal=True, vertical=True):
    if horizontal:
        image_np = np.fliplr(image_np)
    if vertical:
        image_np = np.flipud(image_np)
    return image_np

def add_noise(image_np, noise_range=(-20, 20)):
    noise = np.random.randint(noise_range[0], noise_range[1] + 1, image_np.shape, dtype='int16')
    noisy = np.clip(image_np.astype('int16') + noise, 0, 255).astype('uint8')
    return noisy

def brighten_channels(image_np, channel_increments):
    """
    channel_increments: list or tuple of 3 values for R, G, B (e.g., [40, 0, 0])
    """
    brightened = image_np.copy()
    for i in range(3):  
        brightened[:, :, i] = np.clip(brightened[:, :, i] + channel_increments[i], 0, 255)
    return brightened

def apply_mask(image_np, mask_size=(100, 100), color=(0, 0, 0)):
    masked = image_np.copy()
    h, w = masked.shape[:2]
    cx, cy = w // 2, h // 2
    half_w, half_h = mask_size[0] // 2, mask_size[1] // 2
    masked[cy - half_h:cy + half_h, cx - half_w:cx + half_w] = color
    return masked
input_path = "images/birds.jpg"
image = load_image(input_path)
flipped = flip_image(image)
noisy = add_noise(image)
brightened = brighten_channels(image, [40, 0, 0])  
masked = apply_mask(image, mask_size=(100, 100))

output_dir = "images"
save_image(flipped, os.path.join(output_dir, "birds_flipped.jpg"))
save_image(noisy, os.path.join(output_dir, "birds_noisy.jpg"))
save_image(brightened, os.path.join(output_dir, "birds_brightened.jpg"))
save_image(masked, os.path.join(output_dir, "birds_masked.jpg"))
