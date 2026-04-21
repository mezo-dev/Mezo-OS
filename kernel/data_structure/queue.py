from typing import Any

from ..logger import KernelLogger
from ..process import Process
class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, logger: KernelLogger = None):
        self.head = None
        self.tail = None
        self.size = 0
        self.logger = logger
    
    def enqueue(self, item: Process) -> None:
        new_node = Node(item)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

        if self.logger:
            self.logger.create_log(
                title=f"Enqueue: PID={item.pid}",
                message=f"Process {item.name} (PID={item.pid}) has been enqueued.",
                level="INFO",
            )

