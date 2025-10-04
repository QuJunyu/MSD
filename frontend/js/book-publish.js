document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('token');
    if (!token) {
        alert('Please log in first.');
        window.location.href = 'login.html';
        return;
    }

    const publishForm = document.getElementById('publishForm');
    const messageDiv = document.getElementById('message');

    publishForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const title = publishForm.title.value.trim();
        const author = publishForm.author.value.trim();
        const price = publishForm.price.value.trim();

        if (!title) {
            showMessage('Please enter the title of the book.', 'error');
            return;
        }
        if (!author) {
            showMessage('Please enter the author.', 'error');
            return;
        }
        if (!price || isNaN(price) || parseFloat(price) < 0) {
            showMessage('Please provide a valid price.', 'error');
            return;
        }

        fetch('http://127.0.0.1:5000/api/book/publish', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ title, author, price })
        })
        .then(response => {
            if (!response.ok) throw new Error('Service connection failed');
            return response.json();
        })
        .then(result => {
            if (result.success) {
                showMessage('Book release was successful.！', 'success');
                publishForm.reset();
            } else {
                showMessage(result.message, 'error');
                if (result.message.includes('Please log in first.')) {
                    localStorage.removeItem('token');
                    setTimeout(() => window.location.href = 'login.html', 1500);
                }
            }
        })
        .catch(error => {
            showMessage(error.message, 'error');
        });
    });

    window.logout = function() {
        localStorage.removeItem('token');
    };

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
    }
});
