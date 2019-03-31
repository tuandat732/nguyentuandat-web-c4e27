from flask import Flask, render_template
from mlab import co_river,all_river
continent=[]
for i in all_river:
    if i['continent'] not in continent:
        continent.append(i['continent'])
app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('home.html',continent=continent)

@app.route('/home/detail/<con>/')
def conti(con):
    list_river=co_river.find({'continent':con})
    return render_template('detailriver.html',list_river=list_river,con=con)

@app.route('/home/detail/<con>/<h>')
def ex6(con,h):
    list_river=co_river.find({'continent':con})
    list_riverh=[]
    for i in list_river:
            if i['length'] <= int(h):
                    list_riverh.append(i)
    return render_template('detailriver.html',list_river=list_riverh,con=con,h=h)


if __name__ == '__main__':
    app.run(debug=True)
 

