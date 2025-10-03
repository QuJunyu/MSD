document.addEventListener('DOMContentLoaded', function() {
  const publishForm = document.getElementById('publishForm');
  
  publishForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const title = publishForm.title.value.trim();
    const price = publishForm.price.value;
    
    if (title === '') { alert('Please enter the book title.'); return; }
    if (price <= 0) { alert('The price must be greater than 0.'); return; }
    
    console.log('The book information has been verified and is ready to be submitted to the backend.');
  });
});
