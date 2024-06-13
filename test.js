
function readURL(input) {
    const fileLabel = document.querySelector('.file-label');
    const fileNamePlaceholder = document.getElementById('file-name-placeholder');
  
    if (input.files && input.files[0]) {
      fileLabel.textContent = 'Choose File';
      fileNamePlaceholder.textContent = input.files[0].name;
    } else {
      fileNamePlaceholder.textContent = 'No file chosen';
    }
  }

//  For download button
document.addEventListener('DOMContentLoaded', () => {
   // Get the download button element
  const downloadButton = document.getElementById('downloadButton');
  const extractedTextElement = document.querySelector('.output');

  // Add a click event listener to the download button
  downloadButton.addEventListener('click', () => {
      const extractedText = extractedTextElement.textContent;

      // Create a Blob with the extracted text
      const blob = new Blob([extractedText], { type: 'text/plain' });

      // Create a URL for the Blob
      const url = URL.createObjectURL(blob);

      // Create a temporary link element
      const link = document.createElement('a');
      link.href = url;
      link.download = 'extracted_text.txt'; // File name for download

      // Append the link to the body and trigger the download
      document.body.appendChild(link);
      link.click();

      // Clean up
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
  });
});



function readURL(input) {
  const fileLabel = document.querySelector('.file-label');
  const fileNamePlaceholder = document.getElementById('file-name-placeholder');

  if (input.files && input.files[0]) {
    fileLabel.textContent = 'Choose File';
    fileNamePlaceholder.textContent = input.files[0].name; // This line sets the file name
  } else {
    fileNamePlaceholder.textContent = 'No file chosen';
  }
}





function handleAudioFileSelect(input) {
  const fileNamePlaceholder = document.getElementById('file-name-placeholder');
  if (input.files.length > 0) {
      fileNamePlaceholder.textContent = input.files[0].name;
  } else {
      fileNamePlaceholder.textContent = 'No file chosen';
  }
}

function redirectToImage2Text() {
  window.location.href = "/Image2Text";
}
















