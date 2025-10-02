document.addEventListener('DOMContentLoaded', function() {
  const registerForm = document.getElementById('registerForm');
  
  registerForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const username = registerForm.username.value.trim();
    const password = registerForm.password.value.trim();
    const confirmPwd = registerForm.confirmPassword.value.trim();
    
    if (username === '') { alert('Please enter your username.'); return; }
    if (password.length < 6) { alert('The password must be at least 6 characters long.'); return; }
    if (password !== confirmPwd) { alert('The passwords were inconsistent twice.'); return; }
    
    console.log('Registration information verification has been completed. It is ready to be submitted to the backend.');
  });
});
