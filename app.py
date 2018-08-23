from flask import Flask, render_template, request, redirect
#import turicreate as tc

app = Flask(__name__)
#
# data = tc.load_sframe('test.sframe')
# model = tc.load_model('imgset')
#
# image_show = model.query(data[0:10], k=20)
#
#

class Distance :
    distance_total=[
        [0.2,0.5,0.8,6,7,14.5,15],
        [0.2,1,11.8,14,12.4,1,0.2]
    ]
    distance_same=[
        [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6],
        [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9]
    ]
    distance_similar=[
        [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6, 4.7, 3, 5],
        [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9, 10, 12, 13]
    ]
    distance_avg = 10.73
    distance_max = 15
    distance_min = 1
    count_almost_same = 72
    count_similar = 3270
    count_total = 2039400

@app.route('/')
def hello_world():
    return render_template('basic.html', Distance=Distance)


if __name__ == '__main__':
    app.run()
