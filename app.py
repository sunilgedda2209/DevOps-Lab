from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App! Go to /register"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            return "Missing form fields!", 400

        return render_template('success.html', username=username, email=email)

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
