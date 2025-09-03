


window.addEventListener('DOMContentLoaded', () => {
  // Camera preview and download button
  const previewContainer = document.getElementById('polaroid-preview-container');
  const downloadBtn = document.getElementById('download-photo-btn');
  let lastImageBlob = null;

  // Animate polaroid ejection
  function animatePolaroid(imgUrl) {
    previewContainer.innerHTML = '';
    const img = document.createElement('img');
    img.src = imgUrl;
    img.className = 'preview-img polaroid-eject';
    img.style.position = 'absolute';
    img.style.left = '0';
    img.style.top = '-120px';
    img.style.width = '120px';
    img.style.height = '160px';
    img.style.boxShadow = '0 8px 32px #b7651440, 0 0 0 8px #fffbe6';
    img.style.border = '10px solid #fffbe6';
    img.style.borderRadius = '12px';
    img.style.background = '#fffbe6';
    img.style.transition = 'top 1.2s cubic-bezier(.4,0,.2,1), box-shadow 0.3s';
    previewContainer.appendChild(img);
    setTimeout(() => {
      img.style.top = '0';
      img.style.boxShadow = '0 16px 48px #b7651440, 0 0 0 12px #e6b980';
    }, 100);
  }

  // Handle form submit via AJAX
  document.getElementById('photo-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(res => res.blob())
    .then(blob => {
      lastImageBlob = blob;
      const imgUrl = URL.createObjectURL(blob);
      animatePolaroid(imgUrl);
      downloadBtn.style.display = 'block';
      downloadBtn.onclick = () => {
        const a = document.createElement('a');
        a.href = imgUrl;
        a.download = 'vintage_polaroid.jpg';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      };
    });
  });

  // VSCO-inspired: add film grain overlay
  const style = document.createElement('style');
  style.innerHTML = `
    .polaroid-eject::after {
      content: '';
      position: absolute;
      left: 0; top: 0; width: 100%; height: 100%;
      pointer-events: none;
      background: url('https://www.transparenttextures.com/patterns/diamond-upholstery.png');
      opacity: 0.18;
      mix-blend-mode: multiply;
      border-radius: 12px;
    }
  `;
  document.head.appendChild(style);
  const photoInput = document.getElementById('photo-input');
  const captionInput = document.getElementById('caption-input');
  const dateInput = document.getElementById('date-input');
  const filmGrain = document.getElementById('film-grain');
  const lightLeak = document.getElementById('light-leak');
  const bw = document.getElementById('bw');
  const customFileBtn = document.getElementById('custom-file-btn');
  const fileNameSpan = document.getElementById('file-name');
  let photoStripContainer = document.querySelector('.photo-strip');
  let photoStripImages = [];

  customFileBtn.addEventListener('click', function() {
    photoInput.click();
  });

  photoInput.addEventListener('change', (e) => {
    const files = Array.from(e.target.files);
    fileNameSpan.textContent = files.length ? files.map(f => f.name).join(', ') : '';
    photoStripImages = [];
    if (!files.length) {
      renderPhotoStrip();
      return;
    }
    let loaded = 0;
    files.forEach((file, idx) => {
      const reader = new FileReader();
      reader.onload = function(event) {
        // Get effect values
        let filters = [];
        if (bw.checked) filters.push('grayscale(1)');
        if (filmGrain && filmGrain.checked) filters.push('contrast(1.2)');
        if (lightLeak && lightLeak.checked) filters.push('brightness(1.1)');
        photoStripImages.push({
          imgSrc: event.target.result,
          caption: captionInput.value,
          date: dateInput.value,
          filter: filters.join(' ')
        });
        loaded++;
        if (loaded === files.length) {
          renderPhotoStrip();
        }
      };
      reader.readAsDataURL(file);
    });
  });

  function renderPhotoStrip() {
  // ...existing code...
  }
});
