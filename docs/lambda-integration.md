# Integração entre AWS Step Functions e AWS Lambda

# Introdução

Uma das integrações mais utilizadas no AWS Step Functions é com o AWS Lambda.

Essa combinação permite criar aplicações serverless capazes de executar processos complexos sem a necessidade de gerenciar servidores, utilizando workflows visuais, escaláveis e resilientes.

Neste projeto, o AWS Step Functions é responsável por orquestrar a execução das funções Lambda, coordenando o fluxo das operações e garantindo tratamento adequado para falhas e monitoramento das execuções.

---

# Problema

Em aplicações modernas, é comum que diferentes tarefas precisem ser executadas em sequência:

- Validar arquivos;
- Processar dados;
- Aplicar regras de negócio;
- Enviar notificações;
- Registrar logs;
- Persistir informações.

Implementar essa lógica diretamente nas aplicações aumenta:

- O acoplamento entre componentes;
- A complexidade do código;
- A dificuldade de manutenção;
- O tratamento manual de falhas.

O AWS Step Functions resolve esse problema atuando como uma camada de orquestração.

---

# Arquitetura

```text
             AWS Step Functions
                     |
                     ▼
            +-----------------+
            | Validate File    |
            | Lambda Function  |
            +-----------------+
                     |
                     ▼
            +-----------------+
            | Process Data     |
            | Lambda Function  |
            +-----------------+
                     |
                     ▼
            +-----------------+
            | Notify Execution |
            | Lambda Function  |
            +-----------------+
```

---

# Funções Lambda Implementadas

## Validate File

Responsável por:

- Verificar nome do arquivo;
- Validar extensão;
- Garantir integridade dos dados;
- Aplicar regras de negócio.

Entrada:

```json
{
  "filename": "clientes.csv"
}
```

Saída:

```json
{
  "valid": true
}
```

---

## Process Data

Responsável por:

- Processar os dados recebidos;
- Aplicar transformações;
- Preparar informações para armazenamento.

Entrada:

```json
{
  "valid": true
}
```

Saída:

```json
{
  "status": "processed"
}
```

---

## Notify Execution

Responsável por:

- Informar sucesso da execução;
- Publicar eventos;
- Acionar notificações.

Saída:

```json
{
  "notification": "success"
}
```

---

# Fluxo da Execução

```text
Início
   |
   ▼
Validate File
   |
Arquivo válido?
   |
  Sim
   ▼
Process Data
   |
   ▼
Notify Execution
   |
   ▼
Fim
```

---

# Definição do State Machine

Exemplo utilizando Amazon States Language:

```json
{
  "StartAt": "ValidateFile",
  "States": {
    "ValidateFile": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGIAO:CONTA:function:validate-file",
      "Next": "ProcessData"
    },

    "ProcessData": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGIAO:CONTA:function:process-data",
      "Next": "NotifyExecution"
    },

    "NotifyExecution": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGIAO:CONTA:function:notify-execution",
      "End": true
    }
  }
}
```

---

# Tratamento de Falhas

Uma das vantagens do Step Functions é a capacidade de realizar retries automáticos.

Exemplo:

```json
"Retry": [{
  "ErrorEquals": ["States.ALL"],
  "IntervalSeconds": 2,
  "MaxAttempts": 3,
  "BackoffRate": 2
}]
```

Benefícios:

- Maior resiliência;
- Recuperação automática;
- Menor intervenção manual.

---

# Tratamento de Exceções

Também é possível capturar erros utilizando Catch.

Exemplo:

```json
"Catch": [{
  "ErrorEquals": ["States.ALL"],
  "Next": "HandleError"
}]
```

Fluxo:

```text
Lambda
   |
Erro?
   |
 Sim
   ▼
Handle Error
```

---

# Vantagens da Integração

## Serverless

Não há necessidade de gerenciar servidores.

---

## Escalabilidade Automática

As funções Lambda escalam sob demanda.

---

## Baixo Acoplamento

A lógica de orquestração fica separada da lógica de negócio.

---

## Observabilidade

Todas as execuções são registradas no CloudWatch.

---

## Resiliência

Retry automático e tratamento de exceções.

---

## Menor Complexidade

Os fluxos ficam centralizados em uma máquina de estados.

---

# Boas Práticas

## Funções Pequenas

Cada Lambda deve possuir uma única responsabilidade.

Exemplo:

✅ Validate File

✅ Process Data

✅ Notify Execution

Evitar:

❌ Uma única Lambda fazendo todas as tarefas.

---

## Idempotência

A execução da mesma função várias vezes não deve gerar inconsistências.

---

## Timeout Configurado

Evitar execuções longas.

---

## Logs Estruturados

Utilizar CloudWatch Logs.

---

## Tratamento de Exceções

Implementar Catch e Retry.

---

## Separação da Lógica de Negócio

Step Functions deve orquestrar.

Lambda deve executar.

---

# Casos de Uso

- ETL;
- Processamento de arquivos;
- Microsserviços;
- Machine Learning;
- APIs Serverless;
- Processamento assíncrono;
- Workflows empresariais.

---

# Conclusão

A integração entre AWS Step Functions e AWS Lambda permite construir aplicações modernas, resilientes e escaláveis, reduzindo a complexidade da lógica de orquestração e aumentando a observabilidade dos processos.

Essa arquitetura é amplamente utilizada em ambientes serverless e aplicações distribuídas baseadas em eventos.
