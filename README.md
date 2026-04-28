## 🧠 Mezo-OS | Kernel Simulation

**Mezo-OS** is an educational project that simulates how an operating system kernel works internally.
The goal is not just to build features, but to understand *how a kernel thinks*—from managing processes to sharing CPU time between them.

At this stage, the project focuses on **process management and CPU scheduling**, evolving from simple execution to realistic multitasking behavior.

---

## What Has Been Built So Far

The kernel is designed using a modular architecture, separating responsibilities into components such as the process manager, scheduler, and queue system. This keeps the system clean, scalable, and easy to extend.

A **Process Manager** is responsible for creating processes, assigning unique PIDs, and tracking their lifecycle. Each process now includes execution metadata such as total execution time and remaining time, allowing partial execution and resumption.

To control execution order, a **custom queue data structure** was implemented using a linked list. This ensures efficient enqueue and dequeue operations (O(1)) and provides a deeper understanding of how low-level data structures work.

The scheduling system has evolved into a **Round Robin Scheduler**, enabling true multitasking simulation. Instead of running processes to completion, each process receives a fixed time slice (quantum), after which it is either re-queued or terminated. This introduces fairness and prevents any single process from monopolizing the CPU.

To make the simulation more realistic, **context switching** has been introduced. The system now explicitly simulates saving the current process state and loading the next one, making CPU transitions visible through logs. A small delay is also added to represent switching overhead.

A **kernel logging system** is used throughout the project to trace execution flow, including process creation, scheduling decisions, and context switches. This makes debugging and understanding system behavior much easier.

Basic **validation and error handling** are also in place to ensure stability when dealing with invalid input or incorrect operations.

---

## Summary of Current Components

| Component             | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| Kernel Structure      | Modular design with clear separation of concerns               |
| Process Manager       | Creates and manages processes with execution metadata          |
| Process Model         | Supports execution time, remaining time, and state transitions |
| Process Queue         | Custom linked-list queue (O(1) operations)                     |
| Round Robin Scheduler | Time-sliced CPU scheduling with fair process rotation          |
| Context Switching     | Simulates saving/loading process state between executions      |
| Logging System        | Tracks kernel events and execution flow                        |
| Validation Layer      | Handles invalid input with safe checks and exceptions          |
