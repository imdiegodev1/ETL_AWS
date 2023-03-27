from .abs_factory import AbsFactory
from process.bad_process import BadProcess

class NullFactory(AbsFactory):
    def create_process(self):
        self.nullprocess = nullprocess = BadProcess('Unknown')

        return nullprocess