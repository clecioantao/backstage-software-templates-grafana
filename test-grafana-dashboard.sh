#!/bin/bash

# Teste automatizado para simular métricas e acionar alertas no Grafana
# Autor: Equipe de Observabilidade
# Versão: 1.0

API_URL="http://localhost:5000/api/v1"
LOOP_COUNT=20
DELAY=1

echo "🔁 Iniciando testes para painel: Requisições por Código HTTP (200, 404)"
for i in $(seq 1 $LOOP_COUNT); do
  curl -s "$API_URL/info" > /dev/null
  curl -s "$API_URL/notfound" > /dev/null  # espera-se que retorne 404
done

echo "✅ Requisições 200/404 enviadas."

echo ""
echo "🐢 Testando painel: Duração Média (requisições lentas)"
for i in $(seq 1 10); do
  curl -s "$API_URL/slow" > /dev/null
  sleep 2
done
echo "✅ Simulação de requisições lentas enviada."

echo ""
echo "🧠 Testando painel: Memória (consumo simulado)"
for i in $(seq 1 5); do
  curl -s "$API_URL/memory" > /dev/null
done
echo "✅ Simulação de consumo de memória enviada."

echo ""
echo "🧮 Testando painel: CPU (processamento artificial)"
for i in $(seq 1 5); do
  curl -s "$API_URL/cpu" > /dev/null
done
echo "✅ Simulação de uso de CPU enviada."

echo ""
echo "🚨 Testando ALERTA: Requisições por segundo (alta carga)"
for i in $(seq 1 100); do
  curl -s "$API_URL/info" > /dev/null &
done
wait
echo "✅ Carga alta enviada para simular alerta (>10 req/s)."

echo ""
echo "🔥 Testando ALERTA: Erros 5xx (requisições com erro 500)"
for i in $(seq 1 20); do
  curl -s "$API_URL/error" > /dev/null &
done
wait
echo "✅ Erros 5xx enviados para simular alerta (>0 req/s)."

echo ""
echo "📊 Fim dos testes. Acesse o Grafana para verificar os resultados!"
