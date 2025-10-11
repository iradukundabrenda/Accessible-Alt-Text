// Select all images on the page
const images = document.querySelectorAll('img');

// Loop through each image and add click behavior
images.forEach((img, index) => {
  img.addEventListener('click', async () => {
    const imageUrl = img.src;

    try {
      // Send image URL to your Flask backend
      const response = await fetch('http://127.0.0.1:5000/generate-alt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image_url: imageUrl })
      });

      const data = await response.json();

      // Speak and display generated alt text
      if (data.alt_text) {
        alert(`Description for image ${index + 1}: ${data.alt_text}`);
        const utterance = new SpeechSynthesisUtterance(data.alt_text);
        window.speechSynthesis.speak(utterance);
      } else {
        alert(`Image ${index + 1}: No description generated.`);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('⚠️ Could not connect to the Flask app. Make sure it is running.');
    }
  });
});

