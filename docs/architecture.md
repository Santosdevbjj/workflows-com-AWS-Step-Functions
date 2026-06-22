# Arquitetura da Solução

## Visão Geral

Este projeto demonstra como utilizar o AWS Step Functions para coordenar serviços distribuídos em uma arquitetura orientada a eventos (Event-Driven Architecture), permitindo a automação de processos com baixo acoplamento, alta observabilidade e maior resiliência.

A solução implementa uma máquina de estados (State Machine) responsável por validar arquivos, acionar funções Lambda, publicar mensagens e coordenar serviços da AWS de forma visual e escalável.

---

# Problema

Em arquiteturas modernas, diversos componentes precisam trabalhar em conjunto:

- Amazon S3
- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Amazon ECS
- Amazon EKS

Quando a coordenação dessas etapas é feita manualmente, o sistema tende a apresentar:

- Alto acoplamento;
- Maior complexidade de manutenção;
- Dificuldade de monitoramento;
- Tratamento de falhas mais complexo;
- Baixa observabilidade;
- Dificuldade de escalabilidade.

O AWS Step Functions resolve esse problema atuando como uma camada de orquestração centralizada.

---

# Arquitetura Geral

```text
                +-------------+
                |   Amazon S3 |
                +-------------+
                       |
                       ▼
           +----------------------+
           | AWS Step Functions    |
           | State Machine         |
           +----------------------+
                       |
          ┌────────────┴────────────┐
          ▼                         ▼
+----------------+         +----------------+
| AWS Lambda     |         | AWS Lambda     |
| Validate File  |         | Process Data   |
+----------------+         +----------------+
          |                         |
          └────────────┬────────────┘
                       ▼
               +---------------+
               | Amazon SNS    |
               +---------------+
                       |
                       ▼
               +---------------+
               | Amazon SQS    |
               +---------------+
                       |
                       ▼
               +----------------+
               | DynamoDB        |
               +----------------+
                       |
                       ▼
               +----------------+
               | CloudWatch      |
               +----------------+
```

---

# Fluxo da Aplicação

## 1. Recebimento do Evento

Um arquivo é disponibilizado para processamento.

O workflow é iniciado pelo Step Functions.

---

## 2. Validação

Uma função Lambda é acionada para verificar:

- Nome do arquivo;
- Extensão;
- Integridade;
- Regras de negócio.

Caso a validação falhe:

- O fluxo é encerrado;
- O estado Fail é executado.

Caso seja bem-sucedida:

- O processamento continua.

---

## 3. Processamento

Uma segunda função Lambda executa:

- Transformação dos dados;
- Regras de negócio;
- Preparação das informações.

---

## 4. Publicação de Eventos

Após o processamento, uma mensagem é enviada para o Amazon SNS.

Isso permite notificar:

- Serviços externos;
- Microsserviços;
- Filas SQS;
- Aplicações consumidoras.

---

## 5. Mensageria Assíncrona

O Amazon SQS recebe as mensagens para garantir:

- Desacoplamento;
- Processamento assíncrono;
- Tolerância a falhas;
- Maior escalabilidade.

---

## 6. Persistência

Os dados podem ser armazenados no DynamoDB.

Essa etapa permite:

- Consultas rápidas;
- Alta disponibilidade;
- Escalabilidade automática.

---

## 7. Monitoramento

Todas as execuções são registradas no CloudWatch.

São monitorados:

- Logs;
- Tempo de execução;
- Erros;
- Métricas;
- Histórico das execuções.

---

# Componentes da Solução

## AWS Step Functions

Responsável pela orquestração dos fluxos.

Benefícios:

- Construção visual;
- Retry automático;
- Tratamento de exceções;
- Monitoramento integrado;
- Pouco código;
- Escalabilidade.

---

## AWS Lambda

Executa funções sem necessidade de servidores.

Benefícios:

- Serverless;
- Escalabilidade automática;
- Pagamento sob demanda;
- Integração nativa com Step Functions.

---

## Amazon SNS

Responsável pela publicação de eventos.

Permite comunicação do tipo:

- Publisher/Subscriber.

Benefícios:

- Desacoplamento;
- Distribuição de mensagens;
- Alta disponibilidade.

---

## Amazon SQS

Fila de mensagens utilizada para processamento assíncrono.

Benefícios:

- Resiliência;
- Garantia de entrega;
- Escalabilidade.

---

## Amazon DynamoDB

Banco NoSQL totalmente gerenciado.

Benefícios:

- Baixa latência;
- Alta disponibilidade;
- Escalabilidade automática.

---

## Amazon CloudWatch

Serviço responsável pelo monitoramento.

Permite:

- Logs;
- Métricas;
- Alarmes;
- Observabilidade.

---

# Padrões Arquiteturais Utilizados

## Serverless Architecture

A solução utiliza serviços gerenciados pela AWS.

Benefícios:

- Menor custo operacional;
- Escalabilidade automática;
- Redução da complexidade de infraestrutura.

---

## Event-Driven Architecture

Os componentes se comunicam através de eventos.

Benefícios:

- Baixo acoplamento;
- Maior flexibilidade;
- Facilidade de expansão.

---

## State Machine Pattern

Toda a lógica de negócio é modelada como uma máquina de estados.

Benefícios:

- Fluxo visual;
- Melhor rastreabilidade;
- Facilidade de manutenção.

---

## Retry Pattern

Falhas temporárias são tratadas automaticamente.

Benefícios:

- Resiliência;
- Menor necessidade de intervenção manual.

---

## Fail Fast

Erros críticos encerram o workflow imediatamente.

Benefícios:

- Economia de recursos;
- Maior previsibilidade.

---

# Observabilidade

O CloudWatch fornece:

- Logs detalhados;
- Histórico das execuções;
- Métricas de performance;
- Alarmes;
- Rastreamento de erros.

---

# Escalabilidade

A arquitetura é totalmente escalável.

Os serviços utilizados oferecem:

- Escalabilidade automática;
- Alta disponibilidade;
- Tolerância a falhas;
- Processamento distribuído.

---

# Próximas Evoluções

- Integração com EventBridge;
- Distributed Map;
- Parallel State;
- ECS;
- EKS;
- AWS X-Ray;
- CI/CD com GitHub Actions;
- Terraform;
- AWS CDK;
- Microsserviços orientados a eventos.

---

# Conclusão

O AWS Step Functions atua como um orquestrador visual capaz de coordenar serviços distribuídos de maneira simples e resiliente.

Sua integração nativa com Lambda, SNS, SQS, DynamoDB e CloudWatch permite construir aplicações modernas, escaláveis e alinhadas às melhores práticas de arquitetura em nuvem.
