from .process import Process


class ProcessManager:
    def __init__(self):
        self.processes = []
        self.next_pid = 1
    
    def create_process(self, name: str) -> Process:
        for p in self.processes: # move it to validator as well 
            if p.name == name:
                raise NameError("Process name already exsting!")
        
        process = Process(pid=self.next_pid, name=name)
        self.processes.append(process)
        self.next_pid += 1
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