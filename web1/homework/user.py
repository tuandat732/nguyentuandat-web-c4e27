from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user_m(username):
    users={
        'dat':{
                "name":"Nguyễn Tuấn Đạt",
            "age": '19',
            'work':'...',
            'school':'PTIT',
            'hobbies':'Trâm',
        },
        'tram':{
                "name":"Lê Thị Ngọc Trâm",
            "age": '19',
            'work':'...',
            'school':'hus',
            'hobbies':'Đạt',
        },
        'quan':{
                "name":"Nguyễn Trần Anh Quân",
            "age": '19',
            'work':'osin của Đạt',
            'school':'HUST',
            'hobbies':'...',
        },
        'Nam':{
                "name":"Nguyễn Phương Nam",
            "age": '19',
            'work':'osin giống Quân(level cao hơn)',
            'school':'HUST',
            'hobbies':'...',
        },
    }
    
    if username in users: 
        return render_template('user.html',user=users[username],username=username)
    else:
        username='NAME NOT FOUND'
        return render_template('user.html',user=username)

    

if __name__ == '__main__':
  app.run(debug=True)
 