// Check for browser support
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (!SpeechRecognition) {
  alert('Sorry, your browser does not support Speech Recognition.');
  throw new Error('Speech Recognition API is not supported in this browser.');
}

// Initialize speech recognition
const recognition = new SpeechRecognition();
recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = 'es-ES'; // Set the language to Spanish

// Function to start or stop recognition based on its current state
function toggleVoiceRecognition() {
  if (recognition && recognition.started) {
    recognition.stop();
  } else {
    recognition.start();
  }
}

// Add event listener to the microphone button
const microphoneButton = document.getElementById('microphone');
microphoneButton.addEventListener('click', toggleVoiceRecognition);

// Function to insert recognized text into the active element
function insertText(text) {

  // Find the TinyMCE editor that is currently focused
  const activeEditor = localStorage.getItem('editorActivoId');
  console.log('Editor activo: ', activeEditor);

  if (activeEditor) {
    const editor = tinymce.get(activeEditor);
    if (editor) {
      editor.insertContent(text);
    }

  } else {
    // Fallback to inserting text into standard input or textarea elements if no TinyMCE editor is focused
    const activeElement = document.activeElement;
    if (activeElement.tagName.toLowerCase() === 'input' || activeElement.tagName.toLowerCase() === 'textarea') {
      // Insert text into the standard input or textarea element
      activeElement.value += text;
      activeElement.dispatchEvent(new Event('input'));
    }
  }
}


// Event handler for when the speech recognition service starts
recognition.onstart = function() {
  recognition.started = true;
  microphoneButton.classList.add('activemic');
};

// Event handler for when the speech recognition service ends
recognition.onend = function() {
  recognition.started = false;
  microphoneButton.classList.remove('activemic');
};

// Event handler for the result event which contains the speech recognition results
recognition.onresult = function(event) {
  let finalTranscript = ''; // Store the final transcript
  let interimTranscript = ''; // Store the interim results

  // Loop through the results from the speech recognition event
  for (let i = event.resultIndex; i < event.results.length; ++i) {
    // If the result is final, append it to the final transcript
    if (event.results[i].isFinal) {
      finalTranscript += event.results[i][0].transcript.trim();
    } else {
      // If the result is not final, append it to the interim transcript
      interimTranscript += event.results[i][0].transcript.trim();
    }
  }

  // Insert the final transcript into the active element
  if (finalTranscript !== '') {
    insertText(finalTranscript);
  }

  // You can also handle interim results here, if necessary
};

// Event handler for speech recognition errors
recognition.onerror = function(event) {
  console.error('Speech Recognition Error: ', event.error);
  recognition.stop();
};

// Optional: if you want to handle no match found for speech input
recognition.onnomatch = function(event) {
  console.warn('No match found for speech input: ', event);
};