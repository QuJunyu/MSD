const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const app = express();

// 配置跨域（允许前端地址访问，示例为允许所有，生产环境需指定具体域名）
app.use(cors());

// 解析请求体（支持JSON和表单格式）
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 模拟数据库中的用户（实际项目中应从数据库查询，且密码需哈希存储）
const mockUsers = [
  { id: 1, username: 'admin', password: 'admin123' },  // 示例用户1
  { id: 2, username: 'test', password: 'test456' }     // 示例用户2
];

// Token配置（生产环境密钥需保密，可存在环境变量中）
const JWT_SECRET = 'your-secret-key-123';  // 密钥
const JWT_EXPIRES_IN = '2h';               // Token有效期2小时


// 登录接口
app.post('/api/login', (req, res) => {
  try {
    // 1. 获取请求参数
    const { username, password } = req.body;

    // 2. 后端二次验证（防止绕过前端直接调用接口）
    if (!username || !password) {
      return res.status(400).json({
        success: false,
        message: '用户名和密码不能为空'
      });
    }

    // 3. 验证用户名和密码（实际项目中应查询数据库，并用bcrypt比对哈希密码）
    const user = mockUsers.find(u => u.username === username && u.password === password);
    if (!user) {
      return res.status(401).json({
        success: false,
        message: '用户名或密码错误'
      });
    }

    // 4. 生成Token（包含用户ID，用于后续接口身份验证）
    const token = jwt.sign(
      { userId: user.id, username: user.username },  // Token payload（避免放敏感信息）
      JWT_SECRET,
      { expiresIn: JWT_EXPIRES_IN }
    );

    // 5. 返回成功响应
    res.status(200).json({
      success: true,
      message: '登录成功',
      token: token  // 前端需存储Token（如localStorage），后续请求携带
    });

  } catch (error) {
    // 捕获服务器异常
    res.status(500).json({
      success: false,
      message: '服务器内部错误，请稍后再试'
    });
  }
});


// 启动服务器（监听3000端口）
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`登录接口已启动，地址：http://localhost:${PORT}/api/login`);
});
