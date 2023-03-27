from .abs_process import AbsProcess

class Extract(AbsProcess):

    def connect(self):
        print('connected to source')

    def extract(self):
        print('extracted and saved in a byte object')