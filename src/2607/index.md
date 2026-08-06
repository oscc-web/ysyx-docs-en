---
sidebarDepth: 3
sidebar: auto
pageClass: "ysyx-index"
---

# “One Student One Chip” v26.07 Course Homepage

* Time: Wait to be determined
* If you find errors in the lab handouts or materials, or have questions or suggestions about the experiments, please contact Yu Zihao via email (yuzihao#ict.ac.cn).
    * Given that an increasing number of students are submitting incorrect AI-generated answers as modification suggestions, if no email response is received within one week, the suggestion will be considered not adopted by default.

## Learning Resources

* The `Time` column indicates estimated completion time in hours.
  * Content marked with an estimated completion time of `2` typically does not include programming assignments,
    but consists of 2 hours of video lectures designed to supplement related knowledge.
  * Given varying student proficiency levels, these estimates are based on “intermediate-level” learners.
    This “intermediate level” does not mean “scoring above 80% in programming courses,”
    but rather “having a positive learning attitude, having written a single program exceeding 500 lines of code, and understanding debugging.”
  * If you are a complete beginner, expect to spend 2–3 times this amount of time to complete the study.
    Don't be discouraged—as the saying goes, “Some learn earlier, some later.” The reason other students progress faster is largely because they've already invested effort to overcome the beginner stage.
* Click icons to jump to corresponding resources
* Full lecture notes accessible via the top-right navigation bar
* Course materials created with [reveal.js][reveal.js], exportable to PDF—see [this guide][reveal.js export pdf]
* S-stage lecture content remains under development 🕊

[reveal.js]: https://revealjs.com
[reveal.js export pdf]: https://revealjs.com/pdf-export/

`C` = C language ( programs / emulators / system software ) | `R` = RISC-V instruction set | `P` = Processor design | `T` = Tools

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
	.Stage-F { --hue: 000; }
	.Stage-E { --hue: 050; }
	.Stage-D { --hue: 100; }
	.Stage-C { --hue: 150; }
	.Stage-B { --hue: 200; }
	.Stage-A { --hue: 250; }
	.Stage-S { --hue: 300; }
	.Other-Topic { --saturation: 0%; }
</style>
<table id="schedule-table">
	<thead>
		<tr>
			<th _>Stage</th> <th>Number</th>
			<th>Task</th> <th>Time</th> <th>Course Handout</th> <th>Slide</th> <th>Video</th>
			<th _>C</th> <th _>R</th> <th _>P</th> <th _>T</th>
		</tr>
	</thead>
	<tbody>
		<tr class="Stage-F">
			<td stage-title rowspan="6">F stage</td>
			<td>F1</td> <td task>How to Ask Smart Questions</td> <td>2</td>
            <td _><a href="2607/f/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2607/01.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1WvHazNEsk/" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td>F2</td> <td task>Installing and Using Logisim</td> <td>2</td>
            <td _><a href="2607/f/2.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-F">
			<td>F3</td> <td task>Fundamentals of Digital Logic Circuits</td> <td>20</td>
            <td _><a href="2607/f/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2607/02.html#/" target="_blank">📰(上)</a>
                  <a href="https://ysyx.oscc.cc/slides/2607/03.html#/" target="_blank">📰(下)</a></td>
            <td _><a href="https://www.bilibili.com/video/BV19nWNz2EZC" target="_blank">🎬(上)</a>
                  <a href="https://www.bilibili.com/video/BV1xentzxED7" target="_blank">🎬(下)</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td>F4</td> <td task>State Machine Model of Computer Systems</td> <td>5</td>
            <td _><a href="2607/f/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2607/04.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV17Lx6zREH6" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td>F5</td> <td task>Simple Processor Supporting Sequence Summation</td> <td>5</td>
            <td _><a href="2607/f/5.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2607/05.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1YgxCzdEvq" target="_blank">🎬</a></td>
			<td _></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td>F6</td> <td task>Simple Basic Input/Output</td> <td>5</td>
            <td _><a href="2607/f/6.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><a href="2607/f/7.html" target="_blank"><i class="fa fa-flag"></i>F Stage Tapeout Preparation</a></td>
		</tr>
		<tr class="Stage-E">
			<td stage-title rowspan="8">E Stage</td>
			<td>E1</td> <td task>Hardware Description Language</td> <td>20</td>
            <td _><a href="2607/e/1.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td>E2</td> <td task>C language programming</td> <td>20</td>
            <td _><a href="2607/e/2.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td x></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td>E3</td> <td task>Linux System Installation and Basic Usage</td> <td>10</td>
            <td _><a href="2607/e/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2607/06.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1wD4xzbEpU" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-E">
			<td>E4</td> <td task>Processor Simulation and Verification</td> <td>5</td>
            <td _><a href="2607/e/4.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td x></td> <td x></td> <td x></td> <td x></td>
		</tr>
		<tr class="Stage-E">
			<td>E5</td> <td task>A Fully Functional mini RISC-V Processor</td> <td>5</td>
            <td _><a href="2607/e/5.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td>E6</td> <td task>A Simple Runtime Environment</td> <td>5</td>
            <td _><a href="2607/e/6.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td x></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td>E7</td> <td task>Simple Bus and SoC</td> <td>5</td>
            <td _><a href="2607/e/7.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td>E8</td> <td task>综合与后端物理设计(流片准备)</td> <td>5</td>
            <td _><a href="2607/e/8.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><a href="2607/e/9.html" target="_blank"><i class="fa fa-flag"></i> Submission of pre-study defense application</a></td>
		</tr>
		<tr class="Stage-D">
			<td stage-title rowspan="12">D阶段</td>
			<td rowspan="2">D1</td> <td task>从C代码到二进制程序</td> <td rowspan="2">10</td>
            <td _ rowspan="2"><a href="2607/d/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/07.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1TtWYz2Eun" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td task>C程序的执行</td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/08.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV189svz8ET5" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td>D2</td> <td task>简易调试器</td> <td>20</td>
            <td _><a href="2607/d/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/15.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1bc2YB9Ehi" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-D">
			<td>D3</td> <td task>RISC-V指令集</td> <td>5</td>
            <td _><a href="2607/d/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/16.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1RVmMBaEC6" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td>D4</td> <td task>AM运行时环境</td> <td>5</td>
            <td _><a href="2607/d/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/11.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Vu4y1s73Y" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td rowspan="5">D5</td> <td task>RTL代码的仿真</td> <td rowspan="5">20</td>
            <td _ rowspan="5"><a href="2607/d/5.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/10.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ho1ZBbETt" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td task>逻辑综合</td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/11.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1SyyFBtE7R" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td task>Verilog的RTL综合语义</td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/12.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1PjyFBmE3Z" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td task>标准单元库</td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/13.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1XAU6BpECX" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td task>物理设计</td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/14.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV15ZUzBoEf6" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td>D6</td> <td task>工具和基础设施</td> <td>5</td>
            <td _><a href="2607/d/6.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/12.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1RM411Q7Au" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-D">
			<td>D7</td> <td task>支持RV32E的单周期NPC</td> <td>5</td>
            <td _><a href="2607/d/7.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/13.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1rc411f7mK" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td x></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><a href="2607/d/8.html" target="_blank"><i class="fa fa-flag"></i> D阶段流片准备</a></td>
		</tr>
		<tr class="Stage-C">
			<td stage-title rowspan="6">C阶段</td>
			<td>C1</td> <td task>程序的机器级表示</td> <td>4</td>
            <td _><a href="2607/c/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/09.html#/" target="_blank">📰(上)</a>
                  <a href="https://ysyx.oscc.cc/slides/2306/10.html#/" target="_blank">📰(下)</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ow411275B" target="_blank">🎬(上)</a>
                  <a href="https://www.bilibili.com/video/BV19H4y1d7Yi" target="_blank">🎬(下)</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-C">
			<td>C2</td> <td task>ELF文件和链接</td> <td>2</td>
            <td _><a href="2607/c/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/14.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Ly4y1w7hn" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-C">
			<td>C3</td> <td task>设备和输入输出</td> <td>10</td>
            <td _><a href="2607/c/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/15.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1sb4y1g7Xu" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-C">
			<td>C4</td> <td task>调试技巧</td> <td>2</td>
            <td _><a href="2607/c/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/16.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Vz4y1A7Rt" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-C">
			<td>C5</td> <td task>总线</td> <td>10</td>
            <td _><a href="2607/c/5.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/18.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1gj411s7ah" target="_blank">🎬</a></td>
			<td _></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-C">
			<td>C6</td> <td task>SoC计算机系统</td> <td>30</td>
            <td _><a href="2607/c/6.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/19.html#/" target="_blank">📰(上)</a>
                  <a href="https://ysyx.oscc.cc/slides/2306/20.html#/" target="_blank">📰(下)</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1NC4y1u7K3" target="_blank">🎬(上)</a>
                  <a href="https://www.bilibili.com/video/BV1FC4y1k7mP" target="_blank">🎬(下)</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><a href="2607/c/7.html" target="_blank"><i class="fa fa-flag"></i> C阶段流片准备</a></td>
		</tr>
		<tr class="Stage-B">
			<td stage-title rowspan="4">B阶段</td>
			<td>B1</td> <td task>异常处理和RT-Thread</td> <td>15</td>
            <td _><a href="2607/b/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/17.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1734y1w7ro" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td>B2</td> <td task>时序分析和优化</td> <td>5</td>
            <td _><a href="2607/b/2.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td>B3</td> <td task>性能优化和简易缓存</td> <td>20</td>
            <td _><a href="2607/b/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/21.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1xr421F7ZP" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td x></td> <td x></td>
		</tr>
		<tr class="Stage-B">
			<td>B4</td> <td task>流水线处理器</td> <td>20</td>
            <td _><a href="2607/b/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/22.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ZRtkeVEqw" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td x></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><a href="2306/basic/1.11.html" target="_blank"><i class="fa fa-flag"></i> B阶段流片准备与考核</a></td>
		</tr>
		<tr class="Stage-A">
			<td stage-title rowspan="7">A阶段</td>
			<td></td> <td task>乘除法器</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td></td> <td task>系统调用和应用程序</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td></td> <td task>虚存管理</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td></td> <td task>特权级和xv6</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td></td> <td task>启动Linux和Debian</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td></td> <td task>缓存进阶</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td></td> <td task>分支预测进阶</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><i class="fa fa-flag"></i> A阶段流片准备与考核</td>
		</tr>
		<tr class="Stage-S">
			<td stage-title rowspan="1">S Stage</td>
			<td></td> <td task>待续</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
	</tbody>
</table>



> #### info::Page loading bar is stuck？
>
> If the progress bar is stuck for more than 3 seconds when jumping to a new page, it's probably because we pushed a new version of the page.<br>
> Given that we're still updating and revising the documentation frequently, it may be easier to experience stuck jumps in the near future.<br>
> In this case, just __`refresh`__ You can continue to learn!


## Other Resources

* The RISC-V Reader: An Open Architecture Atlas By David Patterson and Andrew Wathelet
* [Computer Systems: Based on the RISC-V + Linux Platform Edited by Yuan Chunfeng, Yu Zihao, and Chen Lu](https://product.dangdang.com/29720521.html)
* [Digital Design and Computer Architecture - Spring 2023, Onur Mutlu@ETH Zurich](https://safari.ethz.ch/digitaltechnik/spring2023/doku.php?id=schedule)
* [Questioning template](../2205/misc/ask.md)

## Record of events

* 2025/07/21 - [“One Student One Chip” 2025 Summer Workshop](https://space.bilibili.com/2107852263/lists/5997805?type=season) 
* 2024/07/14 - [“One Student One Chip” 2024 Summer Workshop](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=3416378)
* 2023/08/25 - [Open Source Chip Technology Ecology Forum (formerly "One Student One Chip" Technology Forum)](../en/events/20230825-2nd-tech-forum.md)
* 2023/07/02 - [6th "One Student One Chip" Kick-Off Meeting](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=1497409)
* 2022/11/20 - [Chip Open Source and Agile Design from a Software Engineering Perspective(Yungang Bao)](https://www.bilibili.com/video/BV1Dd4y1474D/)
* 2022/08/28 - [The First "One Student One Chip" Technical Forum and the Fifth Launching Meeting](../en/events/20220828-1st-tech-forum.md)
* 2022/03/12 - [Hardware-software collaboration capabilities in chip design(Yue Jin, Bohan Hu, Zeyu Gao)](https://www.bilibili.com/video/BV1334y187zC/)