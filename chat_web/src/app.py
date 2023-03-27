from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/form', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        input_text = request.form['input_text']
        return f'<p style="color:red;">{input_text}</p>'
    else:
        return '''
            <form method="post">
                <label for="input_text">文章を入力してください:</label>
                <input type="text" id="input_text" name="input_text">
                <button type="submit">送信</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4400)