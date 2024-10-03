build:
	docker-compose up -d --build --remove-orphans

up:
	docker-compose up -d --remove-orphans

down:
	docker-compose down

bash:
	docker exec -it case_invoice_module sh

clear:
	$(MAKE) down
	rm -rf vendor || true
	rm .env || true
	rm -rf ./docker/mysql/ || true

restart:
	$(MAKE) down
	$(MAKE) up

reinstall:
	$(MAKE) down
	$(MAKE) build

logs:
	docker logs case_invoice_module

migrate:
	docker exec -it case_invoice_module alembic upgrade head

migrate_fresh:
	$(MAKE) migrate
	docker exec -it case_invoice_module alembic revision --autogenerate
	$(MAKE) migrate
