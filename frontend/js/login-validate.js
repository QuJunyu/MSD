// 等待页面加载完成
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const messageDiv = document.getElementById('message');

    // 表单提交事件
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault(); // 阻止默认提交

        // 获取输入值
        const username = loginForm.username.value.trim();
        const password = loginForm.password.value.trim();

        // 前端验证
        if (!username) {
            showMessage('Please enter your username', 'error');
            return;
        }
        if (!password) {
            showMessage('Please enter your password', 'error');
            return;
        }

        // 调用登录接口
        fetch('http://127.0.0.1:5000/api/login', {
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
                // 登录成功：存储token并跳转书籍发布页
                localStorage.setItem('token', result.token);
                showMessage('Login successful. Redirecting...', 'success');
                setTimeout(() => {
                    window.location.href = 'book-publish.html';
                }, 1500);
            } else {
                showMessage(result.message, 'error');
            }
        })
        .catch(error => {
            showMessage(error.message, 'error');
        });
    });

    // 显示提示信息
    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
    }
});
