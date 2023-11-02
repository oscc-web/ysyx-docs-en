
# x86指令系统简介

i386手册有一章专门列出了所有指令的细节, 附录中的opcode map也很有用.
在这里, 我们先对x86指令系统作一些简单的梳理.
当你对x86指令系统有任何疑惑时, 请查阅i386手册, 关于指令系统的一切细节都在里面.

> #### danger::i386手册勘误
> 由于PDF版本的i386手册的印刷错误较多, 一定程度上影响理解,
> 我们在github上开放了一个[repo][i386 repo], 用于提供修复印刷错误的版本.
> 同时我们也为修复错误后的版本提供在线的[HTML版本][i386 html].
>
> 如果你在做实验的过程中也发现了新的错误, 欢迎帮助我们修复这些错误.

[i386 repo]: https://github.com/NJU-ProjectN/i386-manual
[i386 html]: https://nju-projectn.github.io/i386-manual/toc.htm

## 指令格式

x86指令的一般格式如下:
```
+-----------+-----------+-----------+--------+------+------+------+------------+-----------+
|instruction| address-  |  operand- |segment |opcode|ModR/M| SIB  |displacement| immediate |
|  prefix   |size prefix|size prefix|override|      |      |      |            |           |
|-----------+-----------+-----------+--------+------+------+------+------------+-----------|
|   0 OR 1  |  0 OR 1   |   0 OR 1  | 0 OR 1 |1 OR 2|0 OR 1|0 OR 1| 0,1,2 OR 4 |0,1,2 OR 4 |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
|                                     number of bytes                                      |
+------------------------------------------------------------------------------------------+
```
除了opcode(操作码)必定出现之外, 其余组成部分可能不出现,
而对于某些组成部分, 其长度并不是固定的.
但给定一条具体指令的二进制形式, 其组成部分的划分是有办法确定的,
不会产生歧义(即把一串比特串看成指令的时候, 不会出现两种不同的解释). 例如对于以下指令:
```
100017:	66 c7 84 99 00 e0 ff ff 01 00  	movw   $0x1,-0x2000(%ecx,%ebx,4)
```
其组成部分的划分如下:
```
+-----------+-----------+-----------+--------+------+------+------+------------+-----------+
|instruction| address-  |  operand- |segment |opcode|ModR/M| SIB  |displacement| immediate |
|  prefix   |size prefix|size prefix|override|      |      |      |            |           |
|-----------+-----------+-----------+--------+------+------+------+------------+-----------|
|                            66                 c7     84     99    00 e0 ff ff    01 00   |
+------------------------------------------------------------------------------------------+
```
凭什么`0x84`要被解释成`ModR/M`字节呢?
这是由`opcode`决定的, `opcode`决定了这是什么指令的什么形式, 同时也决定了`opcode`之后的比特串如何解释.
如果你要问是谁来决定`opcode`, 那你就得去问Intel了.

PA中的x86经过简化, `address-size prefix`和`segment override prefix`都不会用到,
因此NEMU也不需要实现这两者的功能.

> #### question::编码的艺术
> 对于以下5个集合:
> 1. 所有`instruction prefix`
> 1. 所有`address-size prefix`
> 1. 所有`operand-size prefix`
> 1. 所有`segment override prefix`
> 1. 所有`opcode`的第一个字节
>
> 它们是两两不相交的. 这是必须的吗? 这背后反映了怎样的隐情?

另外我们在这里先给出`ModR/M`字节和`SIB`字节的格式,
它们是用来确定指令的操作数的, 详细的功能会在将来进行描述:
```
ModR/M byte
7    6    5    4    3    2    1    0
+--------+-------------+-------------+
|  mod   | reg/opcode  |     r/m     |
+--------+-------------+-------------+


SIB (scale index base) byte
7    6    5    4    3    2    1    0
+--------+-------------+-------------+
|   ss   |    index    |    base     |
+--------+-------------+-------------+
```

事实上, 一个字节最多只能区分256种不同的指令形式.
当指令形式的数目大于256时, 我们需要使用另外的方法来识别它们.
x86中有主要有两种方法来解决这个问题:
* 一种方法是使用转义码(escape code).
x86中有一个2字节转义码`0x0f`, 当指令`opcode`的第一个字节是`0x0f`时,
表示需要再读入一个字节才能决定具体的指令形式(部分条件跳转指令就属于这种情况).
后来随着各种SSE指令集的加入, 使用2字节转义码也不足以表示所有的指令形式了,
x86在2字节转义码的基础上又引入了3字节转义码,
当指令`opcode`的前两个字节是`0x0f`和`0x38`时,表示需要再读入一个字节才能决定具体的指令形式.
* 另一种方法是使用`ModR/M`字节中的扩展opcode域来对`opcode`的长度进行扩充.
有些时候, 读入一个字节也还不能完全确定具体的指令形式,
这时候需要读入紧跟在`opcode`后面的`ModR/M`字节,
把其中的`reg/opcode`域当做`opcode`的一部分来解释, 才能决定具体的指令形式.
x86把这些指令划分成不同的指令组(instruction group),
在同一个指令组中的指令需要通过`ModR/M`字节中的扩展opcode域来区分.

## 指令集细节

要实现一条指令, 首先你需要知道这条指令的格式和功能, 格式决定如何解释, 功能决定如何执行.
而这些信息都在instruction set page中, 因此你务必知道如何阅读它们.
我们以`mov`指令的opcode表为例来说明如何阅读:
```
     Opcode       Instruction       Clocks        Description
                  
< 1> 88 /r        MOV r/m8,r8       2/2           Move byte register to r/m byte
< 2> 89 /r        MOV r/m16,r16     2/2           Move word register to r/m word
< 3> 89 /r        MOV r/m32,r32     2/2           Move dword register to r/m dword
< 4> 8A /r        MOV r8,r/m8       2/4           Move r/m byte to byte register
< 5> 8B /r        MOV r16,r/m16     2/4           Move r/m word to word register
< 6> 8B /r        MOV r32,r/m32     2/4           Move r/m dword to dword register
< 7> 8C /r        MOV r/m16,Sreg    2/2           Move segment register to r/m word
< 8> 8D /r        MOV Sreg,r/m16    2/5,pm=18/19  Move r/m word to segment register
< 9> A0           MOV AL,moffs8     4             Move byte at (seg:offset) to AL
<10> A1           MOV AX,moffs16    4             Move word at (seg:offset) to AX
<11> A1           MOV EAX,moffs32   4             Move dword at (seg:offset) to EAX
<12> A2           MOV moffs8,AL     2             Move AL to (seg:offset)
<13> A3           MOV moffs16,AX    2             Move AX to (seg:offset)
<14> A3           MOV moffs32,EAX   2             Move EAX to (seg:offset)
<15> B0 + rb ib   MOV r8,imm8       2             Move immediate byte to register
<16> B8 + rw iw   MOV r16,imm16     2             Move immediate word to register
<17> B8 + rd id   MOV r32,imm32     2             Move immediate dword to register
<18> C6 /0 ib (*) MOV r/m8,imm8     2/2           Move immediate byte to r/m byte
<19> C7 /0 iw (*) MOV r/m16,imm16   2/2           Move immediate word to r/m word
<20> C7 /0 id (*) MOV r/m32,imm32   2/2           Move immediate dword to r/m dword

---------------------------------------------------------------------------
NOTES:
moffs8, moffs16, and moffs32 all consist of a simple offset relative
to the segment base. The 8, 16, and 32 refer to the size of the data. The
address-size attribute of the instruction determines the size of the
offset, either 16 or 32 bits.
---------------------------------------------------------------------------

注:
标记了(*)的指令形式的Opcode相对于i386手册有改动, 具体情况见下文的描述.
```
上表中的每一行给出了`mov`指令的不同形式, 每一列分别表示这种形式的opcode,
汇编语言格式, 执行所需周期, 以及功能描述.
由于NEMU关注的是功能的模拟, 因此`Clocks`一列不必关心.
 <font color=red>另外需要注意的是, i386手册中的汇编语言格式都是Intel格式,
 而objdump的默认格式是AT&T格式, 两者的源操作数和目的操作数位置不一样,
 千万不要把它们混淆了! 否则你将会陷入难以理解的bug中.</font>

首先我们来看`mov`指令的第一种形式:
```
     Opcode       Instruction       Clocks        Description
< 1> 88 /r        MOV r/m8,r8       2/2           Move byte register to r/m byte
```
* 从功能描述可以看出, 它的作用是"将一个8位寄存器中的数据传送到8位的寄存器或者内存中",
其中`r/m`表示"寄存器或内存".
* Opcode一列中的编码都是用十六进制表示, `88`表示这条指令的opcode的首字节是`0x88`,
`/r`表示后面跟一个`ModR/M`字节, 并且`ModR/M`字节中的`reg/opcode`域解释成通用寄存器的编码,
用来表示其中一个操作数.
* 通用寄存器的编码如下:

| 二进制编码 | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8位寄存器 | AL | CL | DL | BL | AH | CH | DH | BH |
| 16位寄存器 | AX | CX | DX | BX | SP | BP | SI | DI |
| 32位寄存器 | EAX | ECX | EDX | EBX | ESP | EBP | ESI | EDI |

* Instruction一列中, `r/m8`表示操作数是8位的寄存器或内存,
`r8`表示操作数是8位寄存器, 按照Intel格式的汇编语法来解释,
表示将8位寄存器(`r8`)中的数据传送到8位寄存器或内存(`r/m8`)中, 这和功能描述是一致的.
至于`r/m`表示的究竟是寄存器还是内存, 这是由`ModR/M`字节的`mod`域决定的:
当`mod`域取值为`3`的时候, `r/m`表示的是寄存器;
否则`r/m`表示的是内存. 表示内存的时候又有多种寻址方式, 具体信息参考i386手册中的表格17-3.

看明白了上面的第一种形式之后, 接下来的两种形式也就不难看懂了:
```
< 2> 89 /r        MOV r/m16,r16     2/2           Move word register to r/m word
< 3> 89 /r        MOV r/m32,r32     2/2           Move dword register to r/m dword
```
但你会发现, 这两种形式的`Opcode`都是一样的, 难道不会出现歧义吗?
不用着急, 还记得指令一般格式中的`operand-size prefix`吗? x86正是通过它来区分上面这两种形式的.
`operand-size prefix`的编码是`0x66`, 作用是指示当前指令需要改变操作数的宽度.
在i386中, 通常来说, 如果这个前缀没有出现, 操作数宽度默认是32位;
当这个前缀出现的时候, 操作数宽度就要改变成16位
(也有相反的情况, 这个前缀的出现使得操作数宽度从16位变成32位, 但这种情况在i386中极少出现).
换句话说, 如果把一个开头为`89 ...`的比特串解释成指令, 它就应该被解释成`MOV r/m32,r32`的形式;
如果比特串的开头是`66 89...`, 它就应该被解释成`MOV r/m16,r16`.

> #### comment::操作数宽度前缀的由来
> i386是从[8086][8086]发展过来的.
> 8086是一个16位的时代, 很多指令的16位版本在当时就已经实现好了.
> 要踏进32位的新时代, 兼容就成了需要仔细考量的一个重要因素.
>
> 一种最直接的方法是让32位的指令使用新的操作码, 但这样1字节的操作码很快就会用光.
> 假设8086已经实现了200条16位版本的指令形式, 为了加入这些指令形式的32位版本,
> 这种做法需要使用另外200个新的操作码, 使得大部分指令形式的操作码需要使用两个字节来表示,
> 这样直接导致了32位的程序代码会变长.
> 现在你可能会觉得每条指令的长度增加一个字节也没什么大不了,
> 但在i386诞生的那个遥远的时代(你可以在i386手册的封面看到那个时代),
> 内存是一种十分珍贵的资源, 因此这种使用新操作码的方法并不是一种明智的选择.
>
> Intel想到的解决办法就是引入操作数宽度前缀, 来达到操作码复用的效果.
> 当处理器工作在16位模式([实模式][real mode])下的时候, 默认执行16位版本的指令;
> 当处理器工作在32位模式([保护模式][protected mode])下的时候, 默认执行32位版本的指令.
> 当某些需要的时候, 才通过操作数宽度前缀来指示操作数的宽度.
> 这种方法最大的好处就是不需要引入额外的操作码, 从而也不会明显地使得程序代码变长.
> 虽然在NEMU里面可以使用很简单的方法来模拟这个功能,
> 但在真实的芯片设计过程中, CPU的译码部件需要增加很多逻辑才能实现.

[8086]: http://en.wikipedia.org/wiki/Intel_8086
[real mode]: http://en.wikipedia.org/wiki/Real_mode
[protected mode]: http://en.wikipedia.org/wiki/Protected_mode

到现在为止, <4>-<6>三种形式你也明白了:
```
< 4> 8A /r        MOV r8,r/m8       2/4           Move r/m byte to byte register
< 5> 8B /r        MOV r16,r/m16     2/4           Move r/m word to word register
< 6> 8B /r        MOV r32,r/m32     2/4           Move r/m dword to dword register
```

`<7>` 和 `<8>` 两种形式的mov指令涉及到段寄存器:
```
< 7> 8C /r        MOV r/m16,Sreg    2/2           Move segment register to r/m word
< 8> 8D /r        MOV Sreg,r/m16    2/5,pm=18/19  Move r/m word to segment register
```
PA中的x86去掉了段寄存器的实现, 我们可以忽略这两种形式的`mov`指令.

`<9>` - `<14>` 这6种形式涉及到一种新的操作数记号`moffs`:
```
< 9> A0           MOV AL,moffs8     4             Move byte at (seg:offset) to AL
<10> A1           MOV AX,moffs16    4             Move word at (seg:offset) to AX
<11> A1           MOV EAX,moffs32   4             Move dword at (seg:offset) to EAX
<12> A2           MOV moffs8,AL     2             Move AL to (seg:offset)
<13> A3           MOV moffs16,AX    2             Move AX to (seg:offset)
<14> A3           MOV moffs32,EAX   2             Move EAX to (seg:offset)
---------------------------------------------------------------------------
NOTES:
moffs8, moffs16, and moffs32 all consist of a simple offset relative
to the segment base. The 8, 16, and 32 refer to the size of the data. The
address-size attribute of the instruction determines the size of the
offset, either 16 or 32 bits.
---------------------------------------------------------------------------
```
NOTES中给出了`moffs`的含义, 它用来表示段内偏移量,
但PA中的x86没有"段"的概念, 目前可以理解成"相对于物理地址0处的偏移量".
这6种形式是`mov`指令的特殊形式, 它们可以不通过`ModR/M`字节,
让`displacement`直接跟在`opcode`后面, 同时让`displacement`来指示一个内存地址.

`<15>` - `<17>` 三种形式涉及到两种新的操作数记号:
```
<15> B0 + rb ib   MOV r8,imm8       2             Move immediate byte to register
<16> B8 + rw iw   MOV r16,imm16     2             Move immediate word to register
<17> B8 + rd id   MOV r32,imm32     2             Move immediate dword to register
```
其中:
* `+rb`, `+rw`, `+rd`分别表示8位, 16位, 32位通用寄存器的编码.
和`ModR/M`中的`reg`域不一样的是, 这三种记号表示直接将通用寄存器的编号按数值加到`opcode`中
(也可以看成通用寄存器的编码嵌在`opcode`的低三位),
因此识别指令的时候可以通过`opcode`的低三位确定一个寄存器操作数.
* `ib`, `iw`, `id`分别表示8位, 16位, 32位立即数

最后3种形式涉及到一种新的操作码记号`/digit`, 其中`digit`为`0`~`7`中的一个数字:
```
<18> C6 /0 ib (*) MOV r/m8,imm8     2/2           Move immediate byte to r/m byte
<19> C7 /0 iw (*) MOV r/m16,imm16   2/2           Move immediate word to r/m word
<20> C7 /0 id (*) MOV r/m32,imm32   2/2           Move immediate dword to r/m dword

注:
标记了(*)的指令形式的Opcode相对于i386手册有改动, 具体情况见下文的描述.
```
上述形式中的`/0`表示一个`ModR/M`字节,
并且`ModR/M`字节中的`reg/opcode`域解释成扩展opcode, 其值取`0`.
对于含有`/digit`记号的指令形式, 需要通过指令本身的`opcode`和`ModR/M`中的扩展opcode共同决定指令的形式,
例如`80 /0`表示`add`指令的一种形式, 而`80 /5`则表示`sub`指令的一种形式,
只看`opcode`的首字节`80`不能区分它们.

注: 在i386手册中, 这3种形式的`mov`指令并没有`/0`的记号,
在这里加入`/0`纯粹是为了说明`/digit`记号的意思.
但同时这条指令在i386中也比较特殊, 它需要使用`ModR/M`字节来表示一个寄存器或内存的操作数,
但`ModR/M`字节中的`reg/opcode`域却没有用到
(一般情况下, `ModR/M`字节中的`reg/opcode`域要么表示一个寄存器操作数, 要么作为扩展opcode),
i386手册也没有对此进行特别的说明, 直觉上的解释就是"无论`ModR/M`字节中的`reg/opcode`域是什么值,
都可以被CPU识别成这种形式的`mov`指令".
x86是商业CPU, 我们无法从电路级实现来考证这一解释,
但对编译器生成代码来说, 这条指令中的`reg/opcode`域总得有个确定的值,
因此编译器一般会把这个值设成`0`.
在NEMU的框架代码中, 对这3种形式的`mov`指令的实现和i386手册中给出`Opcode`保持一致,
忽略`ModR/M`字节中的`reg/opcode`域, 没有判断其值是否为`0`.
如果你不能理解这段话在说什么, 你可以忽略它, 因为这并不会影响实验的进行.

到此为止, 你已经学会了如何阅读大部分的指令集细节了.
需要说明的是, 这里举的`mov`指令的例子并没有完全覆盖i386手册中指令集细节的所有记号, 若有疑问, 请参考i386手册.

除了opcode表之外, `Operation`, `Description`和`Flags Affected`这三个条目都要仔细阅读,
这样你才能完整地掌握一条指令的功能.
`Exceptions`条目涉及到执行这条指令可能产生的异常,
由于PA中的x86不打算加入异常处理的机制, 你可以不用关心这一条目.
