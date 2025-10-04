document.addEventListener('DOMContentLoaded', function() {
  const publishForm = document.getElementById('publishForm');
  const submitBtn = publishForm.querySelector('button[type="submit"]'); // 获取提交按钮
  
  publishForm.addEventListener('submit', function(e) {
    e.preventDefault(); // 强制阻止默认提交（优先执行）
    submitBtn.disabled = true; // 禁用按钮，防止重复提交
    submitBtn.textContent = 'Publishing...';

    // 1. 获取所有字段（包括新增的condition）
    const title = publishForm.title.value.trim();
    const author = publishForm.author.value.trim();
    const price = publishForm.price.value.trim(); // 用trim()避免空格
    const condition = publishForm.condition.value; // 获取书籍品相

    // 2. 前端验证（覆盖所有字段）
    if (title === '') { 
      alert('Please enter the book title.'); 
      submitBtn.disabled = false;
      submitBtn.textContent = 'Release';
      return; 
    }
    if (author === '') { 
      alert('Please enter the author.'); 
      submitBtn.disabled = false;
      submitBtn.textContent = 'Release';
      return; 
    }
    if (price === '' || isNaN(price) || parseFloat(price) <= 0) { 
      alert('The price must be a positive number.'); 
      submitBtn.disabled = false;
      submitBtn.textContent = 'Release';
      return; 
    }
    if (!condition) { // 验证书籍品相
      alert('Please select the grade of quality.'); 
      submitBtn.disabled = false;
      submitBtn.textContent = 'Release';
      return; 
    }

    // 3. 获取登录token
    const token = localStorage.getItem('token');
    if (!token) { 
      alert('Please log in first.'); 
      window.location.href = 'login.html'; 
      return; 
    }

    // 4. 发送请求（包含condition字段）
    fetch('http://127.0.0.1:5000/api/book/publish', {
      method: 'POST', // 确保是POST
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ 
        title, 
        author, 
        price: parseFloat(price), // 转为数字类型
        condition // 新增：传递书籍品相
      })
    })
    .then(response => {
      if (!response.ok) throw new Error('Failed to publish book');
      return response.json();
    })
    .then(result => {
      if (result.success) {
        alert('Book published successfully!');
        publishForm.reset(); // 清空表单
      } else {
        alert(result.message);
      }
    })
    .catch(error => {
      alert('Error: ' + error.message);
    })
    .finally(() => {
      // 无论成功失败，恢复按钮状态
      submitBtn.disabled = false;
      submitBtn.textContent = 'Release';
    });
  });
});
