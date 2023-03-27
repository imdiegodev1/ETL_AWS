from .abs_process import AbsExtract

class Extract(AbsExtract):

    def connect(self):
        print('connected to source')

    def extract(self):
        print('extracted and saved in a byte object')