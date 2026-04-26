


from ..process.process_state import ProcessState
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
        process.state = ProcessState.RUNNING
        self.logger.create_log(
            title="Process Start Executing",
            message=f"[Time {self.time}], Running PID [{process.pid}], Remaining Time: {process.remaining_time}",
            level="INFO"
        )

        executed_time = process.run(self.quantum)
        self.time += executed_time

        self.logger.create_log(
            title=f"Execution Process {process.name} For {executed_time} Time Units",
            message=f"[Time {self.time}], Executed PID [{process.pid}] for {executed_time} time units, Remaining Time: {process.remaining_time}",
            level="INFO"
        )

        if process.is_finished():
            process.state = ProcessState.TERMINATED
            self.logger.create_log(
                title=f"Process {process.name} Terminated",
                message=f"[Time {self.time}], Process PID [{process.pid}] has finished execution and is terminated.",
                level="INFO"
            )
        else:
            process.state = ProcessState.READY
            self.queue.enqueue(process)
            self.logger.create_log(
                title=f"Process {process.name} Re-queued",
                message=f"[Time {self.time}], Process PID [{process.pid}] is re-queued with remaining time {process.remaining_time}.",
                level="INFO"
            )

