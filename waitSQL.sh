#!/bin/bash

echo "Waiting for mysql"
#until mysql -h $1 -P$2 -uroot -p$3 &> /dev/null
until mysql -h 172.0.0.2 -P3306 -uroot -proot &> /dev/null
do
  printf "."
  sleep 1
done

echo -e "\nmysql ready"