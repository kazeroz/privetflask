from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return '<html>
<head>
<script type="text/javascript">
    var text = document.getElementsByTagName("input")[0];
    var val=text.innerHTML;
    alert(val)
</script>
</head>
<body>
<form action="#"><input type="text" value="Some text here..." />
<input type="submit" />
</form>
</body>
</html>'

if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)
