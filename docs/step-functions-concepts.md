# Conceitos Fundamentais do AWS Step Functions

## Introdução

O AWS Step Functions é um serviço de orquestração que permite construir workflows distribuídos utilizando máquinas de estados (State Machines).

Seu principal objetivo é coordenar serviços da AWS e aplicações distribuídas de maneira visual, resiliente e com pouco código.

---

# O que é uma State Machine?

Uma State Machine (Máquina de Estados) representa um fluxo composto por vários estados (States), que são executados sequencialmente ou em paralelo.

Exemplo:

```text
Início
   ↓
Validar Arquivo
   ↓
Processar Dados
   ↓
Enviar Notificação
   ↓
Fim
```

Cada etapa é chamada de State.

---

# Amazon States Language (ASL)

Os workflows são definidos em JSON utilizando a Amazon States Language (ASL).

Exemplo:

```json
{
  "StartAt": "ValidateFile",
  "States": {
    "ValidateFile": {
      "Type": "Task",
      "Next": "ProcessData"
    },
    "ProcessData": {
      "Type": "Task",
      "End": true
    }
  }
}
```

---

# Principais Tipos de States

## Task State

Executa uma tarefa.

Pode invocar:

- AWS Lambda;
- ECS;
- Batch;
- SNS;
- SQS;
- DynamoDB;
- SageMaker.

Exemplo:

```json
{
  "Type": "Task"
}
```

Uso:

- Processamento;
- Validações;
- Regras de negócio.

---

## Pass State

Não executa nenhuma ação.

Apenas encaminha dados para o próximo estado.

Exemplo:

```json
{
  "Type": "Pass"
}
```

Uso:

- Testes;
- Simulações;
- Transformações simples.

---

## Choice State

Permite criar decisões condicionais.

Funciona como um IF/ELSE.

Exemplo:

```text
Arquivo válido?
       |
   Sim ▼ Não
      Processar
          |
         Fail
```

Exemplo JSON:

```json
{
  "Type": "Choice"
}
```

Uso:

- Regras de negócio;
- Validações.

---

## Wait State

Pausa a execução por um período determinado.

Exemplo:

```json
{
  "Type": "Wait",
  "Seconds": 30
}
```

Uso:

- Delay;
- Aguardar recursos externos.

---

## Parallel State

Executa múltiplos fluxos simultaneamente.

Exemplo:

```text
                Início
                   |
          ------------------
          |                |
          ▼                ▼
      Lambda A         Lambda B
          |                |
          ----------- -------
                   |
                  Fim
```

Benefícios:

- Redução do tempo total;
- Processamento paralelo.

---

## Map State

Processa uma coleção de itens.

Exemplo:

```text
Arquivo 1
Arquivo 2
Arquivo 3
Arquivo 4
```

Cada item é processado individualmente.

Uso:

- Listas;
- Batch;
- Processamento em massa.

---

## Succeed State

Representa o sucesso da execução.

Exemplo:

```json
{
 "Type":"Succeed"
}
```

---

## Fail State

Representa o encerramento por erro.

Exemplo:

```json
{
 "Type":"Fail"
}
```

---

# Retry

Permite tentar novamente uma operação em caso de falha.

Exemplo:

```json
"Retry": [
{
 "ErrorEquals": ["States.ALL"],
 "IntervalSeconds": 2,
 "MaxAttempts": 3,
 "BackoffRate": 2
}
]
```

Benefícios:

- Resiliência;
- Recuperação automática.

---

# Catch

Captura exceções.

Exemplo:

```json
"Catch": [
{
 "ErrorEquals": ["States.ALL"],
 "Next": "HandleError"
}
]
```

Benefícios:

- Tratamento de falhas;
- Maior confiabilidade.

---

# Express Workflows

Projetados para:

- Alta taxa de eventos;
- Baixa duração;
- Menor custo.

Aplicações:

- APIs;
- Streaming;
- Processamento em massa.

---

# Standard Workflows

Projetados para:

- Longa duração;
- Alta confiabilidade;
- Rastreamento completo.

Aplicações:

- Processos empresariais;
- ETL;
- Aprovações.

---

# Integrações Nativas

O Step Functions integra-se com:

## AWS Lambda

Processamento serverless.

---

## Amazon SQS

Mensageria.

---

## Amazon SNS

Notificações.

---

## DynamoDB

Persistência.

---

## ECS

Containers.

---

## EKS

Kubernetes.

---

## Glue

ETL.

---

## SageMaker

Machine Learning.

---

## Batch

Processamento em lote.

---

# Monitoramento

O CloudWatch fornece:

- Logs;
- Métricas;
- Alarmes;
- Histórico das execuções.

---

# Benefícios do AWS Step Functions

## Baixo Código

Fluxos são construídos visualmente.

---

## Observabilidade

Histórico completo das execuções.

---

## Resiliência

Retry automático.

---

## Escalabilidade

Integração com serviços serverless.

---

## Tratamento de Erros

Catch e Fail States.

---

## Integração Nativa

Mais de 220 serviços AWS suportados.

---

# Casos de Uso

## ETL

Pipeline de dados.

---

## Processamento de Arquivos

Validação e transformação.

---

## Microsserviços

Coordenação entre serviços.

---

## Machine Learning

Treinamento e inferência.

---

## IoT

Processamento de eventos.

---

## Workflows Empresariais

Aprovações e automações.

---

# Conclusão

O AWS Step Functions é um dos principais serviços de orquestração da AWS, permitindo construir workflows distribuídos de forma visual, resiliente e escalável.

Sua capacidade de integrar serviços como Lambda, SQS, SNS, DynamoDB, ECS e EKS o torna uma ferramenta essencial para arquiteturas modernas baseadas em microsserviços e aplicações orientadas a eventos.
