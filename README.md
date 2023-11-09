# 一生一芯文档站-en

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
    sudo npm i cnpm -g --registry=https://registry.npmmirror.com
    ```

1. Install dependencies.
    ```sh
    # For those NOT using a mirror
    npm i
    # Using china mirror
    cnpm i
    ```
## Local development preview
```sh
# Launch local development server
npm run dev
```
## Build and deploy (at the server)
```sh
# Make sure you are on branch master
git checkout master
# Get latest commit
git pull
# Update submodules
git submodule update
# Build for production
npm run build
```
