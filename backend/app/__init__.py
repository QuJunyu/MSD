from flask import Flask
from flask_cors import CORS

# 初始化Flask应用（核心对象）
app = Flask(__name__)

# 修正1：允许所有/api/*接口跨域（包含登录和注册）
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 修正2：导入整个接口模块，确保路由定义代码被执行
from ..api import login_api    # 导入整个login_api模块，触发登录路由注册
from ..api import register_api # 导入整个register_api模块，触发注册路由注册
