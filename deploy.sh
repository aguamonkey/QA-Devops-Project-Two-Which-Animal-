#!/bin/bash

project_name=which_animal_am_i

#Build Server
docker build -t ${project_name}_server service1

#Build animal_name API
docker build -t ${project_name}_name_api service2 

docker build -t ${project_name}_luck_api service3 

docker build -t ${project_name}_fortune_api service4 

#you'd build as many machines as you need, so 4 for your project

#Create network
docker network create ${project_name}_network

#Run containers
docker run -d \
    -p 5000:5000 \
    --name ${project_name}_server \
    --network ${project_name}_network \
    ${project_name}_server

docker run -d \
    --name ${project_name}_name_api \
    --network ${project_name}_network \
    ${project_name}_name_api

docker run -d \
    --name ${project_name}_luck_api \
    --network ${project_name}_network \
    ${project_name}_luck_api

docker run -d \
    --name ${project_name}_fortune_api \
    --network ${project_name}_network \
    ${project_name}_fortune_api