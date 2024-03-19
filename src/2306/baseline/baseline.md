# Baseline overview

The Baseline stage is the first formal learning stage of the "One Student One Chip".
There are two goals in the Baseline stage
* Running the NES game Super Mario on a processor designed by yourself
* Understand in depth how Super Mario runs on the processor you designed

![image](./mario.png)

Specifically, the tasks in the Baseline stage can be divided into the following parts:
1. Build infrastructures. Infrastructures are tools and methods that help improve debugging efficiency.
If you have heard about the DiffTest (differential testing) mechanism of the third term of the "One Student One Chip",
Then you should probably understand how important infrastructure is for a project of a certain scale.
In addition to DiffTest, you will also implement a simple debugger and various tracing tools.
These infrastructures will accompany you throughout the "One Student One Chip":
Even in stages A and S, you will find that they can still greatly improve debugging efficiency;
What's more? Without these infrastructures, you will have to pay a huge price if you want to survive the S stage.
1. Implement an RV32E single-cycle processor.
But you will first implement an RV32IM (yes, RV32IM) simulator.
Understand the behavior of RISC-V instructions and programs without considering RTL implementation details,
Then apply these understandings to the real processor implemented in RTL.
1. Implement input and output functionality to the single-cycle processor.
After that, you can run Super Mario on the processor you designed.
1. Implement a simple exception handling mechanism and run the RT-Thread operating system
1. Implement bus and connect to SoC
1. Change the processor from a single-cycle processor to a pipelined processor.

> #### caution::Isn’t it enough just learn how to use tools? Why do I have to spend so much time implementing tools?
> If you really have such questions, you most likely do not understand the meaning of "using the right tools to solve problems", which may be reflected in the following aspects
> 1. Not proactively looking for the right tools to improve work efficiency (such as backing up projects by copying and pasting them instead of using version control tools)
> 1. Even if you know how to use certain tools, you are not willing to spend some time to understand the tools in depth.
> 1. If the tool is open source, you have never thought about adding some customized functions.
> 1. If there was no such tool, you would never even think of writing them by yourself.
>
> Developers who truly understand the meaning of tools will not feel that it is a waste of time:
> Taking the time to understand/implement the tools now will help you earn back your time exponentially in the future.
