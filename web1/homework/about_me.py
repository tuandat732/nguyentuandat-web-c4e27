from flask import Flask, render_template,redirect
app = Flask(__name__)

@app.route('/about-me/')
def me():
    me={
        "name":"Nguyễn Tuấn Đạt",
        "age": '19',
        'work':'...',
        'school':'PTIT',
        'hobbies':'...',
    }
    return render_template('about_me.html', me = me)

@app.route('/school')
def school():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run( debug=True)
 