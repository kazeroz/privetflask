from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'ZDAROVA DENIS!!!! '
chars = "s"
check_string ="saaassd"
for cher in chars:
    count = check_string.count(char)
    if count > 1:
        print chart, count
if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)
