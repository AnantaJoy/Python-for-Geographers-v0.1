from abc import ABC, abstractmethod # abstract base class

class InvalidOpeartionError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False
        
    def open(self):
        if self.opened:
            raise IOError("Stream already opened")
        self.opened = True
    
    def close(self):
        if self.opened:
            raise IOError("Stream already opened")
        self.opened = False
    
    @abstractmethod
    def read(self):
        pass

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

stream = Stream()
stream.open()
