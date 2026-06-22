# Monitoramento e Observabilidade com AWS Step Functions

# Introdução

Construir workflows distribuídos é apenas parte da solução. Em ambientes modernos, tão importante quanto executar processos é ser capaz de entender o que está acontecendo durante a execução.

A observabilidade permite identificar falhas, analisar desempenho, medir métricas e garantir que os workflows operem de forma confiável.

Neste projeto, os mecanismos de monitoramento são implementados utilizando principalmente:

- AWS Step Functions
- Amazon CloudWatch
- AWS CloudTrail
- AWS X-Ray
- Logs das funções Lambda

Esses serviços permitem obter visibilidade completa sobre o comportamento das aplicações.

---

# Problema

Em sistemas distribuídos, diversos problemas podem ocorrer:

- Falhas temporárias;
- Timeouts;
- Erros de integração;
- Perda de mensagens;
- Lentidão no processamento;
- Problemas em funções Lambda;
- Falhas em containers;
- Gargalos em filas SQS.

Sem observabilidade, identificar a origem desses problemas torna-se uma tarefa complexa.

---

# Conceitos Fundamentais

## Monitoramento

Consiste em coletar métricas e acompanhar o comportamento dos sistemas.

Exemplos:

- Tempo de execução;
- Taxa de sucesso;
- Número de erros;
- Utilização de recursos.

---

## Observabilidade

Vai além do monitoramento.

Permite responder perguntas como:

- O que aconteceu?
- Quando aconteceu?
- Onde aconteceu?
- Por que aconteceu?

Os três pilares da observabilidade são:

- Logs;
- Métricas;
- Traces.

---

# Arquitetura de Observabilidade

```text
                AWS Step Functions
                         |
          ---------------------------------
          |               |               |
          ▼               ▼               ▼
     CloudWatch       CloudTrail       X-Ray
          |
          ▼
     Logs e Métricas
```

---

# Amazon CloudWatch

O Amazon CloudWatch é responsável por coletar:

- Logs;
- Métricas;
- Eventos;
- Alarmes.

Ele é o principal serviço de monitoramento da AWS.

---

# Histórico das Execuções

O AWS Step Functions mantém o histórico completo das execuções.

Informações disponíveis:

- Hora de início;
- Hora de término;
- Estados executados;
- Tempo de execução;
- Falhas;
- Dados de entrada;
- Dados de saída.

---

# Logs do CloudWatch

Cada execução pode ser registrada automaticamente.

Exemplo:

```text
Execution Started

State: ValidateFile

State: ProcessData

State: PublishNotification

Execution Succeeded
```

Benefícios:

- Rastreabilidade;
- Auditoria;
- Diagnóstico.

---

# Métricas Importantes

## ExecutionsStarted

Número de execuções iniciadas.

---

## ExecutionsSucceeded

Quantidade de execuções bem-sucedidas.

---

## ExecutionsFailed

Quantidade de falhas.

---

## ExecutionsTimedOut

Execuções que excederam o tempo máximo.

---

## ExecutionTime

Tempo médio de execução.

---

# Alarmes do CloudWatch

Permitem detectar comportamentos anormais.

Exemplos:

### Muitas falhas

```text
ExecutionsFailed > 10
```

---

### Tempo excessivo

```text
ExecutionTime > 30 segundos
```

---

### Timeout

```text
ExecutionsTimedOut > 0
```

---

# Logs das Funções Lambda

As funções Lambda enviam automaticamente logs para o CloudWatch.

Exemplo:

```python
import logging

logger = logging.getLogger()

logger.info("Arquivo validado com sucesso")
```

Benefícios:

- Diagnóstico;
- Auditoria;
- Troubleshooting.

---

# AWS CloudTrail

Responsável pelo registro das ações realizadas na conta AWS.

Exemplos:

- Criação de workflows;
- Exclusão de recursos;
- Alterações em permissões;
- Execuções de APIs.

Benefícios:

- Auditoria;
- Segurança;
- Compliance.

---

# AWS X-Ray

Permite rastreamento distribuído (Distributed Tracing).

Exemplo:

```text
Step Functions
     |
     ▼
Lambda
     |
     ▼
SNS
     |
     ▼
SQS
```

Com o X-Ray é possível identificar:

- Latência;
- Gargalos;
- Dependências;
- Falhas entre serviços.

---

# Dashboards

O CloudWatch permite criar dashboards para acompanhar:

- Número de execuções;
- Tempo médio;
- Erros;
- Métricas das Lambdas;
- Filas SQS;
- SNS;
- Containers ECS.

---

# Padrões de Observabilidade

## Logs

Registro detalhado dos eventos.

---

## Metrics

Indicadores quantitativos.

---

## Traces

Fluxo completo das requisições.

---

# Boas Práticas

## Ativar Logs do Step Functions

Permite rastreamento completo.

---

## Monitorar Falhas

ExecutionsFailed.

---

## Criar Alarmes

Notificações automáticas.

---

## Utilizar CloudTrail

Garantir auditoria.

---

## Utilizar AWS X-Ray

Analisar dependências entre serviços.

---

## Implementar Logs Estruturados

Exemplo:

```json
{
  "level": "INFO",
  "event": "validation_success",
  "filename": "clientes.csv"
}
```

---

## Criar Dashboards

Visualização centralizada.

---

# Indicadores Importantes

- Taxa de sucesso;
- Tempo médio;
- Número de falhas;
- Throughput;
- Tempo em filas;
- Uso de memória das Lambdas;
- Latência.

---

# Benefícios da Observabilidade

## Maior Confiabilidade

Falhas são identificadas rapidamente.

---

## Redução do MTTR

Mean Time To Recovery.

---

## Melhor Performance

Identificação de gargalos.

---

## Maior Disponibilidade

Monitoramento contínuo.

---

## Escalabilidade

Acompanhamento do crescimento da aplicação.

---

# Conclusão

Monitoramento e observabilidade são componentes essenciais de arquiteturas modernas.

A combinação entre AWS Step Functions, CloudWatch, CloudTrail e X-Ray fornece visibilidade completa sobre os workflows, permitindo construir aplicações resilientes, auditáveis e alinhadas às melhores práticas do AWS Well-Architected Framework.
