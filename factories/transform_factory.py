from .abs_factory import AbsFactory
from process.transform import Transform

class TransformFactory(AbsFactory):

    def start_transform(self):
        self.process = process = Transform()
        process.process = 'Transform'

        return process
