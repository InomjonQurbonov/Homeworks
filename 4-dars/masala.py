from email.encoders import encode_base64


class MycustomIterator:
    def __init__(self,start,end,step):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end:
            x = self.start
            self.start += self.step
            return x
        else:
            raise StopIteration
        
