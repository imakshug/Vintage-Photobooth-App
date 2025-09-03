from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import io
import datetime
from vintagephoto import process_image as process_image_fn  # Your main image processing logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('photo')
    if not files or files == [None]:
        files = request.files.getlist('photo[]')
    caption = request.form.get('caption', '')
    date_text = request.form.get('date', '')
    film_grain = request.form.get('film_grain') == 'on'
    light_leak = request.form.get('light_leak') == 'on'
    bw = request.form.get('bw') == 'on'

    if not date_text:
        date_text = datetime.datetime.now().strftime("%d %b %Y")

    def create_polaroid_strip(images, caption, date_text):
        # All images should be the same size
        widths, heights = zip(*(img.size for img in images))
        strip_width = max(widths)
        margin = 0  # px between polaroids (no gap, fully tight layout)
        strip_height = sum(heights) + margin * (len(images) - 1)
        extra_caption_height = int(strip_width * 0.18)
        strip_img = Image.new('RGB', (strip_width, strip_height + extra_caption_height), (255, 255, 255))
        y_offset = 0
        for img in images:
            strip_img.paste(img, (0, y_offset))
            y_offset += img.size[1] + margin
        # Draw caption/date at the bottom
        from PIL import ImageDraw, ImageFont
        draw = ImageDraw.Draw(strip_img)
        font_size = int(strip_width * 0.045)
        try:
            font_path = os.path.join(os.path.dirname(__file__), "PlayfairDisplay-Italic-VariableFont_wght.ttf")
            font = ImageFont.truetype(font_path, font_size)
        except Exception:
            font = ImageFont.load_default()
        caption_text = caption.strip()
        date_text = date_text.strip()
        # Move caption up so it's visible above the bottom edge
        caption_y = strip_height + int(font_size * 0.5) - int(font_size * 4.2)
        if caption_text:
            caption_w = draw.textlength(caption_text, font=font)
            draw.text(((strip_width - caption_w) // 2, caption_y), caption_text, font=font, fill="#b76514")
            caption_y += font_size + 10
        if date_text:
            date_w = draw.textlength(date_text, font=font)
            draw.text(((strip_width - date_w) // 2, caption_y), date_text, font=font, fill="#b76514")
        return strip_img

    outputs = []
    polaroid_images = []
    try:
        for file in files:
            if not file:
                continue
            image = Image.open(file.stream)
            # Apply effects based on checkboxes
            if bw:
                image = image.convert('L').convert('RGB')
            if film_grain:
                from PIL import ImageFilter
                image = image.filter(ImageFilter.GaussianBlur(1))
            if light_leak:
                from PIL import ImageEnhance
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(1.1)
            polaroid_images.append(process_image_fn(image, '', ''))

        # If only one image, add caption/date to the single polaroid
        if len(polaroid_images) == 1:
            single_img = polaroid_images[0]
            # Draw caption/date at the bottom of the single image
            from PIL import ImageDraw, ImageFont
            width, height = single_img.size
            font_size = int(width * 0.045)
            try:
                font_path = os.path.join(os.path.dirname(__file__), "PlayfairDisplay-Italic-VariableFont_wght.ttf")
                font = ImageFont.truetype(font_path, font_size)
            except Exception:
                font = ImageFont.load_default()
            draw = ImageDraw.Draw(single_img)
            caption_text = caption.strip()
            date_text = date_text.strip()
            # Move caption up so it's visible above the bottom edge
            caption_y = height - int(font_size * 4.2)
            if caption_text:
                caption_w = draw.textlength(caption_text, font=font)
                draw.text(((width - caption_w) // 2, caption_y), caption_text, font=font, fill="#b76514")
                caption_y += font_size + 10
            if date_text:
                date_w = draw.textlength(date_text, font=font)
                draw.text(((width - date_w) // 2, caption_y), date_text, font=font, fill="#b76514")
            output = io.BytesIO()
            single_img.save(output, format='JPEG')
            output.seek(0)
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'vintage_photo_{timestamp}.jpg'
            return send_file(
                output,
                mimetype='image/jpeg',
                as_attachment=True,
                download_name=filename
            )
        # If multiple, create a photo strip with one caption at the bottom
        if len(polaroid_images) > 1:
            strip_img = create_polaroid_strip(polaroid_images, caption, date_text)
            strip_output = io.BytesIO()
            strip_img.save(strip_output, format='JPEG')
            strip_output.seek(0)
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            strip_filename = f'vintage_photo_strip_{timestamp}.jpg'
            return send_file(
                strip_output,
                mimetype='image/jpeg',
                as_attachment=True,
                download_name=strip_filename
            )
        # Fallback: zip if something goes wrong
        import zipfile
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zipf:
            for out, fname in outputs:
                zipf.writestr(fname, out.getvalue())
        zip_buffer.seek(0)
        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='vintage_photos.zip'
        )
    except Exception as e:
        return f"Error processing image: {e}", 500

    
if __name__ == '__main__':
    app.run(debug=True)
