from .abs_process import AbsProcess

class NullProcess(AbsProcess):

    #def __init__(self, process_name):
    #    self._process_name = process_name
    
    def message(self):
        print('Unknown process "%s",' % self._process)