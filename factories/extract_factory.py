from .abs_factory import AbsFactory
from process.extract import Extract

class ExtractFactory(AbsFactory):

    def start_process(self):
        self.extract = extract = Extract()
        #extract.process = 'Extract'

        return extract

