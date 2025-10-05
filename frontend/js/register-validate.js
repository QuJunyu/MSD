document.addEventListener('DOMContentLoaded', function() {
  const registerForm = document.getElementById('registerForm');
  
  registerForm.addEventListener('submit', function(e) {
    e.preventDefault(); // 阻止表单默认提交（避免页面刷新）
    
    // 1. 前端表单验证（你原有的逻辑，保留不变）
    const username = registerForm.username.value.trim();
    const password = registerForm.password.value.trim();
    const confirmPwd = registerForm.confirmPassword.value.trim();
    
    if (username === '') { 
      alert('Please enter your username.'); 
      return; 
    }
    if (password.length < 6) { 
      alert('The password must be at least 6 characters long.'); 
      return; 
    }
    if (password !== confirmPwd) { 
      alert('The passwords were inconsistent twice.'); 
      return; 
    }
    
    console.log('Registration information verification has been completed. It is ready to be submitted to the backend.');

    // 2. 新增：发送请求到后端注册接口（核心补充部分）
    fetch('http://127.0.0.1:5000/api/register', { // 后端注册接口地址
      method: 'POST', // 必须用POST方法（和后端接口一致）
      headers: {
        'Content-Type': 'application/json', // 告诉后端请求体是JSON格式
      },
      body: JSON.stringify({ // 把表单数据转成JSON字符串，发给后端
        username: username,
        password: password
      })
    })
    // 3. 处理后端返回的响应
    .then(response => {
      // 先判断响应状态是否正常（200-299为成功）
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json(); // 把后端返回的JSON数据解析成JS对象
    })
    .then(data => {
      // 4. 根据后端返回的结果处理（success为true/false）
      if (data.success) {
        // 注册成功：提示用户 + 跳转到登录页（替换为你的登录页路径）
        alert('Registration successful! Redirecting to login page...');
        window.location.href = 'login.html'; // 关键：跳转登录页
      } else {
        // 注册失败：显示后端返回的错误信息（如“用户名已存在”）
        alert('Registration failed: ' + data.message);
      }
    })
    // 5. 捕获请求过程中的错误（如后端没启动、网络断了）
    .catch(error => {
      console.error('Error during registration:', error);
      alert('Registration failed! Please check if the backend service is running.');
    });
  });
});
