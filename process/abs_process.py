import abc

class AbsProcess(abc.ABC):

    @property
    def process(self):
        return self._process

    @process.setter
    def extraction(self, process):
        self._process = process

    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def extract(self):
        pass
    
    #@process.setter
    #def transform(self, process):
    #    self._process = process
#
    #@abc.abstractmethod
    #def transfor_process_1(self):
    #    pass
#
    #@abc.abstractmethod
    #def transfor_process_2(self):
    #    pass


class AbsLoad(AbsProcess):
    
    @property
    def process(self):
        return self._process

    @process.setter
    def load(self, process):
        self._process = process

    @abc.abstractmethod
    def connect_s3(self):
        pass

    @abc.abstractmethod
    def load_s3(self):
        pass