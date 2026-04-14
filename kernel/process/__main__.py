from .process_manager import ProcessManager


def main():
    manager = ProcessManager()
    p = manager.create_process("init")
    print(f"Created: pid={p.pid}, name={p.name}")
    print(f"Processes: {manager.list_processes()}")


if __name__ == "__main__":
    main()
