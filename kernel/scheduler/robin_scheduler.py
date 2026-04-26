


from ..process.process_queue import ProcessQueue
from ..logger import KernelLogger
from ..process import Process
 
class RoundRobinScheduler:
    def __init__(self, process_queue:ProcessQueue, logger: KernelLogger, quantum: int = 2):
        self.queue = process_queue
        self.quantum = quantum
        self.logger = logger
        self.time = 0

    
    def run(self):
        self.logger.create_log(
            title="Round Robin Scheduler Started",
            message=f"Round Robin Scheduler started with quantum ({self.quantum}).",
            level="INFO"
        )

        while not self.queue.is_empty():
            process = self.queue.dequeue()

            if process is None:
                continue
            self._execute(process)

            self.logger.create_log(
                title="Process Executed",
                message=f"Executed process {process.pid} for {self.quantum} time units.",
                level="INFO"
            )
        
    def _execute(self, process: Process):
        pass