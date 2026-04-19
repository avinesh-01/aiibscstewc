import os
from PIL import Image

INPUT_FOLDER = "ambedkar-jayanti"
OUTPUT_FOLDER = "output_images"
MAX_SIZE_KB = 100
MAX_SIZE_BYTES = MAX_SIZE_KB * 1024

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def compress_image(input_path, output_path):
    img = Image.open(input_path)

    # Convert PNG → JPEG (optional, saves more space)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    quality = 95
    step = 5

    # First resize if very large (helps a lot)
    img.thumbnail((1600, 1600))

    while quality > 10:
        img.save(output_path, format="JPEG", quality=quality, optimize=True)
        
        if os.path.getsize(output_path) <= MAX_SIZE_BYTES:
            break
        
        quality -= step

    # If still too big → reduce dimensions further
    while os.path.getsize(output_path) > MAX_SIZE_BYTES:
        width, height = img.size
        img = img.resize((int(width * 0.9), int(height * 0.9)))
        img.save(output_path, format="JPEG", quality=quality, optimize=True)

for file in os.listdir(INPUT_FOLDER):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(INPUT_FOLDER, file)
        output_path = os.path.join(OUTPUT_FOLDER, file)

        compress_image(input_path, output_path)
        print(f"Compressed: {file}")

print("✅ All images processed under 100KB (approx).")