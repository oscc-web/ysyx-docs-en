# F4 内容修改记录

- `Instructions and Their Codes`
  → `Instructions and Their Encoding`

- `a minimum of two opcodes can be used`
  → `a 2-bit opcode is sufficient to distinguish all three instructions`

- `A Simple C Language Exampl`
  → `A Simple C Language Example`

- `compilte`
  → `compilation`

- 在三处 C 代码示例中补充 `#include <stdio.h>`。

- 补充 v26.07 新增的 C 语言三个关键组成要素：
  - Variables
  - Statements
  - Input/output functions

- 补全数列求和程序执行轨迹中未翻译完整的注释。

- `dozens of instructions`
  → `more than a dozen instructions`

- 将旧版关于 elementary functions 的表述更新为与 v26.07 一致的“有限次有理运算和复合操作”：
  → `a finite number of rational operations and compositions of basic elementary functions`

- 补充 v26.07 新增的 GPU 加速相关内容。

- 补充原本为空的 RISC-V 相关文章链接。

- `general purpose registers (GPR)`
  → `general-purpose registers (GPRs)`

- `clock speed of modern processors`
  → `clock frequency of modern processors`

- `advanced programming languages`
  → `high-level programming languages`

- `processor status`
  → `processor state`

- `changes in status`
  → `changes in state`

- `Set of events.`
  → `Event set.`

- 寄存器相关段落整体修改为：

  Some intermediate results need to be saved for later use, so a processor needs components that can store data. These components are called registers. A processor usually contains multiple registers organized into a register set, which some textbooks also call a register file. Because these registers are used to hold general-purpose data, they are called general-purpose registers (GPRs). Other registers serve specialized purposes and therefore do not belong to the GPRs.

- 修正 `1+2+...+10` 示例中的病句，修改为：

  For example, consider calculating `1+2+...+10`. Since a single addition instruction can add only two data values, the result of `1+2` must first be stored in some register `r` in the GPRs. The processor can then compute `r+3`, and so on. Therefore, the operand field of an instruction needs to specify which GPRs provide the input data and which GPR receives the result. For the opcode, the processor only needs a convention that defines which operation each opcode represents.
