from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi1/<int:weight>/<int:height>')
def cal1(weight,height):
    height=height/100
    bmi=weight/(height*height)
    if(bmi<16):
        text='BMI: '+str(bmi)+'=> Severely underweight'
    elif(bmi<18.5):
        text='BMI: '+str(bmi)+'=> Underweight'
    elif(bmi<25):
        text='BMI: '+str(bmi)+'=> Normal'
    elif(bmi<30):
        text='BMI: '+str(bmi)+'=> Overweight'
    else:
        text='BMI: '+str(bmi)+'=> Obese'
    return render_template('bmi.html',text=text)

@app.route('/bmi2/<int:weight>/<int:height>')
def cal2(weight,height):
    height=height/100
    bmi=weight/(height*height)
    if(bmi<16):
        text='bmi: '+str(bmi)+'=> Severely underweight'
    elif(bmi<18.5):
        text='bmi: '+str(bmi)+'=> Underweight'
    elif(bmi<25):
        text='bmi: '+str(bmi)+'=> Normal'
    elif(bmi<30):
        text='bmi: '+str(bmi)+'=> Overweight'
    else:
        text='bmi: '+str(bmi)+'=> Obese'
    return text

if __name__ == '__main__':
  app.run(debug=True)
 