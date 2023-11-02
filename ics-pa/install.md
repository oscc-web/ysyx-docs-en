```bash
# see https://github.com/GitbookIO/gitbook/blob/master/docs/setup.md
apt-get install npm
npm install gitbook-cli -g

# fix `TypeError: cb.apply is not a function`
# see https://stackoverflow.com/questions/64211386/gitbook-cli-install-error-typeerror-cb-apply-is-not-a-function-inside-graceful
cd /usr/local/lib/node_modules/gitbook-cli/node_modules/npm/node_modules/
npm install graceful-fs@4.2.0 --save

gitbook update
```
