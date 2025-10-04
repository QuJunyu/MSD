from flask import Flask
from flask_cors import CORS

# 初始化Flask应用（核心对象）
app = Flask(__name__)

# 允许所有/api/*接口跨域
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 导入接口函数，确保路由注册（关键修正）
from ..api.login_api import login           # 登录接口
from ..api.register_api import register     # 注册接口
from ..api.book_api import publish_book     # 书籍发布接口（新增）
from ..api.book_api import get_all_books    # 查看书籍接口（新增）
