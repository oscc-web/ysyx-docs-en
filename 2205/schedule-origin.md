# 学习规划概述

从这一期开始, "一生一芯"将会培养大家的综合能力.
大家完成学习之后, 将会对以下问题有一定的认识:
1. 处理器是如何设计的?
1. 程序是如何在计算机上运行的?
1. 如何对处理器的性能进行优化?
1. 如何使用/设计正确的工具高效地进行调试?
1. 如何自己编写测试用例进行单元测试?
1. RTL设计如何生成可流片的版图?

我们将会引导大家设计一款配备Cache, 支持RV64IM的RISC-V流水线处理器,
并在自己设计的处理器上运行自己编写的小型操作系统,
在小型操作系统上运行真实游戏仙剑奇侠传.
达成指标的处理器将可以接入到SoC, 并获得流片机会.

> #### hint::信息框说明
> 讲义中会出现一些信息框, 根据其颜色和左上角的图标可以得知信息的类别.
> 例如本信息框就是一些提示相关的内容. 其它类别主要还有
> > #### flag::实验进度相关的提示
>
<!-- -->
> > #### comment::扩展阅读
>
<!-- -->
> > #### question::选做思考题
>
<!-- -->
> > #### option::选做编程题
>
<!-- -->
> > #### todo::实验必做内容
>
<!-- -->
> > #### danger::实验进度相关的必读信息
>
<!-- -->
> > #### caution::重要性超越实验的原则与方法

## 学习安排

> #### hint::按照自己的时间安排来学习
> 由于各位同学的基础和时间安排都各不相同, 因此总体来说"一生一芯"的学习规划是弹性的,
> 大家有事可以随时请假, 请假时间不限, 但需要在进度记录表中说明来告知助教;
> 有空的时候可以继续投入学习.
>
> 我们这里给出的时间安排也仅供参考, 基础较好的同学可能完成较快,
> 而零基础的同学则可能需要投入更多时间进行学习.

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
		width: 0.8em;
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
		line-height: 3em;
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
			<th _>阶段</th>
			<th week>周</th>
			<th>任务</th>
			<th _>环境</th>
			<th _>工具</th>
			<th _>数电</th>
			<th _>微结构</th>
			<th _>软件</th>
		</tr>
	</thead>
	<tbody>
		<tr class="Prestudy">
			<td stage-title rowspan="5">预学习阶段</td>
			<td week></td>
			<td task>学会提问, 安装Linux</td>
			<td x></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Prestudy">
			<td week></td>
			<td task>Linux基本使用</td>
			<td x></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Prestudy">
			<td week></td>
			<td task>搭建verilator仿真环境</td>
			<td x></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td x></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Prestudy">
			<td week></td>
			<td task>数字电路基础实验</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td x></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Prestudy">
			<td week></td>
			<td task>复习C语言, 完成PA1</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td stage-title rowspan="8">基础阶段</td>
			<td week></td>
			<td task rowspan="2">简易调试器</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td week></td>
			<td task>支持RV64IM的NEMU</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td week></td>
			<td task>运行时环境和基础设施</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td week></td>
			<td task>一个简单的单周期处理器</td>
			<td x></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td x></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td week></td>
			<td task>支持RV64IM的单周期处理器</td>
			<td x></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td week></td>
			<td task rowspan="2">设备和输入输出 </td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-B">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td stage-title rowspan="13">进阶阶段</td>
			<td week></td>
			<td task>简单的异常处理机制</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task>用户程序与系统调用</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task rowspan="2">精彩纷呈的用户程序</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task rowspan="2">总线和外设</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task>SoC计算机系统</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td x></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task>性能计数器</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task rowspan="2">高速缓存</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task>乘除法功能单元</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<td task rowspan="2">流水线</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-A">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Achievement">
			<td colspan="8"><i class="fa fa-flag"></i> 达成流片指标</td>
		</tr>
		<tr class="Stage-S">
			<td stage-title rowspan="14">专家阶段</td>
			<td week></td>
			<td task>多道程序</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<td task rowspan="3">分页虚拟内存管理</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td _></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<td task>分时多任务</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<td task rowspan="2">运行xv6操作系统</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<td task rowspan="4">运行Linux</td>
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td week></td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td x></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td x></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td stage-title rowspan="3">自行规划</td>
			<td task>双发射</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td task>乱序执行</td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Stage-S">
			<td task>乱序发射</td>
			<!-- <td task></td> -->
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Other-Topic">
			<td stage-title rowspan="4">其它主题</td>
			<td stage-title rowspan="4">自行规划</td>
			<td task>分支预测</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Other-Topic">
			<td task>替换算法</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Other-Topic">
			<td task>预取算法</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
		<tr class="Other-Topic">
			<td task>其它</td>
			<td _></td><!-- 环境 -->
			<td _></td><!-- 工具 -->
			<td _></td><!-- 数电 -->
			<td x></td><!-- 微结构 -->
			<td _></td><!-- 软件 -->
		</tr>
	</tbody>
</table>
<!-- End of table -->
