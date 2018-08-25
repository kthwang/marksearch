from flask import Flask, render_template, request, redirect, session, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
import turicreate as tc
from turicreate import SFrame, SArray
from flask_dropzone import Dropzone
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

import re
import PIL
from PIL import Image


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

dropzone =  Dropzone(app)
db = SQLAlchemy(app)




photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

# class Turi:
#     queryframe = tc.image_analysis.load_images('static/assets/file-upload')
#     queryframe = queryframe.add_row_number()
#     queryframe.save('model/querydata')
#     query_results = model.query(dataset = queryframe[0:1], k=None, radius = None, verbose = True)
#     pathlist=[]
#     cut = re.compile(r"\d{13}[.]jpg")
#     resultpathlist = imgframe[query_results['reference_label']]['path']
#     for path in resultpathlist:
#         marknum = cut.findall(path)
#         pathlist.append(marknum[0])


class TuriObj:
    def __init__(self, imgUrl):
        self.imgframe = tc.load_sframe('model/net/img_test.sframe')
        self.model = tc.load_model('model/net/image_model')
        self.sample = tc.Image(imgUrl, format='auto')
        self.results = SFrame()
        self.rows = SArray()

    def create_list(self):
        self.results = self.model.query(self.sample, k=None)
        self.rows = self.results['reference_label']
        # for i in range(10):
        #     self.imgframe.filter_by(self.rows, 'id')[i]['image']._to_pil_image().save('static/assets/img/list/{}.jpg'.format(i))
        return self.results

a = TuriObj('static/assets/file-upload/test.jpg')
a.create_list()

data = a.results.to_dataframe()
print(data)


class Distance :
    top8 = 8
    distance_top = [1, 2, 3, 4, 5, 6, 7, 8]
    distance_avg = 10.73
    distance_max = 32
    distance_min = 7
    count_almost_same = 72
    count_similar = 3270
    count_total = 2039400
    distance_top = [1, 2, 3, 4, 5, 6, 7, 8]
    distance_similar_b = [3, 4, 5, 6, 7, 8, 9, 10]
    distance_total = [
        [0.2, 0.5, 0.8, 6, 7, 14.5, 15],
        [0.2, 1, 11.8, 14, 12.4, 1, 0.2]
    ]
    distance_same = [
        [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6],
        [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9]
    ]
    distance_similar = [
        [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6, 4.7, 3, 5],
        [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9, 10, 12, 13]
    ]

    def set_graph(self):
        self.top8 = data.head(n=8).distance.mean()
        self.distance_avg = data['distance'].mean()
        self.distance_max = data['distance'][len(data) - 1]
        self.distance_min = data['distance'][0]
        self.count_total = len(data)
        self.count_almost_same = data.loc[data['distance'] < (self.distance_min+((self.distance_max-self.distance_min)/739))].distance.count()
        self.count_similar = data.loc[data['distance'] < (self.distance_min+((self.distance_max-self.distance_min)/44))].distance.count()


        self.distance_total = [
            [
                (((data.iloc[int(self.count_total / 740)].distance) - self.distance_min) * 16) / (self.distance_max - self.distance_min),
                (((data.iloc[int(self.count_total / 44)].distance) - self.distance_min) * 16) / (self.distance_max - self.distance_min),
                (((data.iloc[int(self.count_total / 6)].distance) - self.distance_min) * 16) / (self.distance_max - self.distance_min),
                (((data.iloc[int(self.count_total / 2)].distance) - self.distance_min) * 16) / (self.distance_max - self.distance_min),
                (((data.iloc[int(self.count_total * 5 / 6)].distance) - self.distance_min) * 16) / (self.distance_max - self.distance_min),
                (((data.iloc[int(self.count_total * 43 / 44)].distance) - self.distance_min) * 16) / (self.distance_max - self.distance_min),
                (((data.iloc[int(self.count_total * 739 / 740)].distance) - self.distance_min) * 16) / (self.distance_max - self.distance_min)
            ],
            [
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 740))].distance.count()) * 16 / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 44))].distance.count()) * 16 / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 6))].distance.count()) * 16 / self.count_total,
                (data.loc[data['distance'] < (self.distance_min + ((self.distance_max - self.distance_min) / 2))].distance.count()) * 16 / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 5 / 6))].distance.count()) * 16 / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 43 / 44))].distance.count()) * 16 / self.count_total,
                (data.loc[data['distance'] > (self.distance_min + ((self.distance_max - self.distance_min) * 739 / 740))].distance.count()) * 16 / self.count_total
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
            data.iloc[int(Distance.count_similar * 1 / 8)].distance,
            data.iloc[int(Distance.count_similar * 2 / 8)].distance,
            data.iloc[int(Distance.count_similar * 3 / 8)].distance,
            data.iloc[int(Distance.count_similar * 4 / 8)].distance,
            data.iloc[int(Distance.count_similar * 5 / 8)].distance,
            data.iloc[int(Distance.count_similar * 6 / 8)].distance,
            data.iloc[int(Distance.count_similar * 7 / 8)].distance,
            data.iloc[int(Distance.count_similar)].distance
        ]

b = Distance()
b.set_graph()



# class Distance:
#     distance_total=[
#         [0.2,0.5,0.8,6,7,14.5,15],
#         [0.2,1,11.8,14,12.4,1,0.2]
#     ]
#     distance_same=[
#         [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6],
#         [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9]
#     ]
#     distance_similar=[
#         [0, 2, 3.5, 4, 8, 3, 4, 6, 2, 6, 4.7, 3, 5],
#         [0, 6, 5.5, 3, 3, 11, 7, 4, 7, 9, 10, 12, 13]
#     ]
#     distance_avg = 10.73
#     distance_max = 15
#     distance_min = 1
#     count_almost_same = 72
#     count_similar = 32700
#     count_total = 2039400

@app.route('/')
def hello_world():
    sample = ''
    return render_template('basic.html', Distance = b)


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
    TuriObj(file_url).create_list()
    return render_template('basic.html', file_url=file_url, Distance=b)

@app.route('/start')
def start():
    pass

if __name__ == '__main__':
    app.run()
