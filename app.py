from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import io
import datetime
from vintagephoto import process_image  # Your main image processing logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['photo']
    caption = request.form.get('caption', '')
    date_text = request.form.get('date', '')

    if not date_text:
        date_text = datetime.datetime.now().strftime("%d %b %Y")

    try:
        image = Image.open(file.stream)
        processed_image = process_image(image, caption, date_text)

        output = io.BytesIO()
        processed_image.save(output, format='JPEG')
        output.seek(0)

        return send_file(
            output,
            mimetype='image/jpeg',
            as_attachment=True,
            download_name='vintage_photo.jpg'
        )
    except Exception as e:
        return f"Error processing image: {e}", 500

@app.route('/process', methods=['POST'])
def process_image():
    try:
        file = request.files['image']
        image = Image.open(file.stream).convert('RGB')

        # Your image logic goes here
        # e.g. apply_vintage_filter(image)

        output = io.BytesIO()
        image.save(output, format='JPEG')
        output.seek(0)

        return send_file(output, mimetype='image/jpeg')
    except Exception as e:
        return f"Error: {e}", 500
    
if __name__ == '__main__':
    app.run(debug=True)
