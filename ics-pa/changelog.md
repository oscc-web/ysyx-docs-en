
## 更新日志

### ICS2023

#### nemu

* 修复译码非法指令时的UB
([补丁](https://github.com/NJU-ProjectN/nemu/commit/8417a259398089bb8b590b7785f768c075548d81))
* 修复C++报告的`invalid suffix on literal`警告
([补丁](https://github.com/NJU-ProjectN/nemu/commit/947dc940a9c9efcbdc798354eb71d85803bc4220))
* 重新添加mips32
([补丁](https://github.com/NJU-ProjectN/nemu/commit/76278e886803354b81d14522aa7eb71d7b810dee))
* 修复在llvm15上库函数路径变化导致的编译错误
([补丁](https://github.com/NJU-ProjectN/nemu/commit/ed2066c1f6e7e6bfb4f8203146c5f3d1d856e348))
* 修复在macOS上按键宏定义与系统库冲突的问题
([补丁](https://github.com/NJU-ProjectN/nemu/commit/48b4860cef80073dbac7b8d980c8d3b90f9bf152))
* 将difftest动态库的符号默认设置为`visibility=hidden`, 提升动态库内部符号引用的性能
([补丁](https://github.com/NJU-ProjectN/nemu/commit/3d5b0b9160cd37fc5d462567123bd43e48f6fac6))
* 更新spike版本, 修复macOS上因llvm版本较新导致的spike编译错误
([补丁](https://github.com/NJU-ProjectN/nemu/commit/fe77a6b3a032f4ccd68da0570832518dd6475a1a))
  * 使用c++17编译spike
  ([补丁](https://github.com/NJU-ProjectN/nemu/commit/5f66cb8067674512bb606e20530d8d764188fbb4))
* 修复`gen-expr`中`fscanf()`未检查返回值导致的编译报错
([补丁](https://github.com/NJU-ProjectN/nemu/commit/c3baa4a77de7525cef93e19c2353b90947e86e78))
* 通过llvm反汇编时关闭伪指令
([补丁](https://github.com/NJU-ProjectN/nemu/commit/9bf4ff83597d37646098ed707f591f07d933e6bd))
* 修复Gentoo Linux中kconfig链接报错的问题
([补丁](https://github.com/NJU-ProjectN/nemu/commit/6498a76b2742a680ac2d6fd68358b878c64b05f5))
* 合并riscv32和riscv64
([补丁](https://github.com/NJU-ProjectN/nemu/commit/4bfdb7e3a95752d2a901ac8ea726d80b3f1b58c6))
* 修复`nemu/src/device/keyboard.c`中宏可能与库的头文件中定义重名的问题
  * 宏展开后重名([补丁](https://github.com/NJU-ProjectN/nemu/commit/b5c841e21b2e87daedb64dd2710c0e8c38ee5aaf))
  * 宏展开过程中重名([补丁](https://github.com/NJU-ProjectN/nemu/commit/7cc6120266ba8163d4ae501017c1fcc195e556cd))
* 修复SDL在Wayland环境下窗口不弹出的问题
([补丁](https://github.com/NJU-ProjectN/nemu/commit/03daf8795774fd9ba65454fb009daa65f66bc29a))

#### abstract-machine

* 去除ld 2.39引入的关于可执行栈和可读可写可执行的可加载段的警告
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/024441cbed3e9889fe62503f34df5d6c3fa08170)和
 [补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/31a5a10f4858096751329b5a9b8a671ba819b1ea))
* 使用riscv64-linux-gnu-gcc 11将CSR指令独立成zicsr扩展, 修复相关编译错误
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/ad9504123fba7548ca41b1295664d1f9928b5052))
* 在mips32的`start.S`中为异常入口`0x80000180`预留若干位置, 用于设置异常入口处的执行
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/5051c13e02f657e87609c2bad17709155019c39c))
* 修复sdl2-2.0.22-1后窗口有概率不显示的问题
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/ba5ba9838edcdef5cc8d7b436124af655ada36d1))
* 支持将`LDFLAGS`传递给native的g++
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/e8943b31fc30adaba4fded6b8e9eb4f73477e491))
* 修复native的`platform.c`链接到RT-Thread中`ftruncate()`的问题
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/21bfbcb293567804c9617e5ceb374f94f4bc32ed))
* 修复macOS上默认调用llvm-ar的问题
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/6d79d0efb082c5346c99fab1f1d67cb996f169f7))
* 将`scripts/isa/`目录下RISC-V相关的`.mk`文件合并成`riscv.mk`
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/ad8f8fb636925666d2fb9a2216da868b82ba0e5b))
* 将`am/include/arch/`目录下RISC-V相关的`.h`文件合并成`riscv.h`
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/e0ae9b7651436f8dfcbe6383f73f67ebb04ce399))
* 将`riscv64-npc`改为`riscv32e-npc`
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/d341fb23a0d3e032e93ca3d3486f7622450e2a72))
  * 为`riscv32e-npc`添加libgcc的若干支持, 用软件模拟乘除指令
  ([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/a4d3661c31570eec6c87be650f6446bdd6099ea8))
* 添加用于生成logisim镜像文件的python脚本
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/83ac97b4d90c2f4cdd0ecc043a93885d0d3c29a1))
* 修复`riscv.h`中通用寄存器数量在rve中不正确的问题
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/b1586e033693a3616b988200658342d6ff90569c))
* 修复`riscv32-nemu`中错误采用rve ABI的问题
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/8878f1f6ce19c3fa0d9a9414e7a8c121116f31e1))

#### am-kernels

* 修复native在glibc 2.39上运行thread-os时发生栈溢出的问题
([补丁](https://github.com/NJU-ProjectN/am-kernels/commit/245c069c4efae82358a292a2d9dbdf9c1584fcbc))
* 新增ALU test, bf等应用, 移植自[movfuscator项目](https://github.com/xoreaxeaxeax/movfuscator)

#### navy-apps

* 修复native在glibc 2.39上段错误的问题
([补丁](https://github.com/NJU-ProjectN/navy-apps/commit/fd219c457db2b83a6e36f007079a6025b6fb3d1f))
* 修复`LD_PRELOAD`影响gdb的问题
([补丁](https://github.com/NJU-ProjectN/navy-apps/commit/378380f4ecf51c4d65f4a475bdf66a91e95913db))
* 将CRT中`_start`的定义集中在一个文件中, 方便使用`__riscv`宏进行判断
([补丁](https://github.com/NJU-ProjectN/navy-apps/commit/8fe76b4e50cc03c2d17e284f57f9e0d6e80e0c2f))
* 新增riscv32e
([补丁](https://github.com/NJU-ProjectN/navy-apps/commit/0e782aa991e68b456c3cee4233b95c2ba4c7b820))
* 修复`README.md`中的错误
([补丁](https://github.com/NJU-ProjectN/navy-apps/commit/f7209826eebd4011ac4a5d97f2a880e9c71d17c7))
* 添加缺失的文件`scripts/riscv/common.mk`
([补丁](https://github.com/NJU-ProjectN/navy-apps/commit/754fea853eaa91baf448b20464adb37f53798dff))

### ICS2022

#### nemu

* 在menuconfig中选中`Enable Debug`时默认采用`-Og`编译
* 去掉RTL中间表示, 用"抄手册"宏重构译码部分
([补丁](https://github.com/NJU-ProjectN/nemu/commit/6892cee4d95ff628d878b4a0f6a9f887c9d5d626))
* 添加NEMU作为REF的API(一生一芯中使用)
([补丁](https://github.com/NJU-ProjectN/nemu/commit/55e43218041ddacd4487b4bdc4e15251b4ab9e03))
* 使用ssh从github上克隆spike
([补丁](https://github.com/NJU-ProjectN/nemu/commit/d65fa540caf35cf1a7e42b26de1fe09dbca7cc42))
* 修复因`optind`重定位错误导致spike触发段错误
([补丁](https://github.com/NJU-ProjectN/nemu/commit/8521f46acae2ada40ad067a4c0513f504cdd42d7))
* 去掉调用`dlopen()`时不使用的`RTLD_DEEPBIND`
([补丁](https://github.com/NJU-ProjectN/nemu/commit/d2de05d7d3f2ef8ae13403bc687be4a1a19c4aac))
* 交换itrace中输出的字节序, 使其符合RISC-V的阅读习惯
([补丁](https://github.com/NJU-ProjectN/nemu/commit/161eb8dcc4ed1616f9e70db8d32bb31b80dd4697))
* 修复pmem右边界的计算
([补丁](https://github.com/NJU-ProjectN/nemu/commit/e9fd223f3d6c793c8ce5732ff183b9b98d3787d9))
* 修复`uint64_t`的格式说明符
([补丁](https://github.com/NJU-ProjectN/nemu/commit/c52dfec86a496a2399ef0aa1f8b54584ab3b7ce6))
* 添加MMIO区间重叠的检查
([补丁](https://github.com/NJU-ProjectN/nemu/commit/a1813e5e6f1ae0668da31d76b04517a189924068))

#### abstract-machine

* 使用标准调试指令实现`nemu_trap`
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/d5fe878987b6f4b547c81b71897eabb7fb250940))
* 默认使用通常模式(而不是批处理模式)来运行NEMU
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/198ce9035281a5bc041c7b3213c2a3daacc091fa))
* 修复ubuntu 21.10下因glibc中的`SIGSTKSZ`展开为函数调用而导致native编译出错的问题
([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/112799e02a28d22f03cfe496fe36408112047a71))
  * 放宽`SIGSTKSZ`的检查条件
  ([补丁](https://github.com/NJU-ProjectN/abstract-machine/commit/7c9b27be201ba70fa7793cab7efe822d8e951eee))

#### am-kernels

* 修复cpu-tests不支持gdb目标的问题
([补丁](https://github.com/NJU-ProjectN/am-kernels/commit/adc316af6e482e6444a9bd68bafc3a57e2cafdbc))

#### nanos-lite

* 修复`sizeof(struct timeval)`在glibc和newlib中不一致的问题
([补丁](https://github.com/NJU-ProjectN/nanos-lite/commit/2a141760e31be246a7316942293a97873925bc2f))

#### navy-apps

* 使用ssh从github上克隆子仓库
([补丁](https://github.com/NJU-ProjectN/navy-apps/commit/13ba3997899ca9fe83e4c4c98a498ea06d41cfdd))
