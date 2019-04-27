from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'ZDAROVA DENIS!!!! '
chars = "s"
check_string ="saaassd"

count= {}
for s in check_string:
    if count.has_key(s):
        count[s]+=1
        else:
            count[s]=1
            for key in count :
                if count[key] >1:
                    print key, count[key]:
if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)
