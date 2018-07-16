from flask import (Flask,
 render_template, request)
app = Flask('app')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/welcome',methods=['POST'])
def display():
  data=dict(request.form.items())
  
  name=str(data.get('name','Guest'))
  email=str(data.get('email', 'no@gmail.com'))
  course=str(data.get('course','Not provided' ))
  context = {'name':name,'email':email,'course':course}
  return  render_template("welcome.html",**context)


if __name__== '__main__':
  app.run( debug= True ,host='0.0.0.0',port = 8080) 