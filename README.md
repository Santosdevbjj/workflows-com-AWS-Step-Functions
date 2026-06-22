## Formação AWS Cloud Foundations

<img width="105" height="120" alt="1000127839" src="https://github.com/user-attachments/assets/19a72c1f-9f5d-4efc-93db-3fdae64064a0" />



---

# file-validation-workflow


## Fluxo

```
Arquivo Recebido
        |
        ▼
Validate File Lambda
        |
        ▼
Arquivo válido?
   /            \
 Sim            Não
  |               |
  ▼               ▼
Success         Fail 

```

---

## Exemplo de entrada

``` 

{
  "filename": "clientes.csv"
}  


```
---



## Exemplo de saída

```

{
  "filename": "clientes.csv",
  "validationResult": {
    "valid": true
  }
} 



```

---

 
# lambda-execution-workflow



## Fluxo

```
Validate File
      |
      ▼
Process Data
      |
      ▼
Notify Execution
      |
      ▼
Success

```


---


## Fluxo de exceção

```

Validate File
      |
      ▼
Erro?
      |
     Sim
      ▼
Handle Error
      |
      ▼
Fail


```

---


## Exemplo de entrada


```
{
  "filename": "clientes.csv"
}

```

---

## Exemplo de saída


```

{
  "validation": {
    "valid": true
  },
  "processResult": {
    "status": "processed"
  },
  "notification": {
    "status": "notification_sent"
  }
}


```


---


# sns-notification-workflow


## Arquitetura

```

Process Data
      |
      ▼
Publish SNS Event
      |
      ▼
SNS Topic
      |
      ▼
Subscribers
(Lambda, Email, SQS, etc.)


```

---


 # Exemplo de entrada

 ```

{
  "event": "file_processed",
  "filename": "clientes.csv",
  "status": "success"
}


```

---



# Exemplo de mensagem enviada ao SNS

```

{
  "event": "file_processed",
  "filename": "clientes.csv",
  "status": "success"
}

```

---




# Fluxo


```

Process Data
      |
      ▼
Publish Notification
      |
      ▼
SNS Topic
      |
      ▼
Success


```

---


# sqs-processing-workflow

```

Step Functions
       |
       ▼
Send Message
       |
       ▼
Amazon SQS
       |
       ▼
Consumer Service

```

---



# Exemplo de entrada

```

{
  "filename": "clientes.csv",
  "event": "file_processed",
  "status": "success"
}



```

---



# Exemplo de mensagem enviada para SQS

```

{
  "filename": "clientes.csv",
  "event": "file_processed",
  "status": "success"
}



```
---

# Fluxo


```


Step Functions
      |
      ▼
Send Message
      |
      ▼
Amazon SQS
      |
      ▼
Success


```

---


Padrões Arquiteturais Aplicados
Publish/Subscribe Pattern
SNS distribui eventos para múltiplos consumidores.


```

Publisher
    |
    ▼
   SNS
 ┌──┼──┐
 ▼  ▼  ▼
A  B  C


```

---


Queue-Based Load Leveling
SQS absorve picos de carga.

```

Producer
    |
    ▼
   SQS
    |
    ▼
Consumer 

```

---



Retry Pattern
Recuperação automática de falhas transitórias.
Fail Fast
Encerramento controlado em caso de erro. 



---

# complete-serverless-workflow

```
                Amazon S3
                     |
                     ▼
           AWS Step Functions
                     |
                     ▼
              Validate File
                     |
                     ▼
              Process Data
                     |
                     ▼
               Amazon SNS
                     |
                     ▼
               Amazon SQS
                     |
                     ▼
              Amazon DynamoDB
                     |
                     ▼
               CloudWatch Logs

```

---

# Fluxo Completo da State Machine

```

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
Publish Notification (SNS)
   |
   ▼
Send Message (SQS)
   |
   ▼
Persist Metadata (DynamoDB)
   |
   ▼
Success


```

---


# Fluxo de exceção

```
Qualquer estado
       |
       ▼
WorkflowFailed
       |
       ▼
Fail


```

---


# Exemplo de entrada

```

{
  "filename": "clientes.csv"
}



```

---


# Saída esperada

```
{
  "filename": "clientes.csv",
  "validation": {
    "valid": true
  },
  "processing": {
    "status": "processed"
  }
}


```

---


# Padrões Arquiteturais Aplicados

✅ Serverless Architecture
Lambda
SNS
SQS
DynamoDB

---

Step Functions
✅ Event-Driven Architecture
Eventos desacoplados através de SNS e SQS.

---


✅ State Machine Pattern
Orquestração explícita do fluxo.

---

✅ Retry Pattern
Recuperação automática de falhas transitórias.

---

✅ Fail Fast
Interrupção imediata em caso de falha.

---

✅ Publish/Subscribe Pattern
SNS distribui eventos.

---

✅ Queue-Based Load Leveling
SQS absorve picos de processamento.

---

✅ Idempotency Pattern
Permite reprocessamentos seguros. 


---



# Estrutura da pasta

```

glambda/
│
└── validate_file/
    │
    ├── lambda_function.py
    └── requirements.txt


```


---



# Exemplo de entrada

```

{
  "filename": "clientes.csv"
}


```

---


# Saída de sucesso

```

{
  "valid": true,
  "filename": "clientes.csv",
  "message": "Arquivo válido."
}


```

---




# Saída para extensão inválida

```

{
  "valid": false,
  "message": "Extensão de arquivo não suportada."
}


```

--- 


# Logs gerados no CloudWatch

```


START RequestId: xxxxx

INFO Iniciando validação do arquivo
INFO Arquivo recebido: clientes.csv
INFO Arquivo validado com sucesso

END RequestId: xxxxx
REPORT RequestId: xxxxx

```

---



# Fluxo da Lambda


```
AWS Step Functions
         |
         ▼
Process Data Lambda
         |
         ▼
Simula processamento
         |
         ▼
Retorna resultado

```

---


# Exemplo de entrada

```


{
  "filename": "clientes.csv"
}


```

---


# Saída esperada

```


{
  "status": "processed",
  "filename": "clientes.csv",
  "records_processed": 1000,
  "processed_at": "2026-06-22T15:30:10.123456"
}


```

---



# Logs gerados no CloudWatch


```

START RequestId: xxxxx

INFO Iniciando processamento do arquivo
INFO Processando arquivo: clientes.csv
INFO 1000 registros processados com sucesso

END RequestId: xxxxx
REPORT RequestId: xxxxx



```

---


# Boas práticas implementadas

# Logging estruturado

```



logger.info("Processando arquivo")

```

---


# Tratamento de exceções

```

try:
    ...
except Exception as error:
    ...



```

---

# Responsabilidade única

A Lambda é responsável apenas pelo processamento.
A orquestração permanece no AWS Step Functions.



# Desacoplamento

A função pode ser reutilizada por:
Step Functions;
EventBridge;
SQS;
SNS;
API Gateway.


---

# lambda notify_execution


Variáveis de ambiente
Esta Lambda utiliza:

```
TOPIC_ARN

```



Exemplo

```

arn:aws:sns:us-east-1:123456789012:file-processing-topic

```

---

# Fluxo

```

Step Functions
      |
      ▼
Notify Execution Lambda
      |
      ▼
Amazon SNS Topic
      |
      ▼
Subscribers
(E-mail, Lambda, SQS, etc.)


```


---


# Exemplo de entrada

```



{
  "filename": "clientes.csv",
  "status": "processed"
}


```

---

# Mensagem publicada no SNS

```

{
  "event": "file_processed",
  "filename": "clientes.csv",
  "status": "processed"
}


```


---


# Saída da Lambda

```

{
  "status": "notification_sent",
  "message_id": "7caa6b5f-9ef5-5c0c-a8ec-4d61eb31cf17",
  "filename": "clientes.csv"
}


```

---

# Logs gerados no CloudWatch

```

START RequestId: xxxx

INFO Iniciando envio de notificação.
INFO Publicando evento no SNS para arquivo clientes.csv
INFO Mensagem publicada com sucesso. MessageId: 7caa6b5f...

END RequestId: xxxx
REPORT RequestId: xxxx


```

---



# Boas práticas implementadas

## Logging estruturado

```

logger.info("Iniciando envio de notificação")

```

---

# Uso de variável de ambiente

```

TOPIC_ARN = os.getenv("TOPIC_ARN")

```

---


Evita hardcoding.


# Tratamento de exceções

```

try:
    ...
except Exception as error:
    ...


```

---



# Responsabilidade única

Esta Lambda faz apenas:
Construção da mensagem;
Publicação no SNS;
Retorno do resultado.



# Integração desacoplada

Os consumidores do SNS podem ser:
Amazon SQS;
Outra Lambda;
Email;
EventBridge;
HTTP Endpoint.


---

# Estrutura atual da pasta lambda

```
lambda/
│
├── validate_file/
│     ├── lambda_function.py
│     └── requirements.txt
│
├── process_data/
│     ├── lambda_function.py
│     └── requirements.txt
│
└── notify_execution/
      ├── lambda_function.py
      └── requirements.txt


```


Com essas três funções, o projeto já possui uma arquitetura serverless completa baseada em:

```


Step Functions
      ↓
Validate File
      ↓
Process Data
      ↓
Notify Execution
      ↓
Amazon SNS
      ↓
Amazon SQS
      ↓
Consumers


```


em um padrão bastante próximo de aplicações distribuídas modernas utilizadas em ambientes corporativos.

---

examples/input.json
Este arquivo representa a entrada inicial do workflow do AWS Step Functions.


Descrição
Campo
Tipo
Descrição
filename
string
Nome do arquivo que será processado 



---



# examples/output.json

## Fluxo correspondente

```
Input
   |
   ▼
Validate File
   |
   ▼
Process Data
   |
   ▼
Notify Execution
   |
   ▼
Output


```

---


# examples/success-response.json

Representa uma resposta simplificada de sucesso do workflow.


# Cenário

```


Arquivo recebido
       |
       ▼
Arquivo válido
       |
       ▼
Processamento concluído
       |
       ▼
Notificação enviada
       |
       ▼
SUCCESS


```

---



# examples/error-response.json


Representa um cenário de falha durante a validação.

## Cenário correspondente

```

Input
   |
   ▼
Validate File
   |
Arquivo válido?
   |
  Não
   |
   ▼
Fail State


```

---


# Estrutura da pasta examples

```

examples/
│
├── input.json
├── output.json
├── success-response.json
└── error-response.json


```

---

# Exemplos de execução

## Entrada


```

{
  "filename": "clientes.csv"
}

```


## Saída


```

{
  "status": "success",
  "records_processed": 1000
}


```

# Entrada inválida

```
{
  "filename": "clientes.exe"
}



```

# Saída


```

{
  "status": "failed",
  "error": "InvalidFile"
}


```





# Benefícios desta pasta

## Documentação
Facilita a compreensão do projeto.

## Testes
Permite simular execuções.

## Reprodutibilidade
Qualquer pessoa consegue entender rapidamente o fluxo.

## Portfólio
Aumenta a legibilidade do repositório

## Engenharia
Aproxima a estrutura do padrão utilizado em documentações corporativas e projetos open source.


---


