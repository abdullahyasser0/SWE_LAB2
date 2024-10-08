from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('result.html',name=name,email=email)


@app.route('/return',methods=['POST'])
def re():
    return render_template('form.html')



if __name__== '__main__':
    app.run()