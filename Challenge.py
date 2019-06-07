from flask import Flask, render_template, request, jsonify
app = Flask(__name__)





@app.route('/')
def landing():
    return render_template('home.html')



@app.route('/record-hike')
def record_hike():
    return render_template('record-hike.html')



@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return  render_template('result.html', result = result)



if __name__ ==  '__main__':
    app.run(debug=True)


