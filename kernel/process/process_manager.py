from .process import Process


class ProcessManager:
    def __init__(self):
        self.processes = []
        self.next_pid = 1
    
    def create_process(self, name: str) -> Process:
        process = Process(pid=self.next_pid, name=name)
        self.processes.append(process)
        self.next_pid += 1
        return process
    
    def list_processes(self) -> list[Process]:
        return self.processes
    
    