docker-compose build --parallel
docker login -u ${username} -p ${password}
docker-compose push