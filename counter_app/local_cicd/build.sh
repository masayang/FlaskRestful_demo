#! /bin/bash

rm requirements.txt
rm -rf app
pip freeze > requirements.txt
cp -r ../../counter_app/app .
docker-compose up -d --build
