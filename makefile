up:
	docker compose up -d
u:
	make up
down:
	docker compose down
d:
	make down
du:
	make d
	make u
logs:
	docker compose logs -f
ul:
	make up
	make logs
dv:
	docker compose down -v
dvul:
	make dv
	make ul
a:
	docker exec -it namenode bash
h:
	docker exec -it hive-server bash 
push:
	git add --all
	git commit -m ":pray:"
	git push
