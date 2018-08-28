import turicreate as tc
from turicreate import SFrame, SArray
import re

class TuriObj:
    def __init__(self):
        self.imgframe = tc.load_sframe('model/final/final.sframe')
        self.model = tc.load_model('model/final/final_model')
        self.sample = tc.Image()
        self.results = SFrame()
        self.rows = SArray()
        self.pathlist = []
        self.distance_list = []

    def create_sample(self, imgUrl):
        self.sample = tc.Image(imgUrl, format='auto')

    def create_list(self):
        self.pathlist=[]
        self.distance_list = []
        self.results = self.model.query(self.sample, k=None)
        self.rows = self.results['reference_label']
        path_cutter = re.compile(r"\d{13}")
        for i in range(10):
            pathstr = str(self.imgframe[self.imgframe['id'] == self.results['reference_label'][i]]['path'])
            self.pathlist.append(path_cutter.findall(pathstr)[0])
            self.distance_list.append(float(self.results['distance'][i]))
        return self.results