<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>登录 - 校园二手书交易平台</title>
    <link rel="stylesheet" href="css/login.css">  <!-- 关联后续CSS文件 -->
  </head>
  <body>
    <div class="login-container">
      <h2>用户登录</h2>
      <form id="loginForm">  <!-- 表单ID供JS调用 -->
        <div class="form-group">
          <label>用户名：</label>
          <input type="text" name="username" required>  <!-- 与后端接口参数一致 -->
        </div>
        <div class="form-group">
          <label>密码：</label>
          <input type="password" name="password" required>
        </div>
        <button type="submit">登录</button>
        <p>还没有账号？<a href="register.html">立即注册</a></p>  <!-- 跳转注册页 -->
      </form>
    </div>
  </body>
</html>
