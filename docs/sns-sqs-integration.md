# Integração entre Amazon SNS e Amazon SQS

# Introdução

Em arquiteturas modernas orientadas a eventos (Event-Driven Architecture), é fundamental desacoplar componentes para aumentar a escalabilidade, a resiliência e a flexibilidade das aplicações.

Neste projeto, o AWS Step Functions utiliza os serviços Amazon SNS e Amazon SQS para implementar comunicação assíncrona entre componentes, permitindo que diferentes serviços processem eventos de forma independente.

---

# Problema

Em aplicações distribuídas, quando os componentes dependem diretamente uns dos outros, surgem problemas como:

- Alto acoplamento;
- Baixa escalabilidade;
- Propagação de falhas;
- Dificuldade de manutenção;
- Perda de mensagens;
- Baixa tolerância a indisponibilidades.

O desacoplamento através de mensageria resolve esses problemas.

---

# Arquitetura da Solução

```text
                AWS Step Functions
                         |
                         ▼
                 AWS Lambda Process
                         |
                         ▼
                    Amazon SNS
                         |
         ----------------------------------
         |                |               |
         ▼                ▼               ▼
      SQS Queue A     SQS Queue B     SQS Queue C
         |                |               |
         ▼                ▼               ▼
      Consumer A      Consumer B      Consumer C
```

---

# Amazon SNS

O Amazon Simple Notification Service (SNS) é um serviço de publicação e assinatura (Pub/Sub) utilizado para distribuir mensagens para múltiplos consumidores.

## Características

- Alta disponibilidade;
- Escalabilidade automática;
- Entrega quase em tempo real;
- Comunicação desacoplada;
- Integração com diversos serviços AWS.

---

# Amazon SQS

O Amazon Simple Queue Service (SQS) é um serviço de filas responsável por armazenar mensagens até que sejam processadas.

## Benefícios

- Processamento assíncrono;
- Garantia de entrega;
- Tolerância a falhas;
- Escalabilidade;
- Redução do acoplamento.

---

# Fluxo do Processo

```text
Início
   |
   ▼
Step Functions
   |
   ▼
Lambda Process Data
   |
   ▼
SNS Topic
   |
   ▼
SQS Queue
   |
   ▼
Consumer
```

---

# Publicação da Mensagem

Após o processamento, uma Lambda publica um evento no SNS.

Exemplo:

```json
{
  "event": "file_processed",
  "filename": "clientes.csv",
  "status": "success"
}
```

---

# Distribuição das Mensagens

O SNS pode enviar a mesma mensagem para diversos destinos:

- Filas SQS;
- AWS Lambda;
- HTTP Endpoints;
- Email;
- SMS.

Exemplo:

```text
Evento Publicado
       |
       ▼
      SNS
 ┌─────┼─────┐
 ▼     ▼     ▼
SQS1  SQS2  SQS3
```

---

# Processamento Assíncrono

Cada consumidor processa a mensagem independentemente.

Benefícios:

- Paralelismo;
- Escalabilidade;
- Resiliência.

---

# Dead Letter Queue (DLQ)

Mensagens que falham repetidamente podem ser enviadas para uma fila especial.

```text
SQS Principal
       |
Erro após tentativas
       |
       ▼
Dead Letter Queue
```

Benefícios:

- Investigação de falhas;
- Reprocessamento posterior;
- Maior confiabilidade.

---

# FIFO Queue

Quando a ordem das mensagens é importante, utiliza-se uma fila FIFO.

Características:

- Ordem garantida;
- Deduplicação automática.

Aplicações:

- Processamento financeiro;
- Pedidos;
- Transações.

---

# Integração com AWS Step Functions

Exemplo simplificado:

```text
Validate File
      |
      ▼
Process Data
      |
      ▼
Publish Event
      |
      ▼
SNS Topic
      |
      ▼
SQS Queue
      |
      ▼
Consumer Service
```

---

# Padrões Arquiteturais Aplicados

## Publish/Subscribe Pattern

Um produtor publica eventos para diversos consumidores.

---

## Queue-Based Load Leveling

A fila absorve picos de carga.

---

## Event-Driven Architecture

Os componentes se comunicam através de eventos.

---

## Loose Coupling

Serviços independentes.

---

# Benefícios

## Escalabilidade

Os consumidores podem ser escalados independentemente.

---

## Resiliência

Falhas em um consumidor não afetam os demais.

---

## Disponibilidade

As mensagens permanecem armazenadas até serem processadas.

---

## Baixo Acoplamento

Serviços independentes entre si.

---

## Alta Performance

Processamento assíncrono.

---

# Boas Práticas

## Utilizar Dead Letter Queue

Para capturar mensagens com falha.

---

## Implementar Idempotência

Evitar processamento duplicado.

---

## Monitorar Filas com CloudWatch

Acompanhar:

- Número de mensagens;
- Tempo de permanência;
- Taxa de erro.

---

## Utilizar FIFO quando necessário

Garantir ordem das mensagens.

---

## Configurar Visibility Timeout

Evitar processamento duplicado.

---

# Casos de Uso

- Microsserviços;
- Processamento de arquivos;
- ETL;
- Notificações;
- IoT;
- Machine Learning;
- Processamento em lote.

---

# Conclusão

A combinação entre Amazon SNS e Amazon SQS permite construir sistemas distribuídos altamente resilientes e escaláveis.

Essa abordagem reduz o acoplamento entre componentes e constitui um dos padrões mais utilizados em arquiteturas modernas baseadas em eventos.
