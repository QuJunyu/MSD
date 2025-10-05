document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('token');
    if (!token) {
        alert('Please log in first.');
        window.location.href = 'login.html';
        return;
    }

    const passwordForm = document.getElementById('passwordForm');
    const messageDiv = document.getElementById('message');

    passwordForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const oldPassword = passwordForm.oldPassword.value.trim();
        const newPassword = passwordForm.newPassword.value.trim();

        if (!oldPassword) {
            showMessage('Please enter your old password.', 'error');
            return;
        }
        if (!newPassword) {
            showMessage('Please enter a new password.', 'error');
            return;
        }
        if (newPassword.length < 6) {
            showMessage('The new password must consist of at least 6 characters.', 'error');
            return;
        }
        if (oldPassword === newPassword) {
            showMessage('The new password cannot be the same as the old one.', 'error');
            return;
        }

        fetch('http://127.0.0.1:5000/api/user/change-password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ old_password: oldPassword, new_password: newPassword })
        })
        .then(response => {
            if (!response.ok) throw new Error('Service connection failed');
            return response.json();
        })
        .then(result => {
            if (result.success) {
                showMessage('Password modification was successful. You will be redirected to the login page shortly....', 'success');
                localStorage.removeItem('token');
                setTimeout(() => {
                    window.location.href = 'login.html';
                }, 1500);
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
