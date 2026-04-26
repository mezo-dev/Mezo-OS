from ..data_structure.queue import Queue
from ..logger import KernelLogger
from .process import Process


class ProcessQueue:
    def __init__(self, logger: KernelLogger):
        self.queue = Queue(logger)

    def enqueue(self, process: Process):
        self.queue.enqueue(process)

    def dequeue(self):
        return self.queue.dequeue()

    def peek(self):
        return self.queue.peek()

    def is_empty(self):
        return self.queue.is_empty()
