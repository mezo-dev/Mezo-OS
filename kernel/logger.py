from datetime import datetime


class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'


LEVEL_COLORS = {
    "INFO": Colors.GREEN,
    "WARN": Colors.YELLOW,
    "ERROR": Colors.RED,
}


class KernelLogger:
    def __init__(self):
        self.logs: list[dict] = []

    def create_log(self, *, title: str, message: str, level: str = "INFO") -> None:
        timestamp = datetime.now().isoformat(timespec="seconds")
        self.logs.append({
            "timestamp": timestamp,
            "level": level,
            "title": title,
            "message": message,
        })
        color = LEVEL_COLORS.get(level, Colors.GREEN)
        print(f"{color}[{timestamp}] {level} {title}: {message}{Colors.RESET}")

    def get_logs(self) -> list[dict]:
        return self.logs

    # get log by title and add id for each object

# if __name__ == "__main__":
#     test = KernelLogger()
#     test.create_log(
#         title="Process management",
#         message="The process failed because something happens!",
#         level="INFO",
#     )
