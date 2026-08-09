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

  # F5 内容修改记录

- 修正 PC 位宽错误：
  - `PC bit width is 4 bits`
  - → `PC bit width is 8 bits`

- 补充 v26.07 新增的 Decode 相关内容：
  - 增加“操作码译码（opcode decoding）”与“操作数译码（operand decoding）”的说明。
  - 补充内容：

  `Instruction decoding can be further divided into opcode decoding and operand decoding. Opcode decoding identifies the function of an instruction based on its opcode, while operand decoding extracts the corresponding operands from the instruction encoding.`

- 为了与新增的“操作码译码 / 操作数译码”内容衔接更加自然，对后续 `li` 指令译码段落进行了调整：
  - 修改为：

  `For opcode decoding, since only the li instruction needs to be implemented at this stage, we can assume that every fetched instruction is an li instruction. For operand decoding, we only need to extract the rd and imm fields from the li instruction. From a circuit perspective, these are simply bit-field extraction operations and are straightforward to implement.`

- 补充 Decode 部分对“译码目的”的说明：
  - 增加：

  `The purpose of decoding is to identify the function of an instruction from its encoding.`

  - 并重新调整 Decode 开头的说明，使其更准确地表达从指令编码识别指令功能的过程。

- 修正控制逻辑表格中的端口错误：
  - `raddr2 Selection`
  - → `raddr1 Selection`

- 修正控制逻辑表格中 `add` 指令对应的源寄存器字段：
  - `Instruction's rs2`
  - → `Instruction's rs1`

  此修改仅针对控制逻辑表格中的这一处，使其与 `raddr1` 的实际功能以及前文的数据通路说明保持一致。

  # F6 内容修改记录
  - 标题 Simple Basic Input/Output 表达重复
    - `F6 Simple Basic Input/Output`
    - → `F6 Simple Input/Output`
  其它基本没有很大问题
