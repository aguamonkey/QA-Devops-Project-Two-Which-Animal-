scp docker-compose.yaml manager-node:
ssh manager-node << EOF
export SECRET_KEY=${SECRET_KEY}
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml app
EOF