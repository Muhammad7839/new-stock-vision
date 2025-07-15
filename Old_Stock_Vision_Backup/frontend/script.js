fetch("http://127.0.0.1:5000/api/message")
  .then(response => response.json())
  .then(data => {
    document.body.innerHTML += `<p>${data.text}</p>`;
  })
  .catch(error => {
    console.error("Error:", error);
  });