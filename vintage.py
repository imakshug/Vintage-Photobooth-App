import random
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os
import subprocess
from datetime import datetime
from PIL import ImageEnhance

VINTAGE_COLOR_LEVELS = {
    'r': [0, 0, 0, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 17, 18, 19, 19, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 45, 47, 48, 49, 52, 54, 55, 57, 59, 60, 62, 65, 67, 69, 70, 72, 74, 77, 79, 81, 83, 86, 88, 90, 92, 94, 97, 99, 101, 103, 107, 109, 111, 112, 116, 118, 120, 124, 126, 127, 129, 133, 135, 136, 140, 142, 143, 145, 149, 150, 152, 155, 157, 159, 162, 163, 165, 167, 170, 171, 173, 176, 177, 178, 180, 183, 184, 185, 188, 189, 190, 192, 194, 195, 196, 198, 200, 201, 202, 203, 204, 206, 207, 208, 209, 211, 212, 213, 214, 215, 216, 218, 219, 219, 220, 221, 222, 223, 224, 225, 226, 227, 227, 228, 229, 229, 230, 231, 232, 232, 233, 234, 234, 235, 236, 236, 237, 238, 238, 239, 239, 240, 241, 241, 242, 242, 243, 244, 244, 245, 245, 245, 246, 247, 247, 248, 248, 249, 249, 249, 250, 251, 251, 252, 252, 252, 253, 254, 254, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    'g' : [0, 0, 1, 2, 2, 3, 5, 5, 6, 7, 8, 8, 10, 11, 11, 12, 13, 15, 15, 16, 17, 18, 18, 19, 21, 22, 22, 23, 24, 26, 26, 27, 28, 29, 31, 31, 32, 33, 34, 35, 35, 37, 38, 39, 40, 41, 43, 44, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 83, 84, 85, 86, 88, 89, 90, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 105, 106, 107, 108, 109, 111, 113, 114, 115, 117, 118, 119, 120, 122, 123, 124, 126, 127, 128, 129, 131, 132, 133, 135, 136, 137, 138, 140, 141, 142, 144, 145, 146, 148, 149, 150, 151, 153, 154, 155, 157, 158, 159, 160, 162, 163, 164, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 181, 182, 183, 184, 186, 186, 187, 188, 189, 190, 192, 193, 194, 195, 195, 196, 197, 199, 200, 201, 202, 202, 203, 204, 205, 206, 207, 208, 208, 209, 210, 211, 212, 213, 214, 214, 215, 216, 217, 218, 219, 219, 220, 221, 222, 223, 223, 224, 225, 226, 226, 227, 228, 228, 229, 230, 231, 232, 232, 232, 233, 234, 235, 235, 236, 236, 237, 238, 238, 239, 239, 240, 240, 241, 242, 242, 242, 243, 244, 245, 245, 246, 246, 247, 247, 248, 249, 249, 249, 250, 251, 251, 252, 252, 252, 253, 254, 255],
    'b' : [53, 53, 53, 54, 54, 54, 55, 55, 55, 56, 57, 57, 57, 58, 58, 58, 59, 59, 59, 60, 61, 61, 61, 62, 62, 63, 63, 63, 64, 65, 65, 65, 66, 66, 67, 67, 67, 68, 69, 69, 69, 70, 70, 71, 71, 72, 73, 73, 73, 74, 74, 75, 75, 76, 77, 77, 78, 78, 79, 79, 80, 81, 81, 82, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 89, 89, 90, 90, 91, 91, 93, 93, 94, 94, 95, 95, 96, 97, 98, 98, 99, 99, 100, 101, 102, 102, 103, 104, 105, 105, 106, 106, 107, 108, 109, 109, 110, 111, 111, 112, 113, 114, 114, 115, 116, 117, 117, 118, 119, 119, 121, 121, 122, 122, 123, 124, 125, 126, 126, 127, 128, 129, 129, 130, 131, 132, 132, 133, 134, 134, 135, 136, 137, 137, 138, 139, 140, 140, 141, 142, 142, 143, 144, 145, 145, 146, 146, 148, 148, 149, 149, 150, 151, 152, 152, 153, 153, 154, 155, 156, 156, 157, 157, 158, 159, 160, 160, 161, 161, 162, 162, 163, 164, 164, 165, 165, 166, 166, 167, 168, 168, 169, 169, 170, 170, 171, 172, 172, 173, 173, 174, 174, 175, 176, 176, 177, 177, 177, 178, 178, 179, 180, 180, 181, 181, 181, 182, 182, 183, 184, 184, 184, 185, 185, 186, 186, 186, 187, 188, 188, 188, 189, 189, 189, 190, 190, 191, 191, 192, 192, 193, 193, 193, 194, 194, 194, 195, 196, 196, 196, 197, 197, 197, 198, 199]
    }  # (same dictionary, truncated for brevity)

def apply_vintage_effect(image):
    # Convert to RGB just in case
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Apply sepia filter
    width, height = image.size
    pixels = image.load()

    for py in range(height):
        for px in range(width):
            r, g, b = pixels[px, py]

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            pixels[px, py] = (
                min(255, tr),
                min(255, tg),
                min(255, tb)
            )

    # Slightly reduce saturation
    converter = ImageEnhance.Color(image)
    image = converter.enhance(0.9)

    # Slightly increase contrast
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(1.2)

    return image

def modify_all_pixels(im, pixel_callback):
    width, height = im.size
    pxls = im.load()
    for x in range(width):
        for y in range(height):
            pxls[x, y] = pixel_callback(x, y, *pxls[x, y])

def vintage_colors(im, color_map=VINTAGE_COLOR_LEVELS):
    r_map = color_map['r']
    g_map = color_map['g']
    b_map = color_map['b']
    def adjust_levels(x, y, r, g, b):
        return r_map[r], g_map[g], b_map[b]
    modify_all_pixels(im, adjust_levels)
    return im

def add_noise(im, noise_level=20):
    def pixel_noise(x, y, r, g, b):
        noise = random.randint(0, noise_level) - noise_level // 2
        return tuple(max(0, min(c + noise, 255)) for c in (r, g, b))
    modify_all_pixels(im, pixel_noise)
    return im

def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    return file_path
def add_polaroid_frame(image, message="My Polaroid 📸", date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    width, height = image.size
    border_top = int(height * 0.05)
    border_sides = int(width * 0.05)
    border_bottom = int(height * 0.25)

    new_width = width + border_sides * 2
    new_height = height + border_top + border_bottom

    framed = Image.new('RGB', (new_width, new_height), color='white')
    framed.paste(image, (border_sides, border_top))

    draw = ImageDraw.Draw(framed)

    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    text_x = new_width // 2
    text_y = height + border_top + 10

    draw.text((text_x, text_y), message, fill="black", font=font, anchor="mm")
    draw.text((text_x, text_y + 30), date, fill="gray", font=font, anchor="mm")

    return framed

def get_next_filename(export_dir, base_name="photo", ext=".jpg"):
    i = 1
    while True:
        filename = f"{base_name}_{i:03d}{ext}"
        full_path = os.path.join(export_dir, filename)
        if not os.path.exists(full_path):
            return full_path
        i += 1

# Main Execution
if __name__ == '__main__':
    filename = select_image_file()
    if not filename:
        print("No file selected. Exiting.")
        exit()

    try:
        image = Image.open(filename)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Apply improved vintage effect and noise
        image = apply_vintage_effect(image)
        image = add_noise(image)

        # Get user input for message and date
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        message = tk.simpledialog.askstring("Polaroid Message", "Enter a short caption:", initialvalue="My Polaroid 📸"
                                            ) or "My Polaroid 📸"
        date = tk.simpledialog.askstring("Date (optional)", "Enter a date (or leave blank for today):")
        if not date:
            date = datetime.now().strftime("%d %b %Y")
        else:
            try:
                date = datetime.strptime(date, "%d %b %Y").strftime("%d %b %Y")
            except ValueError:
                print("Invalid date format. Using today's date instead.")
                date = datetime.now().strftime("%d %b %Y")

        root.destroy()  # Close the dialog window
        # Add Polaroid frame with message and date
 
        print(f"📸 Adding Polaroid frame with message: '{message}' and date: '{date}'")
        image = vintage_colors(image)
        image = add_noise(image, noise_level=20)
        image = add_polaroid_frame(image, message=message, date=date)
        print("✅ Vintage effects applied successfully.")
        
        final_image = add_polaroid_frame(image, message=message, date=date)

        # Save to export directory
        export_dir = r"D:\Vintage Photobooth App\exports"
        os.makedirs(export_dir, exist_ok=True)

        def get_next_filename(base_name="photo", ext=".jpg"):
            i = 1
            while True:
                filename = f"{base_name}_{i:03d}{ext}"
                full_path = os.path.join(export_dir, filename)
                if not os.path.exists(full_path):
                    return full_path
                i += 1

        final_path = get_next_filename()
        final_image.save(final_path)
        print(f"\n✅ Saved Polaroid image to: {final_path}")

        try:
            subprocess.Popen(f'explorer "{export_dir}"')
        except Exception as e:
            print(f"⚠ Could not open folder: {e}")

    except Exception as e:
        print(f"❌ Error processing image: {e}")