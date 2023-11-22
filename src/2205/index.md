---
sidebarDepth: 3
sidebar: auto
pageClass: "ysyx-index"
---

# Translation in progress

<!-- # 第五期"一生一芯"课程主页

* 课时: 每周六19:00~21:00
  * [B站直播](https://live.bilibili.com/24416626) | [录播链接](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=690279)
* 答疑: 每周日19:00~20:00 (通过预学习答辩后由助教通知) -->
<!-- * [报名流程](about/enroll/student.md) | [报名常见问题](about/enroll/faq.md) -->

<!-- ## 课件和讲义

0. `C` = C语言(程序/模拟器/系统软件) | `R` = RISC-V指令集 | `P` = 处理器设计 | `T` = 工具
   <hr color=#987cb9 size=4 />
   <div align=center>预学习阶段</div>
1. 🎬["一生一芯"概述](https://ysyx.oscc.cc/slides/2205/01.html#/) | 📄[如何科学地提问](prestudy/0.1.md)
1. 🎬[工具是第一生产力——Linux入门教程`T`](https://ysyx.oscc.cc/slides/2205/02.html#/) | 📄[Linux系统安装和基本使用](prestudy/0.2.md)
1. 🎬[计算机系统的状态机模型`C` `R` `P`](https://ysyx.oscc.cc/slides/2205/03.html#/) | 📄[复习C语言](prestudy/0.3.md)
1. 🎬[从C语言到二进制程序`C` `T`](https://ysyx.oscc.cc/slides/2205/04.html#/)
1. 🎬[程序的执行和模拟器`C` `R` `P`](https://ysyx.oscc.cc/slides/2205/05.html#/) | 📄[搭建verilator仿真环境](prestudy/0.4.md) | 📄[数字电路基础实验](prestudy/0.5.md)
1. 🎬[NEMU代码导读`C` `T`](https://ysyx.oscc.cc/slides/2205/06.html#/)| 📄[完成PA1](prestudy/0.6.md)
   <hr color=#987cb9 size=4 />
   <div align=center>B阶段</div>
1. 🎬[RISC-V指令集`C` `R` `P`](https://ysyx.oscc.cc/slides/2205/07.html#/) | 📄[支持RV64IM的NEMU](baseline/1.1.md)
1. 🎬[程序的机器级表示`C` `R`](https://ysyx.oscc.cc/slides/2205/08.html#/)
1. 🎬[RISC-V单周期处理器设计`P`](https://ysyx.oscc.cc/slides/2205/09.html#/) | 📄[用RTL实现最简单的处理器](baseline/1.2.md)
1. 🎬[Abstract Machine裸机运行时环境`C`](https://ysyx.oscc.cc/slides/2205/10.html#/) | 📄[运行时环境和基础设施](baseline/1.3.md)
1. 🎬[ELF文件和链接`C` `R`](https://ysyx.oscc.cc/slides/2205/11.html#/)
1. 🎬[工具和基础设施`T`](https://ysyx.oscc.cc/slides/2205/12.html#/) | 📄[支持RV64IM的单周期NPC](baseline/1.4.md)
1. 🎬[设备和输入输出`C` `R` `P`](https://ysyx.oscc.cc/slides/2205/13.html#/) | 📄[设备和输入输出](baseline/1.5.md)
1. 🎬[调试技巧选讲`T`](https://ysyx.oscc.cc/slides/2205/14.html#/)
   <hr color=#987cb9 size=4 />
   <div align=center>A阶段</div>
1. 🎬[异常处理`C` `R` `P`](https://ysyx.oscc.cc/slides/2205/15.html#/) | 📄[简单的异常处理机制](advanced/2.1.md)
1. 🎬[计算机系统软件栈`C`](https://ysyx.oscc.cc/slides/2205/16.html#/) | 📄[用户程序与系统调用](advanced/2.2.md) | 📄[精彩纷呈的用户程序](advanced/2.3.md)
1. 🎬[总线选讲`P`](https://ysyx.oscc.cc/slides/2205/17.html#/) | 📄[总线](advanced/2.4.md)
1. 🎬[SoC计算机系统`P`](https://ysyx.oscc.cc/slides/2205/18.html#/) | 📄[SoC计算机系统](advanced/2.5.md)
1. 🎬[性能和缓存`P`](https://ysyx.oscc.cc/slides/2205/19.html#/) | 📄[性能计数器](advanced/2.6.md) | 📄[Cache简介](advanced/2.7.md)
1. 🎬[功能单元设计`P`](https://ysyx.oscc.cc/slides/2205/20.html#/) | 📄[乘除法功能单元](advanced/2.8.md)
1. 🎬[流水线处理器`P`](https://ysyx.oscc.cc/slides/2205/21.html#/) | 📄[流水线处理器](advanced/2.9.md)
   <hr color=#987cb9 size=4 />
   <div align=center>S阶段(香山主题邀请报告)</div>
1. 🎬[香山处理器前端`P`](https://www.bilibili.com/video/BV17e4y1c719/)
1. 🎬[香山乱序流水`P`](https://www.bilibili.com/video/BV13b411X7i4/)
1. 🎬[香山乱序访存`P`](https://www.bilibili.com/video/BV1hs4y1V7gV/)
1. 🎬[香山缓存`P`](https://www.bilibili.com/video/BV1Q24y147AX/)
1. 🎬[高性能处理器的性能迭代加速`P` `T`](https://www.bilibili.com/video/BV1rN411K7jn/)
1. 🎬[香山处理器敏捷开发方法与工具`T`](https://www.bilibili.com/video/BV1Mh411g7Vf/)
   <hr color=#987cb9 size=4 />
   <div align=center>课程总结</div>
1. 🎬[课程总结](https://ysyx.oscc.cc/slides/2205/28.html#/)

* 完整的讲义可通过页面右上方导航栏查看
* S阶段讲义内容仍然在🕊


> #### info::页面加载条卡住了？
>
> 跳转页面时, 如果进度条卡住 3 秒以上, 很可能是由于我们推送了网页版本更新.<br>
> 鉴于我们还在频繁更新、修订文档, 近期可能会比较容易遇到跳转卡住的情况.<br>
> 遇到这种情况, 只需要 __`刷新整个页面`__ 即可继续学习咯

## 其他资源

* [提问模板](misc/ask.md)

## 活动记录

* 2022/11/20 - [从软件工程视角看芯片开源与敏捷设计(包云岗)](https://www.bilibili.com/video/BV1Dd4y1474D/)
* 2022/08/28 - [第一届“一生一芯”技术论坛暨第五期启动会](../events/20220828-1st-tech-forum.md)
* 2022/03/12 - [软硬件协同能力在芯片设计中的应用(金越, 胡博涵, 高泽宇)](https://www.bilibili.com/video/BV1334y187zC/) -->
