from .process_state import ProcessState


class Process:
    def __init__(self, pid: int, name: str, execution_time: int = 0.5):
        self.pid = pid
        self.name = name
        self.state = ProcessState.NEW
        self.execution_time = execution_time
        self.remaining_time = execution_time

    def run(self, time_slice: int):
        if self.remaining_time <= 0:
            return 0

        execution_time = min(self.remaining_time, time_slice)
        self.remaining_time -= execution_time

        return execution_time

    def __repr__(self):
        return f"Process(pid={self.pid}, name='{self.name}, state='{self.state}', remaining={self.remaining_time}))"

    def is_finished(self) -> bool:
        return bool(self.remaining_time == 0)
