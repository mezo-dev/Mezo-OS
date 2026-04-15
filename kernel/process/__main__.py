from pprint import pprint
from .process_manager import ProcessManager


def main() -> None:
    pm = ProcessManager()
    pm.create_process(name="init process")
    pm.create_process(name="shell process")
    pm.create_process(name="user process")

    pprint(pm.list_processes())
    print(pm.get_process_by_pid(pid=1))


if __name__ == "__main__":
    main()
