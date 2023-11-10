# 一生一芯文档站

+ Production environment: [ysyx.org](docs.ysyx.org)

+ Development environment: [ysyx.dev](docs.ysyx.dev)

## Environment setup

Note: documentation framework 'vuepress' requires `NodeJS` and its default
package manager `NPM` to work properly. If you do not have these depencencies
installed, please follow this [guide](https://nodejs.org/en/download/package-manager/).

1. Initialize git submodules on a fresh clone.
    ```sh
    git submodule init
    ```

1. (Optional) Setup mirrors for the package manager.
    ```sh
    # Setup china mirror for npm
    npm config set registry=https://registry.npmmirror.com
    ```

1. Install dependencies.
    ```sh
    npm install
    ```
## Local development preview
```sh
# Launch local development server
npm run dev
```
## Build and deploy (at the server)
```sh
# Get latest commit
git pull
# Update submodules
git submodule update
# Deploy for production
npm run deploy
# Domain: ysyx.oscc.cc 
# 账号密码是一生一芯的账号密码
```

# 错误排查

1. `Node: unable to import XXX` (无法导入 node 依赖包)

    可能是新增了依赖包，在项目目录下运行 `npm i`

1. 预览页面弹窗提示找不到组件 `Error: ..., dose the file ***.vue exist?`

    git submodule `common` 没有成功拉取，这种情况可能是因为 git submodule 报错退出

    手动拉取子仓库:

    ```sh
    rm -rf ./common
    git clone git@github.com:ysyx-org/frontend-common ./common
    ```

1. 运行 Node 脚本时提示语法错误

    检查 NodeJS 版本（建议升级至 18.4.x）

    升级方法: [Node Binary Distribution](https://github.com/nodesource/distributions#installation-instructions)

1. 预览的页面有组件缺失 (比如导航栏显示为空白)

    npm 安装的依赖包版本需要升级, 使用 `npm run upgrade` 可以解决