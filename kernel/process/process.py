from .process_state import ProcessState


class Process:
    def __init__(self, pid: int, name: str):
        self.pid = pid
        self.name = name
        self.state = ProcessState.NEW
        self.execution_time = 2

    def __repr__(self):
        return f"Process(pid={self.pid}, name='{self.name}, state='{self.state}')"