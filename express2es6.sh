#! /bin/bash

if [ $# -eq 1 ]; then
  path=$1
fi

if [ ! -d $path/src ]; then
  mkdir $path/src
fi

mv $path/{bin,routes,views,app.js} $path/src

cat $path/src/routes/index.js

formattedString=$(python3 ./format.py \"$(cat $path/src/routes/index.js)\")

echo $formattedString

if [ -f $path/bin/www ]; then
  mv $path/bin/www $path/bin/www.js
fi