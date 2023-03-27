from .abs_factory import AbsFactory
from process.extract import Extract

class ExtractFactory(AbsFactory):

    def start_extraction(self):
        self.process = process = Extract()
        process.process = 'Extract'

        return process

