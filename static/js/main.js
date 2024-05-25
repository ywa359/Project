// Animations
AOS.init({
    anchorPlacement: 'top-left',
    duration: 1000
});

// Add your javascript here
// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Define the URL endpoint from which to fetch the data
var url = 'https://example.com/data';

// Open a new GET request to the specified URL
xhr.open('GET', url, true);

// Set up a callback function to handle the response
xhr.onload = function() {
  // Check if the request was successful
  if (xhr.status >= 200 && xhr.status < 300) {
    // Parse the JSON response into a JavaScript object
    var responseData = JSON.parse(xhr.responseText);

    // Use the response data to update the HTML content
    updateContent(responseData);
  } else {
    // Handle errors
    console.error('Request failed with status ' + xhr.status);
  }
};

// Set up a callback function to handle errors
xhr.onerror = function() {
  console.error('Request failed');
};

// Send the request
xhr.send();

// Function to update the HTML content with the response data
function updateContent(data) {
  // Example: Update the age, email, phone, and address fields
  document.querySelector('.text-secondary[data-field="age"]').textContent = data.age;
  document.querySelector('.text-secondary[data-field="email"]').textContent = data.email;
  document.querySelector('.text-secondary[data-field="phone"]').textContent = data.phone;
  document.querySelector('.text-secondary[data-field="address"]').textContent = data.address;
}
