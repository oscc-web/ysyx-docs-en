---
sidebarDepth: 3
sidebar: auto
pageClass: "ysyx-index"
---

<!-- # 第六期"一生一芯"课程主页 -->
# Sixth "Ysyx" Program Home Page

<!-- * 课时: 每周六15:00~17:00
  * [B站直播](https://live.bilibili.com/24416626) | [录播链接](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=1523995) -->
* Time: Every Saturday 15:00~17:00 China Standard Time
  * [Bilibil Live](https://live.bilibili.com/24416626) | [recording](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=1523995)

<!-- ## 学习目标 -->
## Learning Objectives

<!-- "一生一芯"将会培养大家的综合能力.
大家完成学习之后, 将会对以下问题有一定的认识:
1. 处理器是如何设计的?
1. 程序是如何在计算机上运行的?
1. 如何对处理器的性能进行优化?
1. 如何使用/设计正确的工具高效地进行调试?
1. 如何自己编写测试用例进行单元测试?
1. RTL设计如何生成可流片的版图? -->
"Ysyx" will develop your general skills.
At the end of the course, you will have a better understanding of the following questions:
1. how processors are designed?
1. how programs run on computers?
1. how to optimize the performance of a processor?
1. how to use/design the right tools for efficient debugging?
1. how to write your own test cases for unit testing?
1. how does an RTL design generate a flowable layout?

<!-- 我们将会引导大家设计一款RISC-V流水线处理器,
并在自己设计的处理器上运行操作系统,
在操作系统上运行真实游戏.
达成指标的处理器将可以接入到SoC, 并获得流片机会. -->
We will guide you to design a RISC-V pipeline processor.
Run an operating system on your processor.
Run a real game on the OS.
The processor that achieves the target will be connected to the SoC and will be given the opportunity to tapeout.

<!-- ## 教学资源 -->
## Learning Resource

<!-- * 可点击图标跳转到相应资源
* 完整的讲义可通过页面右上方导航栏查看
* S阶段讲义内容仍然在🕊 -->
* Icons can be clicked to jump to the appropriate resource
* Complete handouts can be viewed via the navigation bar at the top right of the page
* The content of the Stage S handout is still available 🕊

<!-- `C` = C语言(程序/模拟器/系统软件) | `R` = RISC-V指令集 | `P` = 处理器设计 | `T` = 工具 -->
`C` = C language (program/simulator/system software) | `R` = RISC-V instruction set | `P` = processor design | `T` = tools

<style scoped type="text/css">
	@media (max-width: 719px) {
		table {
			font-size: 3vw
		}
	}
	@media (min-width: 720px) {
		[task] {
			width: 20em
		}
	}
	table {
		display: table;
		vertical-align: center;
		counter-reset: week;
	}
	table > * {
		min-width: 100%;
	}
	td {
		vertical-align: center;
		text-align: center;
	}
	table [_],
	table [x] {
		padding: 0;
		width: 3.6em;
	}
	[stage-title] {
		word-break:break-all;
		padding: 1em;
	}
	thead {
		position: sticky;
		/* Don't forget this, required for the stickiness */
		top: var(--navbar-height);
		/* Styles */
		padding-top: 0.5em;
		padding-bottom: 0.5em;
		backdrop-filter: contrast(0.5) blur(4px) brightness(120%);
	}
	[task] {
		padding-left: 0.8em;
		padding-right: 0.8em;
		text-align: left;
	}
	/* Auto increment number inside week column */
	[week] {
		width: 2.1em;
	}
	td[week]::before {
		counter-increment: week;
		content: counter(week);
	}
	/* Place a checkmark inside <td x> (short hand for <td xked>) */
	td[x]::before {
		content: '✓';
	}
	td[x] {
		background-color: hsla(var(--hue), calc(2 * var(--saturation)), 50%, 0.1) !important;
	}
	/* Coloring by style */
	.Achievement td {
		font-weight: bold;
		line-height: 1em;
		background-color: hsla(100, 100%, 30%, 0.3) !important;
		/* border-left: 12px Green solid; */
	}
	tbody > tr {
		--hue: 0;
		--saturation: 50%;
		background-color: hsla(var(--hue), var(--saturation), 50%, 0.1) !important;
	}
	.Prestudy {
		--hue: 000;
	}
	.Stage-B {
		--hue: 110;
	}
	.Stage-A {
		--hue: 220;
	}
	.Stage-S {
		--hue: 330;
	}
	.Other-Topic {
		--saturation: 0%;
	}
</style>
<table id="schedule-table">
	<thead>
		<tr>
			<th _>Stage</th> <th week>ID</th>
			<th>Task</th> <th>Handouts</th> <th>Slides</th> <th>Recording</th>
			<th _>C</th> <th _>R</th> <th _>P</th> <th _>T</th>
		</tr>
	</thead>
	<tbody>
		<tr class="Prestudy">
			<td stage-title rowspan="8">pre-study stage</td>
			<td week></td> <td task>How to ask questions scientifically</td>
            <td _><a href="2306/prestudy/0.1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/01.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV14F411975K" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Prestudy">
			<td week></td> <td task>Linux system installation and basic usage</td>
            <td _><a href="2306/prestudy/0.2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/02.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1vF4119726" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Prestudy">
			<td week></td> <td task>State machine models of computer systems</td>
            <td _> - </td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/03.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1oN411Y7FK" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Prestudy">
			<td week></td> <td task>Reviewing the C language</td>
            <td _><a href="2306/prestudy/0.3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/04.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV13z4y147mB" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Prestudy">
			<td week></td> <td task>Program execution and simulators</td>
            <td _> - </td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/05.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Rm4y1p7Cg" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Prestudy">
			<td week></td> <td task>Build a verilator simulation environment</td>
            <td _><a href="2306/prestudy/0.4.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td x></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Prestudy">
			<td week></td> <td task>Basic Digital Circuit Experiment</td>
            <td _><a href="2306/prestudy/0.5.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/06.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ZH4y1Q7Cv" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Prestudy">
			<td week></td> <td task>Complet PA1</td>
            <td _><a href="2306/prestudy/0.6.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/07.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1up4y1j7Ji" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Achievement">
			<td colspan="10"><i class="fa fa-flag"></i>Application for admission defense</td>
		</tr>
		<tr class="Stage-B">
			<td stage-title rowspan="14">basic level</td>
			<td week></td> <td task>NEMU with RV32IM support</td>
            <td _><a href="2306/baseline/1.1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/08.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV15h4y1A7Up" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Machine-level representation of programs (part 1)</td>
            <td _> - </td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/09.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ow411275B" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Machine-level representation of programs (part 2)</td>
            <td _> - </td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/10.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV19H4y1d7Yi" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Simplest processor implementation with RTL</td>
            <td _><a href="2306/baseline/1.2.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>AM Runtime Environment</td>
            <td _><a href="2306/baseline/1.3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/11.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Vu4y1s73Y" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Tools and infrastructure</td>
            <td _> - </td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/12.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1RM411Q7Au" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Single-cycle NPC with RV32E support</td>
            <td _><a href="2306/baseline/1.4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/13.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1rc411f7mK" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td x></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>ELF files and linking</td>
            <td _> - </td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/14.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Ly4y1w7hn" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Devices and inputs/outputs</td>
            <td _><a href="2306/baseline/1.5.html" target="_blank">📚</a></td>
            <td _> </td>
            <td _> </td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Exception handling and RT-Thread</td>
            <td _><a href="2306/baseline/1.6.html" target="_blank">📚</a></td>
            <td _> </td>
            <td _> </td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Bus</td>
            <td _><a href="2306/baseline/1.7.html" target="_blank">📚</a></td>
            <td _> </td>
            <td _> </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>SoC computer systems</td>
            <td _><a href="2306/baseline/1.8.html" target="_blank">📚</a></td>
            <td _> </td>
            <td _> </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Performance and Simple Caching</td>
            <td _><a href="2306/baseline/1.9.html" target="_blank">📚</a></td>
            <td _> </td>
            <td _> </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>Pipeline</td>
            <td _><a href="2306/baseline/1.10.html" target="_blank">📚</a></td>
            <td _> </td>
            <td _> </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="10"><i class="fa fa-flag"></i>Accomplish stage B tapeout</td>
		</tr>
		<tr class="Stage-A">
			<td stage-title rowspan="4">advanced stage</td>
			<td week></td> <td task>under construction</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>under construction</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>under construction</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>under construction</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="10"><i class="fa fa-flag"></i>Accomplish stage A tapeout</td>
		</tr>
	</tbody>
</table>
<!-- End of table -->

<!-- > #### info::页面加载条卡住了？
>
> 跳转页面时, 如果进度条卡住 3 秒以上, 很可能是由于我们推送了网页版本更新.<br>
> 鉴于我们还在频繁更新、修订文档, 近期可能会比较容易遇到跳转卡住的情况.<br>
> 遇到这种情况, 只需要 __`刷新整个页面`__ 即可继续学习咯 -->
> #### info::Page loading bar is stuck？
>
> If the progress bar is stuck for more than 3 seconds when jumping to a new page, it's probably because we pushed a new version of the page.<br>
> Given that we're still updating and revising the documentation frequently, it may be easier to experience stuck jumps in the near future.<br>
> In this case, just __`refresh`__ You can continue to learn!

<!-- ## 往期课程主页

* [第五期](../2205/index.md) -->
## Past Courses Home

* [5th Cohort](../2205/index.md)

<!-- ## 其他资源

* [提问模板](../2205/misc/ask.md) -->
## Other resources

* [Questioning template](../2205/misc/ask.md)

<!-- ## 活动记录

* 2023/08/25 - [开源芯片技术生态论坛（原“一生一芯”技术论坛）](../events/20230825-2nd-tech-forum.md)
* 2023/07/02 - [第六期“一生一芯”启动会](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=1497409)
* 2022/11/20 - [从软件工程视角看芯片开源与敏捷设计(包云岗)](https://www.bilibili.com/video/BV1Dd4y1474D/)
* 2022/08/28 - [第一届“一生一芯”技术论坛暨第五期启动会](../events/20220828-1st-tech-forum.md)
* 2022/03/12 - [软硬件协同能力在芯片设计中的应用(金越, 胡博涵, 高泽宇)](https://www.bilibili.com/video/BV1334y187zC/) -->
## Record of events

* 2023/08/25 - [Open Source Chip Technology Ecology Forum (formerly "Ysyx" Technology Forum)](../events/20230825-2nd-tech-forum.md)
* 2023/07/02 - [Sixth "Ysyx" Kick-Off Meeting](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=1497409)
* 2022/11/20 - [Chip Open Source and Agile Design from a Software Engineering Perspective(包云岗)](https://www.bilibili.com/video/BV1Dd4y1474D/)
* 2022/08/28 - [The First "Ysyx" Technical Forum and the Fifth Launching Meeting](../events/20220828-1st-tech-forum.md)
* 2022/03/12 - [Hardware-software collaboration capabilities in chip design(金越, 胡博涵, 高泽宇)](https://www.bilibili.com/video/BV1334y187zC/)
