from flask import Flask, render_template, request, session, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

from flask_dropzone import Dropzone
from flask_sqlalchemy import SQLAlchemy

# Load Model Class
from turi_model import TuriObj
from db_model import DBObj
import pandas as pd
import sqlite3

# db Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model/mark.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'mark'

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static/assets/file-upload'

# Activate app
dropzone = Dropzone(app)
db = SQLAlchemy(app)


# Connect Upload Router
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class Distance:
    def __init__(self):
        self.top8 = 8
        self.distance_top = [1, 2, 3, 4, 5, 6, 7, 8]
        self.distance_avg = 10.73
        self.distance_max = 32
        self.distance_min = 7
        self.count_almost_same = 72
        self.count_similar = 3270
        self.count_total = 2039400
        self.distance_top = [1, 2, 3, 4, 5, 6, 7, 8]
        self.distance_similar_b = [3, 4, 5, 6, 7, 8, 9, 10]
        self.distance_total = [
                [0.2, 0.5, 0.8, 6, 7, 14.5, 15],
                [0.2, 1, 11.8, 14, 12.4, 1, 0.2]
            ]
        self.distance_same = [
                [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6],
                [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9]
            ]
        self.distance_similar = [
                [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6, 4.7, 3, 5],
                [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9, 10, 12, 13]
            ]

    def set_graph(self):
        data = a.results.to_dataframe()
        self.top8 = data.head(n=8).distance.mean()
        self.distance_avg = data['distance'].mean()
        self.distance_max = data['distance'][len(data) - 1]
        self.distance_min = data['distance'][0]
        self.count_total = len(data)
        self.count_almost_same = data.loc[data['distance'] < (self.distance_min+((self.distance_max-self.distance_min)/739))].distance.count()
        self.count_similar = data.loc[data['distance'] < (self.distance_min+((self.distance_max-self.distance_min)/44))].distance.count()


        self.distance_total = [
            [
                (data.iloc[int(self.count_total / 740)].distance),
                (data.iloc[int(self.count_total / 44)].distance),
                (data.iloc[int(self.count_total / 6)].distance),
                (data.iloc[int(self.count_total / 2)].distance),
                (data.iloc[int(self.count_total * 5 / 6)].distance),
                (data.iloc[int(self.count_total * 43 / 44)].distance),
                (data.iloc[int(self.count_total * 739 / 740)].distance)
            ],
            [
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 740))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 44))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 6))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 2))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 5 / 6))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 43 / 44))].distance.count()) * self.distance_max / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 739 / 740))].distance.count()) * self.distance_max / self.count_total
            ]
        ]
        self.distance_same = [
            [
                0,
                2,
                3.5,
                4,
                8,
                3,
                4,
                6,
                2,
                6
            ],
            [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9]
        ]
        self.distance_similar = [
            [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6, 4.7, 3, 5],
            [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9, 10, 12, 13]
        ]

        self.distance_top = [
            data.head(n=8).distance[0],
            data.head(n=8).distance[1],
            data.head(n=8).distance[2],
            data.head(n=8).distance[3],
            data.head(n=8).distance[4],
            data.head(n=8).distance[5],
            data.head(n=8).distance[6],
            data.head(n=8).distance[7]
        ]
        self.distance_similar_b = [
            data.iloc[int(self.count_similar * 1 / 8)].distance,
            data.iloc[int(self.count_similar * 2 / 8)].distance,
            data.iloc[int(self.count_similar * 3 / 8)].distance,
            data.iloc[int(self.count_similar * 4 / 8)].distance,
            data.iloc[int(self.count_similar * 5 / 8)].distance,
            data.iloc[int(self.count_similar * 6 / 8)].distance,
            data.iloc[int(self.count_similar * 7 / 8)].distance,
            data.iloc[int(self.count_similar)].distance
        ]

a = TuriObj()
b = Distance()
sql_obj = DBObj()


@app.route('/')
def hello_world():
    return render_template('basic.html', sql_obj= sql_obj.obj_list, Distance = b)


@app.route('/test', methods=['POST', 'GET'])
def upload():
    print('test start')
    if "file_urls" not in session:
        session['file_urls'] = "../../static/assets/img/samsung.jpg"
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename
            )

            # append image urls
            file_urls = photos.url(filename)

        session['file_urls'] = file_urls
        print('uploding')
        return "uploading..."
    # return dropzone template on GET request
    print('test end2')
    return 'good'


@app.route('/results')
def results():
    # set the file_urls and remove the session variable
    file_url = session['file_urls']
    a.create_sample(file_url)
    a.create_list()
    return render_template('basic.html', file_url=file_url, Distance = b)


@app.route('/start')
def start():
    sql_obj.open("model/mark.db")
    b.set_graph()
    sql_obj.obj_list = []
    for i in a.pathlist:
        sql_obj.obj_list.append(sql_obj.find(i))
    return render_template('basic.html', file_url=session['file_urls'], Distance= b, sql_obj=sql_obj.obj_list, turi = a.distance_list)


if __name__ == '__main__':
    app.run()
