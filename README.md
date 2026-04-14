## Mezo-OS | Kernel Simulation
is a lightweight operating system simulation that models core kernel components such as process scheduling, memory management, and system calls to demonstrate how an OS manages hardware and user programs.

| ID | Component        | Description                                                                        | Core Concept                            |
| ---- | --------------------- | ---------------------------------------------------------------------------------- | --------------------------------------- |
| 1    | Kernel Skeleton       | Create the basic structure of the kernel with modules (process, memory, scheduler) | Modular Design & Separation of Concerns |
| 2    | Process Model         | Represent a process with attributes (PID, state, priority)                         | Process Abstraction                     |
| 3    | Process Queue         | Implement a queue to hold processes waiting for execution                          | Queue (Data Structure)                  |
| 4    | Basic Scheduler       | Run processes one by one using FIFO                                                | Scheduling Algorithms (FIFO)            |
| 5    | Round Robin Scheduler | Add time-slicing and process rotation                                              | Circular Queue & Time Sharing           |
| 6    | Process States        | Add states (Ready, Running, Waiting, Terminated)                                   | Finite State Machine                    |
| 7    | Context Switching     | Simulate switching between processes                                               | Context Switching Concept               |
| 8    | System Call Interface | Create a layer for user programs to request kernel services                        | User Mode vs Kernel Mode                |
| 9    | Memory Model          | Simulate memory as an array or blocks                                              | Memory Abstraction                      |
| 10   | Memory Allocation     | Implement allocation (First Fit / Best Fit)                                        | Greedy Algorithms                       |
| 11   | Memory Deallocation   | Free memory and handle fragmentation                                               | Memory Management                       |
| 12   | Paging Simulation     | Divide memory into pages and assign to processes                                   | Paging Concept                          |
| 13   | Interrupt System      | Simulate interrupts (timer, I/O)                                                   | Interrupt Handling                      |
| 14   | Priority Scheduling   | Add priorities to processes and schedule accordingly                               | Heap / Priority Queue                   |
| 15   | Starvation Handling   | Prevent low-priority processes from being ignored                                  | Aging Algorithm                         |
| 16   | File System Model     | Simulate files and directories                                                     | Tree Data Structure                     |
| 17   | File Operations       | Implement create, read, write, delete                                              | File System Basics                      |
| 18   | Device Manager        | Simulate I/O devices (disk, keyboard)                                              | Abstraction Layer                       |
| 19   | I/O Scheduling        | Manage device requests efficiently                                                 | Scheduling (FCFS, SSTF)                 |
| 20   | Logging System        | Track kernel events and actions                                                    | Observer Pattern                        |
| 21   | Error Handling        | Handle invalid operations safely                                                   | Defensive Programming                   |
| 22   | Configuration System  | Manage kernel settings dynamically                                                 | Singleton Pattern                       |
| 23   | Performance Metrics   | Measure execution time, wait time, throughput                                      | Algorithm Analysis                      |
| 24   | Optimization Phase    | Improve scheduling, memory, and structures                                         | Time & Space Complexity                 |
| 25   | Final Integration     | Combine all modules into a working mini-kernel                                     | System Design                           |
