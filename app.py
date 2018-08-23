from flask import Flask, render_template, request, redirect
import turicreate as tc
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
import re
import PIL
from PIL import Image


app = Flask(__name__)
dropzone =  Dropzone(app)

imgframe = tc.load_sframe('model/net/img_test.sframe')
model = tc.load_model('model/net/image_model')
queryframe = tc.image_analysis.load_images('static/assets/file-upload')
queryframe = queryframe.add_row_number()
queryframe.save('model/querydata')

query_results = model.query(dataset = queryframe[0:1], k=None, radius = None, verbose = True)

pathlist=[]
cut = re.compile(r"\d{13}[.]jpg")
resultpathlist = imgframe[query_results['reference_label']]['path']
for path in resultpathlist:
    marknum = cut.findall(path)
    pathlist.append(marknum[0])


def store_image():
    for i in range(10):
        data[i]['image']._to_pil_image().save('static/assets/img/list/{}.jpg'.format(i))

# store_image()




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
    count_similar = 32700
    count_total = 2039400

@app.route('/')
def hello_world():
    return render_template('basic.html', Distance=Distance)


@app.route('/test', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save("static/assets/file-upload/"+secure_filename(f.filename))
                return 'file save'
    return 'good'


if __name__ == '__main__':
    app.run()
