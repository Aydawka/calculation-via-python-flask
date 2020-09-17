from flask import Flask, render_template,request,flash
app=Flask(__name__)
 
@app.route('/')
def entry_page():
    return render_template('home.html',page_title='Welcome to tiny-miny Einstein Project')

@app.route('/h')
def entry_page1():
    return render_template('home1.html',page_title='Welcome to tiny-miny Einstein Project')




@app.route('/sum',methods=['POST'])
def sum():
    x=int(request.form['firstValue'])
    y=int(request.form['secondValue'])
    return render_template('sum.html',page_title='Calculation result',sum_result=(x+y),first_value=x,second_value=y)
 
@app.route('/minus',methods=['POST'])
def minus():
    x=int(request.form['firstValue'])
    y=int(request.form['secondValue'])
    return render_template('minus.html',page_title='Calculation result',sum_result1=(x-y),first_value=x,second_value=y)
 


if __name__ == '__main__':
    app.run(debug=True)