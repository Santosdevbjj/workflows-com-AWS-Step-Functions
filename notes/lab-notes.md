# Laboratório: Explorando Workflows Automatizados com AWS Step Functions

## Objetivo

Consolidar conhecimentos sobre orquestração de workflows utilizando AWS Step Functions e sua integração com serviços da AWS, como:

- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Amazon ECS
- Amazon EKS
- Amazon CloudWatch

---

# Contexto

Aplicações modernas são compostas por diversos serviços distribuídos. Coordenar a execução desses serviços utilizando apenas código pode aumentar a complexidade e dificultar manutenção, monitoramento e recuperação de falhas.

O AWS Step Functions resolve esse problema através de máquinas de estados (State Machines), permitindo construir workflows visuais e resilientes.

---

# Atividades Realizadas

## 1. Estudo dos conceitos do AWS Step Functions

Conceitos estudados:

- State Machine
- Task State
- Choice State
- Pass State
- Succeed State
- Fail State
- Retry
- Catch
- ResultPath

---

## 2. Integração com AWS Lambda

Foram criadas três funções Lambda:

### validate_file

Responsável pela validação do arquivo.

### process_data

Responsável pelo processamento.

### notify_execution

Responsável pela publicação de eventos.

---

## 3. Integração com SNS

Implementado padrão Publish/Subscribe para desacoplar produtores e consumidores.

Benefícios:

- Escalabilidade;
- Baixo acoplamento;
- Comunicação assíncrona.

---

## 4. Integração com SQS

Implementado processamento baseado em filas.

Benefícios:

- Buffer de mensagens;
- Tolerância a picos de carga;
- Maior resiliência.

---

## 5. Persistência com DynamoDB

Simulação de armazenamento de metadados dos arquivos processados.

---

## 6. Tratamento de erros

Aplicação dos padrões:

- Retry
- Catch
- Fail State

---

## 7. Observabilidade

Estudo das integrações com:

- Amazon CloudWatch
- AWS X-Ray
- CloudTrail

---

# Arquitetura Final

S3
↓
Step Functions
↓
Lambda
↓
SNS
↓
SQS
↓
DynamoDB
↓
CloudWatch

---

# Tecnologias Utilizadas

- AWS Step Functions
- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Python 3.13
- Amazon CloudWatch

---

# Resultado

O laboratório permitiu compreender como aplicações serverless modernas utilizam workflows para coordenar serviços distribuídos com alta escalabilidade e observabilidade.
