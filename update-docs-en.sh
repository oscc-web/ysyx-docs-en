#!/usr/bin/env bash

set -e

PATH_ROOT=${PWD}
PATH_DOCS_EN=${PATH_ROOT}/src/en/

if [ ! -d ${PATH_DOCS_EN}/.git ]; then
    echo ""
    echo "Downloading ysyx-docs-en..."
    rm -rf ${PATH_DOCS_EN}
    git clone git@github.com:oscc-web/ysyx-docs-en.git ${PATH_DOCS_EN}
else
    echo ""
    echo "Updating ysyx-docs-en..."
    cd ${PATH_DOCS_EN}
    git pull origin main
    cd ${PATH_ROOT}
fi
