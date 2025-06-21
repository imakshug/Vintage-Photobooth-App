function generatePolaroid() {
      const canvas = document.getElementById('previewCanvas');
      const ctx = canvas.getContext('2d');
      const file = document.getElementById('imageUpload').files[0];
      const caption = document.getElementById('caption').value;
      const date = document.getElementById('date').value || new Date().toLocaleDateString();
      const theme = document.getElementById('theme').value;

      if (!file) {
        alert("Please upload an image.");
        return;
      }

      const reader = new FileReader();

      reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
          // Clear canvas
          ctx.clearRect(0, 0, canvas.width, canvas.height);

          const frameColor = theme === 'black' ? '#000' : '#fff';
          const textColor = theme === 'black' ? '#fff' : '#000';

          // Draw polaroid frame
          ctx.fillStyle = frameColor;
          ctx.fillRect(0, 0, canvas.width, canvas.height);

          // Draw image
          const imgWidth = 460;
          const imgHeight = 460;
          ctx.drawImage(img, 20, 20, imgWidth, imgHeight);

          // Draw caption
          ctx.fillStyle = textColor;
          ctx.font = "20px 'Playfair Display', serif";
          ctx.textAlign = "center";
          ctx.fillText(caption, canvas.width / 2, 520);

          // Draw date
          ctx.font = "16px 'Playfair Display', serif";
          ctx.fillText(date, canvas.width / 2, 550);
        };
        img.src = e.target.result;
      };

      reader.readAsDataURL(file);
    }