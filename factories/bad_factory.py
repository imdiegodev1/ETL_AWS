from .abs_factory import AbsFactory
from process.bad_process import BadProcess

class BadFactory(AbsFactory):
    def create_process(self):
        self.badprocess = badprocess = BadProcess('Unknown')

        return badprocess