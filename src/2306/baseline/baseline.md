# Baseline overview

The Baseline stage is the first formal learning stage of "One Student One Chip".
There are two goals in the Baseline stage
* Running the NES game Super Mario on a processor designed by yourself
* Understand in depth how Super Mario runs on the processor you designed

![image](./mario.png)

Specifically, the tasks in the Baseline stage can be divided into the following parts:
1. Build infrastructures. Infrastructures are tools and methods that help improve debugging efficiency.
如果你已经听说过第三期"一生一芯"的DiffTest(差分测试)机制,
相信你也大概能够明白基础设施对于一个有一定规模的项目来说多么的重要了.
除了DiffTest之外, 你还会实现简易调试器和各种trace(踪迹)工具,
这些基础设施将会伴随你整个"一生一芯"的学习:
即使到了A阶段和S阶段, 你会发现它们仍然可以大幅提升调试的效率;
甚至可以说, 如果没有这些基础设施, 你想要在S阶段中存活下来, 将要付出巨大的代价.
1. 设计一个支持RV32E的单周期处理器.
不过你会首先实现一个RV32IM(对, 是RV32IM)的模拟器,
在不接触RTL实现细节的情况下理解RISC-V指令和程序的行为,
然后再把这些理解迁移到RTL实现的真实处理器中.
1. 为单周期处理器添加输入输出功能.
这样以后, 你就可以在自己设计的处理器上运行超级玛丽了.
1. 实现简单的异常处理机制, 运行RT-Thread操作系统
1. 实现总线, 接入SoC
1. 将处理器改成流水线结构

> #### caution::Isn’t it enough just learn how to use tools? Why do I have to spend so much time implementing tools?
> If you really have such questions, you most likely do not understand the meaning of "using the right tools to solve problems", which may be reflected in the following aspects
> 1. Not proactively looking for the right tools to improve work efficiency (such as backing up projects by copying and pasting them instead of using version control tools)
> 1. Even if you know how to use certain tools, you are not willing to spend some time to understand the tools in depth.
> 1. If the tool is open source, you have never thought about adding some customized functions.
> 1. If there was no such tool, you would never even think of writing them by yourself.
>
> Developers who truly understand the meaning of tools will not feel that it is a waste of time:
> Taking the time to understand/implement the tools now will help you earn back your time exponentially in the future.
