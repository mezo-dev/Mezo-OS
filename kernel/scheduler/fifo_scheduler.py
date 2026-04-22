"""
Steps: 
    - Pull process from queue
    - Mark it as RUNNING
    - Simulate execution
    - Mark it as TERMINATED
    - Move to next process
"""


from ..process.process_state import ProcessState
from ..process.process_queue import ProcessQueue
from ..logger import KernelLogger
from ..process import Process


class FIFOScheduler:
    def __init__(self, process_queue: ProcessQueue, logger: KernelLogger):
        self.process_queue = process_queue
        self.logger = logger


    def run(self):
        self.logger.create_log(
            title="FIFO Scheduler Started",
            description="The FIFO Scheduler has started executing processes.",
            level="INFO"
        )

        while not self.process_queue.is_empty():
            process = self.process_queue.dequeue()

            if process is None:
                continue 
                
            self._execute(process)
        self.logger.create_log(
            title="FIFO Scheduler Finished",
            description="The FIFO Scheduler has finished executing all processes.",
            level="INFO"
        )
    
    def _execute(self, process: Process):
        process.state = ProcessState.RUNNING
        self.logger.create_log(
            title=f"Process {process.pid} Running",
            description=f"Process {process.pid} ({process.name}) is now running.",
            level="INFO"
        )

        print(f"Executing Process {process.pid} ({process.name})...")

        process.state = ProcessState.TERMINATED
        self.logger.create_log(
            title=f"Process {process.pid} Terminated",
            description=f"Process {process.pid} ({process.name}) has terminated.",
            level="INFO"
        )