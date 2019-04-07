from flask import *
from mlap import all_bike
app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('bike.html')
    else:
        form = request.form
        create_bike={}
        head=['Model','Daily','Image','Year']
        inputs=['input_model','input_dailyfee','input_image','input_year']
        for i in range(4):
            create_bike[head[i]]=form[inputs[i]]
        all_bike.insert_one(create_bike)
    return redirect('/create')

@app.route('/view')
def view():
    findbike=all_bike.find()
    return render_template('bikeview.html',all_bike=findbike)

if __name__ == '__main__':
  app.run(debug=True)
 