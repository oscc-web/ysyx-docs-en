---
sidebarDepth: 3
sidebar: auto
pageClass: "ysyx-index"
---

# "一生一芯" v24.07 课程主页

* 直播教学计划从2025年9月开始, 请保持关注
* 如果你发现了实验讲义和材料的错误或者对实验内容有疑问或建议,
  可通过邮件联系余子濠(yuzihao#ict.ac.cn)

## 教学资源

* `时间`一栏是以小时为单位的预估完成时间
  * 预估完成时间为`2`的内容, 一般没有相关的编程任务,
    只有2小时的视频录播, 用于补充讲解相关知识
  * 鉴于同学们的基础水平有高有低, 此处按照"中等水平"同学的能力来预估.
    但这里的"中等水平"并不是指"程序设计课程总评80分以上",
    而是指"学习心态端正, 编写过500行以上代码的单个程序, 并且懂得调试".
  * 如果你是零基础的初学者, 你应该预期花费这个数字`2~3`倍的时间来完成学习.
    不过你不必为此感到沮丧, 所谓"闻道有先后", 之所以其他同学学得快,
    很大一部分原因是因为他们之前已经付出努力迈过了初学者的阶段.
* 可点击图标跳转到相应资源
* 完整的讲义可通过页面右上方导航栏查看
* 课件用[reveal.js][reveal.js]编写, 可导出为PDF文件, 具体见[这里的操作][reveal.js export pdf]
* S阶段讲义内容仍然在🕊

[reveal.js]: https://revealjs.com
[reveal.js export pdf]: https://revealjs.com/pdf-export/

`C` = C语言(程序/模拟器/系统软件) | `R` = RISC-V指令集 | `P` = 处理器设计 | `T` = 工具

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
			<th _>阶段</th> <th week>序号</th>
			<th>任务</th> <th>时间</th> <th>讲义</th> <th>课件</th> <th>视频</th>
			<th _>C</th> <th _>R</th> <th _>P</th> <th _>T</th>
		</tr>
	</thead>
	<tbody>
		<tr class="Stage-F">
			<td stage-title rowspan="6">F阶段</td>
			<td week></td> <td task>如何科学地提问</td> <td>2</td>
            <td _><a href="2407/f/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/01.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV14F411975K" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td week></td> <td task>Logisim安装和使用</td> <td>2</td>
            <td _><a href="2407/f/2.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-F">
			<td week></td> <td task>数字逻辑电路基础</td> <td>20</td>
            <td _><a href="2407/f/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/06.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ZH4y1Q7Cv" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td week></td> <td task>计算机系统的状态机模型</td> <td>5</td>
            <td _><a href="2407/f/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/03.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1oN411Y7FK" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td week></td> <td task>支持数列求和的简单处理器</td> <td>5</td>
            <td _><a href="2407/f/5.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-F">
			<td week></td> <td task>功能完备的迷你RISC-V处理器</td> <td>5</td>
            <td _><a href="2407/f/6.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td stage-title rowspan="6">E阶段</td>
			<td week></td> <td task>C语言程序设计</td> <td>20</td>
            <td _><a href="2407/e/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/04.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV13z4y147mB" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td week></td> <td task>硬件描述语言</td> <td>20</td>
            <td _><a href="2407/e/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/06.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ZH4y1Q7Cv" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td week></td> <td task>Linux系统安装和基本使用</td> <td>10</td>
            <td _><a href="2407/e/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2407/2.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1vF4119726" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-E">
			<td week></td> <td task>从C代码到二进制程序</td> <td>10</td>
            <td _><a href="2407/e/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/05.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Rm4y1p7Cg" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td week></td> <td task>从RTL代码到可流片版图</td> <td>20</td>
            <td _><a href="2407/e/5.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td x></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-E">
			<td week></td> <td task>完成PA1</td> <td>20</td>
            <td _><a href="2407/e/6.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/07.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1up4y1j7Ji" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><a href="2407/e/7.html" target="_blank"><i class="fa fa-flag"></i> 申请入学答辩</a></td>
		</tr>
		<tr class="Stage-D">
			<td stage-title rowspan="6">D阶段</td>
			<td week></td> <td task>支持RV32IM的NEMU</td> <td>10</td>
            <td _><a href="2407/d/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/08.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV15h4y1A7Up" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td week></td> <td task>程序的机器级表示(上)</td> <td>2</td>
            <td _><a href="2407/d/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/09.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ow411275B" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td week></td> <td task>程序的机器级表示(下)</td> <td>2</td>
            <td _><a href="2407/d/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/10.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV19H4y1d7Yi" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td week></td> <td task>AM运行时环境</td> <td>5</td>
            <td _><a href="2407/d/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/11.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Vu4y1s73Y" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td week></td> <td task>用RTL实现迷你RISC-V处理器</td> <td>5</td>
            <td _><a href="2407/d/4.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-D">
			<td week></td> <td task>设备和输入输出</td> <td>10</td>
            <td _><a href="2407/d/5.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/15.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1sb4y1g7Xu" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-C">
			<td stage-title rowspan="5">C阶段</td>
			<td week></td> <td task>工具和基础设施</td> <td>5</td>
            <td _><a href="2407/c/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/12.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1RM411Q7Au" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-C">
			<td week></td> <td task>支持RV32E的单周期NPC</td> <td>5</td>
            <td _><a href="2407/c/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/13.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1rc411f7mK" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td x></td>
		</tr>
		<tr class="Stage-C">
			<td week></td> <td task>调试技巧</td> <td>2</td>
            <td _><a href="2407/c/3.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/16.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Vz4y1A7Rt" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td _></td> <td x></td>
		</tr>
		<tr class="Stage-C">
			<td week></td> <td task>ELF文件和链接</td> <td>2</td>
            <td _><a href="2407/c/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/14.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1Ly4y1w7hn" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-C">
			<td week></td> <td task>异常处理和RT-Thread</td> <td>15</td>
            <td _><a href="2407/c/5.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/17.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1734y1w7ro" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><i class="fa fa-flag"></i> C阶段结业准备与考核</td>
		</tr>
		<tr class="Stage-B">
			<td stage-title rowspan="6">B阶段</td>
			<td week></td> <td task>总线</td> <td>10</td>
            <td _><a href="2407/b/1.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/18.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1gj411s7ah" target="_blank">🎬</a></td>
			<td _></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>SoC计算机系统(上)</td> <td>15</td>
            <td _><a href="2407/b/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/19.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1NC4y1u7K3" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>SoC计算机系统(下)</td> <td>15</td>
            <td _><a href="2407/b/2.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/20.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1FC4y1k7mP" target="_blank">🎬</a></td>
			<td x></td> <td x></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>时序分析和优化</td> <td>5</td>
            <td _><a href="2407/b/3.html" target="_blank">📚</a></td>
            <td _> - </td>
            <td _> - </td>
			<td _></td> <td _></td> <td x></td> <td _></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>性能优化和简易缓存</td> <td>20</td>
            <td _><a href="2407/b/4.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/21.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1xr421F7ZP" target="_blank">🎬</a></td>
			<td x></td> <td _></td> <td x></td> <td x></td>
		</tr>
		<tr class="Stage-B">
			<td week></td> <td task>流水线处理器</td> <td>20</td>
            <td _><a href="2407/b/5.html" target="_blank">📚</a></td>
            <td _><a href="https://ysyx.oscc.cc/slides/2306/22.html#/" target="_blank">📰</a></td>
            <td _><a href="https://www.bilibili.com/video/BV1ZRtkeVEqw" target="_blank">🎬</a></td>
			<td _></td> <td _></td> <td x></td> <td x></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><a href="2306/basic/1.11.html" target="_blank"><i class="fa fa-flag"></i> B阶段流片准备与考核 📚</a></td>
		</tr>
		<tr class="Stage-A">
			<td stage-title rowspan="7">A阶段</td>
			<td week></td> <td task>乘除法器</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>系统调用和应用程序</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>虚存管理</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>特权级和xv6</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>启动Linux和Debian</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>缓存进阶</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Stage-A">
			<td week></td> <td task>分支预测进阶</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
		<tr class="Achievement">
			<td colspan="11"><i class="fa fa-flag"></i> A阶段流片准备与考核</td>
		</tr>
		<tr class="Stage-S">
			<td stage-title rowspan="1">S阶段</td>
			<td week></td> <td task>待续</td> <td>0</td>
            <td _> </td> <td _> </td> <td _> </td>
            <!-- 环境       工具       数电        微结构       软件 -->
			<td _></td> <td _></td> <td _></td> <td _></td>
		</tr>
	</tbody>
</table>
<!-- End of table -->

> #### info::页面加载条卡住了？
>
> 跳转页面时, 如果进度条卡住 3 秒以上, 很可能是由于我们推送了网页版本更新.<br>
> 鉴于我们还在频繁更新、修订文档, 近期可能会比较容易遇到跳转卡住的情况.<br>
> 遇到这种情况, 只需要 __`刷新整个页面`__ 即可继续学习咯

## 往期课程主页

可通过顶部导航栏的"课程主页"查看.

## 其他资源

* [《RISC-V开放架构设计之道》 大卫·帕特森 安德鲁·沃特曼 著，勾凌睿 陈璐 刘志刚 译](https://item.jd.com/10092349081102.html)
* [《计算机系统——基于RISC-V+Linux平台》 袁春风 余子濠 陈璐  编著](https://product.dangdang.com/29720521.html)
* [Digital Design and Computer Architecture - Spring 2023, Onur Mutlu@ETH Zurich](https://safari.ethz.ch/digitaltechnik/spring2023/doku.php?id=schedule)
* [提问模板](../2205/misc/ask.md)

## 活动记录

* 2024/07/14 - [“一生一芯”2024暑期宣讲会](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=3416378)
* 2023/08/25 - [开源芯片技术生态论坛（原“一生一芯”技术论坛）](../events/20230825-2nd-tech-forum.md)
* 2023/07/02 - [第六期“一生一芯”启动会](https://space.bilibili.com/2107852263/channel/collectiondetail?sid=1497409)
* 2022/11/20 - [从软件工程视角看芯片开源与敏捷设计(包云岗)](https://www.bilibili.com/video/BV1Dd4y1474D/)
* 2022/08/28 - [第一届“一生一芯”技术论坛暨第五期启动会](../events/20220828-1st-tech-forum.md)
* 2022/03/12 - [软硬件协同能力在芯片设计中的应用(金越, 胡博涵, 高泽宇)](https://www.bilibili.com/video/BV1334y187zC/)
