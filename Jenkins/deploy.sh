scp docker-compose.yaml docker-manager:
ssh docker-manager << EOF
export SECRET_KEY=${SECRET_KEY}
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml which_animal_am_i_server
docker exec which_animal_am_i_server python create.py
EOF