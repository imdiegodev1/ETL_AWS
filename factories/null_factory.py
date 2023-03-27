from .abs_factory import AbsFactory
from process.bad_process import NullProcess

class NullFactory(AbsFactory):
    def create_process(self):
        self.nullprocess = nullprocess = NullProcess('Unknown')

        return nullprocess