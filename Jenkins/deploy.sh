scp docker-compose.yaml docker:
ssh docker << EOF
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml app
EOF