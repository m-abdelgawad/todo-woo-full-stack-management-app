# Create networks
docker network create automagic-front-end
docker network create automagic-back-end

# Create the "static" volume
docker volume create automagic-static

# Database container
docker build ./postgres -t automagic-db
docker run -d --name db -v "$(pwd)/mounts/postgres_data":/var/lib/postgresql/data --network=automagic-back-end automagic-db

# SysMonitor container
docker build ./sysmonitor/ -t monitor
docker run -d --privileged --pid=host --name monitor --network=automagic-back-end monitor

# App container
docker build ./app/ -t automagic-app
docker create --name app -v automagic-static:/website/static -v "$(pwd)/mounts/media":/website/media --env-file app/.env --network=automagic-front-end automagic-app
docker network connect automagic-back-end app
docker start app

# Nginx container
docker build ./nginx/ -t automagic-nginx
docker run -d --name nginx -p 80:80 -p 443:443 -v "$(pwd)/mounts/media":/media -v automagic-static:/static --network=automagic-front-end \
	-v "$(pwd)/mounts/letsencrypt":/etc/letsencrypt automagic-nginx

# Verify status
docker ps
