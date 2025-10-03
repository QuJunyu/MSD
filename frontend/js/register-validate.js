document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const messageDiv = document.getElementById('message');

    registerForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const username = registerForm.username.value.trim();
        const password = registerForm.password.value.trim();

        // 前端验证
        if (!username) {
            showMessage('Please enter your username', 'error');
            return;
        }
        if (username.length < 3) {
            showMessage('Username must be at least 3 characters long', 'error');
            return;
        }
        if (!password) {
            showMessage('Please enter your password', 'error');
            return;
        }
        if (password.length < 6) {
            showMessage('The password must consist of at least 6 characters', 'error');
            return;
        }

        // 调用注册接口
        fetch('http://127.0.0.1:5000/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => {
            if (!response.ok) throw new Error('Service connection failed');
            return response.json();
        })
        .then(result => {
            if (result.success) {
                showMessage('Registration successful. You will be redirected to the login page shortly...', 'success');
                setTimeout(() => {
                    window.location.href = 'login.html';
                }, 1500);
            } else {
                showMessage(result.message, 'error');
            }
        })
        .catch(error => {
            showMessage(error.message, 'error');
        });
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
    }
});
