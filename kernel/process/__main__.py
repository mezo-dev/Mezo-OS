
from ..logger import KernelLogger
from ..process.process_queue import ProcessQueue
from ..scheduler.fcfs_scheduler import FCFSScheduler
from .process_manager import ProcessManager
from ..scheduler.robin_scheduler import RoundRobinScheduler
logger = KernelLogger()


def main() -> None:
    pm = ProcessManager(logger)
    queue = ProcessQueue(logger)

    p1 = pm.create_process(name="Chrome")
    p2 = pm.create_process(name="VSCode")
    p3 = pm.create_process(name="Terminal")
    p4 = pm.create_process(name="Spotify")

    queue.enqueue(p1)
    queue.enqueue(p2)
    queue.enqueue(p3)
    queue.enqueue(p4)

    scheduler = FCFSScheduler(queue, logger)
    scheduler.run()

    scheduler = RoundRobinScheduler(queue, logger)
    scheduler.run()


if __name__ == "__main__":
    main()
