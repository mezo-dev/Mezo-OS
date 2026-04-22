## 🧠 Mezo-OS | Kernel Simulation

**Mezo-OS** is an educational project that simulates the core behavior of an operating system kernel.  
The goal is to understand how an OS manages processes internally—starting from creation to execution—by building each component step by step.

At its current stage, the project focuses on **process management and basic CPU scheduling**, providing a simplified but realistic view of how a kernel operates.

---

## 🚀 What Has Been Built So Far

The foundation of the kernel has been designed with a modular structure, separating responsibilities into clear components such as the process manager, scheduler, and queue system. This makes the system easier to extend and maintain as more features are added.

A **Process Manager** has been implemented to handle the creation and tracking of processes. Each process is assigned a unique PID and initialized with a basic state, allowing us to simulate a real process lifecycle in a simplified way.

To manage execution order, a **custom queue data structure** was built from scratch using a linked list. This ensures efficient operations (O(1) enqueue and dequeue) and avoids relying on built-in abstractions, helping to better understand how data structures work internally.

On top of that, a **FIFO (First-In, First-Out) scheduler** was implemented. It simulates how the CPU picks processes from the queue and executes them sequentially. Each process transitions through basic states such as `NEW`, `RUNNING`, and `TERMINATED`, mimicking real OS behavior.

The system also includes a **simple kernel logging mechanism** to track events like process creation, execution, and errors. Additionally, **basic input validation and custom exceptions** are used to ensure the system behaves predictably and safely when handling invalid data.

---

## 🧩 Summary of Current Components

| Component        | Description |
|------------------|------------|
| Kernel Structure | Modular design separating core responsibilities |
| Process Manager  | Handles process creation, PID assignment, and storage |
| Process Queue    | Custom linked-list queue for managing execution order |
| FIFO Scheduler   | Executes processes sequentially based on arrival order |
| Logging System   | Tracks kernel events and actions |
| Validation Layer | Ensures safe input handling with custom exceptions |