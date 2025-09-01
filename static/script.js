


window.addEventListener('DOMContentLoaded', () => {
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
    photoStripContainer.innerHTML = '';
    photoStripImages.forEach(({ imgSrc, caption, date, filter }) => {
      const frame = document.createElement('div');
      frame.className = 'polaroid-frame';
      const img = document.createElement('img');
      img.className = 'preview-img';
      img.src = imgSrc;
      if (filter) img.style.filter = filter;
      frame.appendChild(img);
      const captionDiv = document.createElement('div');
      captionDiv.className = 'polaroid-caption';
      captionDiv.style.fontSize = '1.3rem';
      captionDiv.style.fontFamily = 'Playfair Display, serif';
      captionDiv.style.fontWeight = '700';
      captionDiv.style.color = '#b76514';
      captionDiv.style.background = 'rgba(255,255,255,0.85)';
      captionDiv.style.borderRadius = '10px';
      captionDiv.style.padding = '6px 16px';
      captionDiv.style.boxShadow = '0 2px 8px #b7651440';
      captionDiv.innerHTML = `${caption ? `<p>${caption}</p>` : ''}${date ? `<p>${date}</p>` : ''}`;
      frame.appendChild(captionDiv);
      photoStripContainer.appendChild(frame);
    });
  }
});
