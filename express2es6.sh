#! /bin/bash

if [ $# -eq 1 ]; then
  path=$(pwd)/$1
fi
if [ $# -eq 0 ]; then
  path=$(pwd)/target
fi

# if [ ! -d $path/src ]; then
#   mkdir $path/src
# fi

# www=$(find -P $path -name www)
# if [ -f $www ]; then
#   mv $www $www.js
# fi

# mv $path/{bin,routes,views,app.js} $path/src

# files=$(find $path/ -type f \! \( -type d -name node_modules -prune false \) | grep '\.js$')
# echo 'find .js'
# echo $files

# for file in $files
# do
#   echo $file
#   python3 ./format.py $file
# done

# sed -i '' "s/public/..\/public/" $path/src/app.js


# cd $path
# echo $(pwd)

# npm i --save npm-run-all

# npm install -D @babel/core @babel/cli @babel/preset-env @babel/node
# echo $path
# echo "{ \"presets\": [\"@babel\/preset-env\"]}" > "$path/.babelrc"

# sed -i '' "s/scripts/a\ \"start\": \"node \.\/bin\/www\",/" $path/package.json
sed -i '' "/scripts/ a\\
\"start\": \"node \.\/bin\/www.js\",
" $path/package.json
sed -i '' "/scripts /a\\
\"server\": \"babel-node \.\/src\/bin\/www\",
" $path/package.json
sed -i '' "/scripts /a\\
\"dev\": \"dev\": \"NODE_ENV=development npm-run-all server\",
" $path/package.json
