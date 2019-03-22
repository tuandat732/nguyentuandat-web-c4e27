from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello c4e27'

@app.route('/say-hi/<sum>/<int:a>/<int:b>') 
def sayhi(sum,a,b):
    sum=a+b
    return 'ket qua ne ' + str(sum)

@app.route('/poem')
def poem():
    poems=[
            {
                'title':'thơ con cóc',
                'content':'hôm nay trăng lên cao quá',
                'author':'hue',
                'gender':'female'
            },
            {
                'title':'thơ con cho',
                'content':'ko co j dau haha',
                'author':'nam',
                'gender':'male'
            }
    ]

    return render_template('poem.html',poems=poems)
if __name__ == '__main__':
  app.run(debug=True)
 