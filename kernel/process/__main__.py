from pprint import pprint

from ..scheduler.fifo_scheduler import FIFOScheduler

from ..process.process_queue import ProcessQueue
from .process_manager import ProcessManager
from ..logger import KernelLogger

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

    scheduler = FIFOScheduler(queue, logger)
    scheduler.run()


if __name__ == "__main__":
    main()
