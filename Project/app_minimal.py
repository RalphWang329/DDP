# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g

app = Flask("app")


# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# Each @app.route(...) indicates a URL.
# Using that URL causes the function immediately after the @app.route(...) line to run.
# THIS ROUTE IS TO PROVE THE FLASK SETUP WORKS.
# YOU SHOULD REPLACE IT WITH YOUR OWN CONTENT.
        

users = {
    'administrator':'password'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # 检查用户名和密码是否匹配
        if username in users and users[username] == password:
            # 登录成功，重定向到主页
            return redirect(url_for('index', username=username))
        elif username not in users:
            # 登录失败，检查是否需要跳转到注册页面
            return redirect(url_for('register'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 检查用户名是否已经存在
        if username in users:
            # 用户名已存在，重定向到注册页面，并在 URL 中添加错误参数
            return redirect(url_for('register', error='This account already exists'))
        else:
            # 将新用户添加到数据库中
            users[username] = password
            # 注册成功后，重定向到登录页面
            return redirect(url_for('login'))

    return render_template('register.html')

        

products_dict = {
    'Bumble tea': {'price': '$10', 'quantity': 20}
}


@app.route('/products_update', methods=['GET', 'POST'])
def products_update():
    if request.method == 'POST':
        product_name = request.form['product-name']
        price = request.form['price']
        quantity = request.form['quantity']
        
        # 将输入的内容添加到字典中
        products_dict[product_name] = {'price': price, 'quantity': quantity}
        
        return redirect(url_for('success'))

    return render_template('products_update.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/show_products')
def show_products():
    return render_template('products.html', products=products_dict)

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')






### YOUR CODE GOES HERE ###
if __name__ == "__main__":
    app.run(debug=True)
