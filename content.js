// Get all images on the page
const images = document.querySelectorAll('img');

// Loop through each image
images.forEach((img, index) => {
  // If the image has alt text
  if (img.alt) {
    // Use SpeechSynthesis API to read the alt text
    const utterance = new SpeechSynthesisUtterance(`Image ${index + 1} description: ${img.alt}`);
    speechSynthesis.speak(utterance);
  } else {
    // If no alt text, read fallback message
    const utterance = new SpeechSynthesisUtterance(`Image ${index + 1} does not have a description`);
    speechSynthesis.speak(utterance);
  }
});

