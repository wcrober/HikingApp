from flask import Flask, render_template, request, url_for, jsonify
import geocoder



app = Flask(__name__)

g = geocoder.ip('me')
latitude = g.lat
longitude = g.lng



@app.route('/')
def landing():
    return render_template('home.html')


@app.route('/record-hike')
def record_hike():
    return render_template('record-hike.html')




@app.route('/result',methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result,latitude=latitude, longitude=longitude )


@app.route('/schedule-post')
def schedule_post():
    return render_template('schedule_post.html')

@app.route('/auto-track')
def autot_track():
    return render_template('auto_track.html')

if __name__ == '__main__':
    app.run(debug=True)


