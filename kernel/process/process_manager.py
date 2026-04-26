from ..logger import KernelLogger
from .process import Process
from .validator import ProcessValidator


class ProcessManager:
    def __init__(self, logger: KernelLogger | None = None):
        self.logger = logger or KernelLogger()
        self.processes = []
        self.next_pid = 1

    def create_process(self, name: str) -> Process:
        process_validator = ProcessValidator(name=name, processes=self.processes)
        process_validator.validate()

        process = Process(pid=self.next_pid, name=name)
        self.processes.append(process)
        self.next_pid += 1

        self.logger.create_log(
            title="Created Process...",
            message=f"Process #{process.pid} '{process.name}' has been created.",
            level="INFO",
        )
        return process

    def list_processes(self) -> list[Process]:
        return self.processes

    def get_process_by_pid(self, pid: int) -> Process | None:
        left, right = 0, len(self.processes) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.processes[mid].pid == pid:
                return self.processes[mid]
            elif self.processes[mid].pid < pid:
                left = mid + 1
            else:
                right = mid - 1
        return None
