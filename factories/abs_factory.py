import abc

class AbsFactory(abc.ABC):

    @abc.abstractmethod
    def start_process(self):
        pass