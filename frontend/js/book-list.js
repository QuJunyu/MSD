document.addEventListener('DOMContentLoaded', function() {
    const bookList = document.getElementById('bookList');
    const messageDiv = document.getElementById('message');

    fetchBooks();

    function fetchBooks() {
        fetch('http://127.0.0.1:5000/api/book/all', {
            method: 'GET'
        })
        .then(response => {
            if (!response.ok) throw new Error('获取书籍失败');
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
            bookList.innerHTML = '<li>加载失败，请刷新页面重试</li>';
        });
    }

    function renderBooks(books) {
        if (books.length === 0) {
            bookList.innerHTML = '<li>暂无已发布的书籍</li>';
            return;
        }

        // 状态中文映射
        const conditionMap = {
            'new': '全新',
            'like-new': '接近全新',
            'used': '已使用'
        };

        let html = '';
        books.forEach(book => {
            const publishTime = new Date(book.publish_time).toLocaleDateString();
            const conditionText = conditionMap[book.condition] || book.condition;
            html += `
                <li class="book-item">
                    <h3>${book.title}</h3>
                    <div class="book-info">
                        <span>作者：${book.author}</span>
                        <span>价格：¥${parseFloat(book.price).toFixed(2)}</span>
                        <span>状态：${conditionText}</span>
                        <span>发布者：${book.username}</span>
                    </div>
                    <div class="publish-time">发布时间：${publishTime}</div>
                </li>
            `;
        });
        bookList.innerHTML = html;
    }

    window.logout = function() {
        localStorage.removeItem('token');
        alert('已成功退出登录');
        window.location.href = 'login.html';
    };

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
        // 3秒后自动隐藏
        setTimeout(() => {
            messageDiv.textContent = '';
            messageDiv.className = 'message';
        }, 3000);
    }
});
