from .process_manager import ProcessManager
from pprint import pprint

pm = ProcessManager()

pm.create_process(name="init process")
pm.create_process(name="shell process")
pm.create_process(name="user process")
pm.create_process(name="user process")


pprint(pm.list_processes())
print(pm.get_process_by_pid(pid=1))