document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('forgotPasswordForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const username = form.username.value.trim();
        const newPassword = form.newPassword.value.trim();

        // 前端验证
        if (!username) {
            showMessage('Please enter your username', 'error');
            return;
        }
        if (!newPassword) {
            showMessage('Please enter a new password', 'error');
            return;
        }
        if (newPassword.length < 6) {
            showMessage('The new password must be at least 6 characters', 'error');
            return;
        }

        // 发送重置密码请求
        fetch('http://127.0.0.1:5000/api/user/forgot-password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                new_password: newPassword
            })
        })
        .then(response => {
            if (!response.ok) throw new Error('Service connection failed');
            return response.json();
        })
        .then(result => {
            if (result.success) {
                showMessage('Password reset successful, please login', 'success');
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
