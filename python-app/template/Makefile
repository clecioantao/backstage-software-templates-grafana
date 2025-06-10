# Makefile para subir o stack Grafana + Loki + Prometheus + Flask + Promtail com ulimit adequado

NETWORK=template_monitoring
LOGS_DIR=$(PWD)/logs
PROMTAIL_CONFIG=$(PWD)/promtail-config.yaml

up:
	docker compose up -d --build --force-recreate
	sleep 3
	docker rm -f promtail || true
	docker run -d --name promtail \
		--ulimit nofile=65536:65536 \
		-v "$(LOGS_DIR):/var/log/flask" \
		-v "$(PROMTAIL_CONFIG):/etc/promtail/promtail.yaml" \
		--network $(NETWORK) \
		grafana/promtail:2.9.2 \
		-config.file=/etc/promtail/promtail.yaml

down:
	docker compose down --remove-orphans
	docker rm -f promtail || true

logs:
	docker logs -f promtail

status:
	docker ps --filter "name=promtail"

