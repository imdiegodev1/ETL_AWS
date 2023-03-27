from .abs_factory import AbsFactory
from process.load import Load

class ExtractFactory(AbsFactory):

    def start_load(self):
        self.process = process = Load()
        process.process = 'Load'

        return process
