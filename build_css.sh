set -e
set -x
export NPATH=`pwd`/node_modules
cd ./pcss && find *.css | grep -v "^_" | xargs node ${NPATH}/postcss-cli/bin/postcss -d ../static/css --no-map "$@"
echo '--------- BUILD COMPLETED ---------'
