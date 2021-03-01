from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>' \
           """
           <div id="biaoqian">
				<ul>
					<li>
						<a href="#">首页</a>
					</li>
					<li>
						<a href="#">新疆简介</a>
					</li>
					<li>
						<a href="#">风土人情</a>
					</li>
					<li>
						<a href="#">吃在新疆</a>
					</li>
					<li>
						<a href="#">路线选择</a>
					</li>
					<li>
						<a href="#">自助行</a>
					</li>
					<li>
						<a href="#">摄影摄像</a>
					</li>
					<li>
						<a href="#">游记精选</a>
					</li>
					<li>
						<a href="#">资源下载</a>
					</li>
					<li>
						<a href="#">雁过留声</a>
					</li>
				</ul>
			</div>
           """

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()