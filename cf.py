from flask import Flask, render_template_string
import random

app = Flask(__name__)

# HTML templates
index_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coin Flip</title>
</head>
<body>
    <h1>Coin Flip</h1>
    <p>Click the button below to flip the coin:</p>
    <form action="/flip_coin" method="get">
        <button type="submit">Flip Coin</button>
    </form>
</body>
</html>
'''

result_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coin Flip Result</title>
</head>
<body>
    <h1>Coin Flip Result</h1>
    <p>The result of the coin flip is: <strong>{{ result }}</strong></p>
    <p><a href="/">Back to Home</a></p>
</body>
</html>
'''

# Routes
@app.route('/')
def home():
    return render_template_string(index_template)

@app.route('/flip_coin')
def flip_coin():
    result = random.choice(['Heads', 'Tails'])
    return render_template_string(result_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
