scp docker-compose.yaml docker:
ssh docker << EOF
#export SECRET_KEY=${SECRET_KEY}
export DATABASE_URI=${DATABASE_URI}
ssh -oStrictHostKeyChecking=no host
docker exec which_animal_am_i_server python3 create.py
docker stack deploy --compose-file docker-compose.yaml app
EOF