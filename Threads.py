from threading import Thread

class GenericThread(Thread):
    def __init__(self, func, args):
        Thread.__init__(self)
        self._func = func
        self._args = args

    def run(self):
        self._func(self._args)
    
