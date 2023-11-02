
## NEMU ISA相关的API说明文档

为了提高性能, 这些API也可以通过宏定义实现,
但本文档还是以C变量或函数的方式列出, 以给出变量或函数的类型.

### 全局类型

```c
word_t;
```
表示与ISA字长等长的无符号类型, 在32位的ISA中为`uint32_t`, 在64位的ISA中为`uint64_t`.

---

```c
sword_t;
```
表示与ISA字长等长的有符号类型, 在32位的ISA中为`int32_t`, 在64位的ISA中为`int64_t`.

---

```c
char *FMT_WORD;
```
`word_t`类型对应的十六进制格式化说明符, 在32位的ISA中为`"0x%08x"`, 在64位的ISA中为`"0x%016lx"`.

### Monitor相关

```c
unsigned char isa_logo[];
```
用于在未实现指令的报错信息中提示开发者阅读相关的手册.

---

```c
word_t RESET_VECTOR;
```
表示PC的初始值.

---

```c
void init_isa();
```
在monitor初始化时调用, 进行至少如下ISA相关的初始化工作:
* 设置必要的寄存器初值, 如`PC`等
* 加载内置客户程序

### 寄存器相关

```c
struct {
  // ...
  word_t pc;
} CPU_state;
```
寄存器结构的类型定义, 其中必须包含一个名为`pc`, 类型为`word_t`的成员.

---

```c
CPU_state cpu;
```
寄存器结构的全局定义.

---

```c
void isa_reg_display();
```
用于打印寄存器当前的值.

---

```c
word_t isa_reg_str2val(const char *name, bool *success);
```
若存在名称为`name`的寄存器, 则返回其当前值, 并设置`success`为`true`;
否则设置`success`为`false`.

### 指令执行相关

```c
struct {
  // ...
} ISADecodeInfo;
```
用于存放ISA相关的译码信息, 会嵌入在译码信息结构体`Decode`的定义中.

---

```c
int isa_exec_once(Decode *s);
```
取出`s->pc`指向的指令并译码执行, 同时更新`s->snpc`.

### 虚拟内存相关

```c
int isa_mmu_check(vaddr_t vaddr, int len, int type);
```
检查当前系统状态下对内存区间为`[vaddr, vaddr + len)`, 类型为`type`的访问是否需要经过地址转换.
其中`type`可能为:
* `MEM_TYPE_IFETCH`: 取指令
* `MEM_TYPE_READ`: 读数据
* `MEM_TYPE_WRITE`: 写数据

函数返回值可能为:
* `MMU_DIRECT`: 该内存访问可以在物理内存上直接进行
* `MMU_TRANSLATE`: 该内存访问需要经过地址转换
* `MMU_FAIL`: 该内存访问失败, 需要抛出异常(如RISC架构不支持非对齐的内存访问)

---

```c
paddr_t isa_mmu_translate(vaddr_t vaddr, int len, int type);
```
对内存区间为`[vaddr, vaddr + len)`, 类型为`type`的内存访问进行地址转换.
函数返回值可能为:
* `pg_paddr` | `MEM_RET_OK`: 地址转换成功, 其中`pg_paddr`为物理页面的地址(而不是`vaddr`翻译后的物理地址)
* `MEM_RET_FAIL`: 地址转换失败, 原因包括权限检查失败等不可恢复的原因, 一般需要抛出异常
* `MEM_RET_CROSS_PAGE`: 地址转换失败, 原因为访存请求跨越了页面的边界

### 中断异常相关

```c
vaddr_t isa_raise_intr(word_t NO, vaddr_t epc);
```
抛出一个号码为`NO`的异常, 其中`epc`为触发异常的指令PC, 返回异常处理的出口地址.

---

```c
word_t isa_query_intr();
```
查询当前是否有未处理的中断, 若有则返回中断号码, 否则返回`INTR_EMPTY`.

### DiffTest相关

```c
bool isa_difftest_checkregs(CPU_state *ref_r, vaddr_t pc);
```
检查当前的寄存器状态是否与`ref_r`相同, 其中`pc`为`cpu.pc`的上一条动态指令的PC, 即`cpu.pc`的旧值.
如果状态相同, 则返回`true`, 否则返回`false`.

---

```c
void isa_difftest_attach();
```
将当前的所有状态同步到REF, 并在之后的执行中开启DiffTest.
