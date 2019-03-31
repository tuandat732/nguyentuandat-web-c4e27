from flask import Flask, render_template, redirect
from services import Services
from bson.objectid import ObjectId #về nhà gg xem json vs bson khác j nhau
app = Flask(__name__)


@app.route('/')
def hompage():
    return render_template('homepage.html')

@app.route('/all-service/<g>')
def gender(g):
  services = Services.find({'gender':g})
  return render_template('all-service.html',all_service=services)


@app.route('/all-service')
def allser():
  all=Services.find()
  return render_template('all-service.html',all_service=all)

@app.route('/all-service/detail/<id>')
def detail(id):
  detail_person = Services.find_one({'_id':ObjectId(id)})
  return render_template('detail.html' ,detail_person=detail_person)

@app.route('/all-service/delete/<id>')
def delete(id):
  delete_person=Services.find_one({'_id':ObjectId(id)})
  Services.delete_one(delete_person)
  return redirect('/all-service') # tro lai trang all-service


if __name__ == '__main__':
  app.run(debug=True)
 