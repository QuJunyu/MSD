document.addEventListener('DOMContentLoaded', function() {
    const bookList = document.getElementById('bookList');
    const messageDiv = document.getElementById('message');

    fetchBooks();

    function fetchBooks() {
        fetch('http://127.0.0.1:5000/api/book/all', {
            method: 'GET'
        })
        .then(response => {
            if (!response.ok) throw new Error('Failed to obtain the book');
            return response.json();
        })
        .then(result => {
            if (result.success) {
                renderBooks(result.books);
            } else {
                showMessage(result.message, 'error');
            }
        })
        .catch(error => {
            showMessage(error.message, 'error');
            bookList.innerHTML = '<li>Failed to load. Please refresh the page and try again.</li>';
        });
    }

    function renderBooks(books) {
        if (books.length === 0) {
            bookList.innerHTML = '<li>No books have been released yet.</li>';
            return;
        }

        let html = '';
        books.forEach(book => {
            const publishTime = new Date(book.publish_time).toLocaleDateString();
            html += `
                <li class="book-item">
                    <h3>${book.title}</h3>
                    <div class="book-info">
                        <span>Author：${book.author}</span>
                        <span>Price：¥${book.price}</span>
                        <span>Condition：${book.condition}</span> <!-- 直接显示英文品相值 -->
                        <span>Publisher：${book.username}</span>
                    </div>
                    <div class="publish-time">Release date：${publishTime}</div>
                </li>
            `;
        });
        bookList.innerHTML = html;
    }

    window.logout = function() {
        localStorage.removeItem('token');
    };

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
    }
});
