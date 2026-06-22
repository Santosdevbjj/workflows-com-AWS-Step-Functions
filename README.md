## Formação AWS Cloud Foundations

<img width="105" height="120" alt="1000127839" src="https://github.com/user-attachments/assets/19a72c1f-9f5d-4efc-93db-3fdae64064a0" />



---




✅ Storytelling técnico;

✅ AWS Well-Architected Framework;

✅ Foco em resolver problemas, e não apenas demonstrar ferramentas.


🚀 Explorando Workflows Automatizados com AWS Step Functions

«Orquestrando aplicações distribuídas e orientadas a eventos com AWS Step Functions, Lambda, SNS e SQS, aplicando conceitos de automação, resiliência e observabilidade em arquiteturas serverless.»

---

📌 Visão Geral

Aplicações modernas são compostas por diversos serviços distribuídos que precisam trabalhar em conjunto. Coordenar essas integrações apenas através de código pode aumentar a complexidade, dificultar o tratamento de falhas e comprometer a observabilidade.

Este projeto demonstra como utilizar o AWS Step Functions para orquestrar workflows automatizados, integrando serviços como:

- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Amazon CloudWatch

A solução implementa uma arquitetura orientada a eventos (Event-Driven Architecture), permitindo a execução coordenada de tarefas com baixo acoplamento, maior escalabilidade e melhor capacidade de monitoramento.

---

🎯 Objetivo do Projeto

Este projeto foi desenvolvido durante a formação AWS Cloud Foundations com o objetivo de:

- Consolidar conhecimentos sobre AWS Step Functions;
- Compreender a construção de máquinas de estados (State Machines);
- Implementar integrações com serviços serverless;
- Aplicar boas práticas do AWS Well-Architected Framework;
- Construir um material de consulta para futuras implementações.

Mais do que aprender uma ferramenta, o objetivo é compreender como resolver problemas reais de orquestração em sistemas distribuídos.

---

🏢 Problema de Negócio

Em aplicações modernas, diversas etapas precisam ser executadas em sequência:

1. Receber um arquivo;
2. Validar seu conteúdo;
3. Processar os dados;
4. Publicar eventos;
5. Notificar consumidores;
6. Monitorar a execução.

Quando essa coordenação é implementada diretamente no código da aplicação, surgem problemas como:

- Alto acoplamento;
- Complexidade excessiva;
- Baixa observabilidade;
- Dificuldade de recuperação em caso de falhas;
- Baixa escalabilidade.

O desafio é construir um fluxo resiliente e monitorável utilizando serviços gerenciados da AWS.

---

🌎 Contexto

Arquiteturas modernas são cada vez mais orientadas a eventos e compostas por microsserviços.

Nesse cenário, torna-se necessário:

- Coordenar tarefas;
- Implementar mecanismos de retry;
- Tratar exceções;
- Garantir observabilidade;
- Desacoplar componentes.

O AWS Step Functions atua como um orquestrador visual, permitindo que cada serviço mantenha responsabilidade única enquanto o fluxo é coordenado por uma máquina de estados.

---

📋 Premissas

Durante o desenvolvimento foram consideradas as seguintes premissas:

- O arquivo recebido deve possuir extensão válida;
- O processamento é executado por funções Lambda;
- Notificações são publicadas utilizando Amazon SNS;
- O desacoplamento entre produtores e consumidores é realizado através do Amazon SQS;
- Falhas são esperadas em sistemas distribuídos e devem ser tratadas;
- Logs e métricas fazem parte da arquitetura, e não são adicionados posteriormente.

---

🏗 Arquitetura da Solução

Input
  │
  ▼
AWS Step Functions
  │
  ▼
Validate File Lambda
  │
  ▼
Process Data Lambda
  │
  ▼
Notify Execution Lambda
  │
  ▼
Amazon SNS
  │
  ▼
Amazon SQS
  │
  ▼
Consumers
  │
  ▼
CloudWatch Logs

---

⚙ Estratégia da Solução

A estratégia utilizada foi dividida em etapas:

1. Entendimento do problema

Identificar como aplicações distribuídas coordenam tarefas e tratam falhas.

2. Construção da máquina de estados

Utilizando AWS Step Functions.

3. Implementação das funções Lambda

- validate_file
- process_data
- notify_execution

4. Integração com serviços de mensageria

- Amazon SNS
- Amazon SQS

5. Tratamento de erros

Aplicando:

- Retry Pattern;
- Catch Pattern;
- Fail State.

6. Observabilidade

Integração com:

- CloudWatch Logs;
- Metrics;
- Tracing.

---

⚡ Decisões Técnicas

Por que AWS Step Functions?

Porque permite:

- Criar workflows visualmente;
- Reduzir código de orquestração;
- Melhorar observabilidade;
- Implementar retries nativamente.

Alternativas consideradas

- Implementar toda a lógica em uma única Lambda;
- EventBridge;
- Código procedural tradicional.

Trade-offs

Foi escolhida uma arquitetura baseada em State Machines porque ela proporciona:

✔ Maior legibilidade;

✔ Melhor manutenção;

✔ Recuperação automática de falhas;

✔ Menor acoplamento entre componentes.

---

🛠 Tecnologias Utilizadas

Serviços AWS

- AWS Step Functions
- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Amazon CloudWatch

Linguagem

- Python 3.13

SDK

- boto3

Conceitos

- Serverless Computing
- Event-Driven Architecture
- Retry Pattern
- Fail Fast
- Observabilidade
- State Machines

---

📂 Estrutura do Repositório

workflows-com-AWS-Step-Functions/
│
├── docs/
├── workflows/
├── lambda/
├── examples/
├── notes/
├── references/
├── images/
│
├── .gitignore
├── LICENSE
└── README.mdNa próxima parte do README serão incluídas:

Como executar o projeto;

Estrutura das Lambdas;

Workflows implementados;

Integrações com SNS, SQS, ECS e EKS;

Observabilidade;

Insights e aprendizados;

Resultados;

Próximos passos;

Referências;

---



🚀 Como Executar o Projeto

Pré-requisitos

- Conta AWS
- AWS CLI configurado
- Python 3.13+
- Git
- Conhecimentos básicos sobre serviços AWS

---

Clonar o repositório

git clone https://github.com/Santosdevbjj/workflows-com-AWS-Step-Functions.git

cd workflows-com-AWS-Step-Functions

---

Criar ambiente virtual

python -m venv .venv

Linux/Mac:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

---

Instalar dependências

validate_file

cd lambda/validate_file

pip install -r requirements.txt

process_data

cd ../process_data

pip install -r requirements.txt

notify_execution

cd ../notify_execution

pip install -r requirements.txt

---

🔄 Workflows Implementados

1. Validação de Arquivos

Arquivo:

workflows/file-validation-workflow.json

Fluxo:

Input
 ↓
Validate File
 ↓
Success / Fail

Objetivo:

Garantir que apenas arquivos válidos avancem no pipeline.

---

2. Processamento de Dados

Arquivo:

workflows/lambda-execution-workflow.json

Fluxo:

Input
 ↓
Process Data
 ↓
Success

Objetivo:

Executar processamento desacoplado através do AWS Lambda.

---

3. Notificações com SNS

Arquivo:

workflows/sns-notification-workflow.json

Fluxo:

Lambda
 ↓
SNS Topic
 ↓
Subscribers

Objetivo:

Aplicar padrão Publish/Subscribe.

---

4. Processamento Assíncrono com SQS

Arquivo:

workflows/sqs-processing-workflow.json

Fluxo:

Producer
 ↓
SQS Queue
 ↓
Consumer

Objetivo:

Absorver picos de carga e aumentar a resiliência.

---

5. Workflow Serverless Completo

Arquivo:

workflows/complete-serverless-workflow.json

Fluxo:

Input
 ↓
Validate File
 ↓
Process Data
 ↓
Notify Execution
 ↓
SNS
 ↓
SQS
 ↓
Consumers

---

λ Funções Lambda

validate_file

Responsável por:

- Receber o nome do arquivo;
- Validar extensão;
- Retornar resultado.

---

process_data

Responsável por:

- Simular processamento;
- Produzir informações de saída;
- Registrar logs.

---

notify_execution

Responsável por:

- Publicar mensagens no SNS;
- Notificar consumidores;
- Desacoplar componentes.

---

📊 Observabilidade

A observabilidade foi tratada como parte da arquitetura.

Serviços estudados:

Amazon CloudWatch

- Logs
- Métricas
- Alarmes

AWS X-Ray

- Distributed Tracing
- Service Map

CloudTrail

- Auditoria
- Histórico de chamadas

---

🧠 Principais Insights

O Step Functions é um orquestrador

A lógica de negócio permanece nas Lambdas.

---

Sistemas distribuídos falham

Por isso foram estudados:

- Retry Pattern
- Catch Pattern
- Fail State

---

Event-Driven Architecture reduz acoplamento

SNS e SQS permitem construir sistemas mais resilientes.

---

Observabilidade é fundamental

Logs são parte da arquitetura.

Não um recurso opcional.

---

Simplicidade é uma vantagem

Fluxos menores:

- São mais legíveis;
- São mais fáceis de manter;
- Possuem menor risco operacional.

---

📈 Resultados Obtidos

Este laboratório permitiu compreender na prática:

Orquestração de workflows

Com AWS Step Functions.

Integração entre serviços

- Lambda
- SNS
- SQS

Arquiteturas orientadas a eventos

Com baixo acoplamento.

Resiliência

Tratamento de falhas e retries.

Observabilidade

Logs, métricas e rastreamento.

Serverless Computing

Redução da complexidade operacional.

Mais importante do que aprender serviços específicos, foi compreender como resolver problemas de coordenação em sistemas distribuídos.

---

📚 Aprendizados

Durante o desenvolvimento deste projeto, alguns pontos se destacaram.

Falhas são normais

Sistemas distribuídos devem ser construídos considerando falhas.

---

Serviços gerenciados reduzem carga operacional

Permitem que o foco permaneça no problema de negócio.

---

O Step Functions simplifica a coordenação

Separando claramente:

- Fluxo;
- Regras de negócio;
- Tratamento de erros.

---

Serverless não elimina arquitetura

Segurança, custos e observabilidade continuam sendo responsabilidades do arquiteto.

---

📁 Exemplos Disponíveis

Pasta:

examples/

Arquivos:

- input.json
- output.json
- success-response.json
- error-response.json

Esses exemplos facilitam:

- Testes;
- Reprodutibilidade;
- Documentação.

---

📖 Documentação Complementar

Pasta:

docs/

Contém:

- architecture.md
- step-functions-concepts.md
- lambda-integration.md
- validation-workflow.md
- sns-sqs-integration.md
- ecs-eks-integration.md
- monitoring-and-observability.md
- best-practices.md
- lessons-learned.md

---

📝 Anotações

Pasta:

notes/

Contém:

- lab-notes.md
- insights.md
- study-plan.md

---

🔗 Referências

Pasta:

references/

Contém:

- useful-links.md
- aws-documentation.md

Todo o projeto foi baseado em documentação oficial da AWS e nas recomendações do AWS Well-Architected Framework.Na terceira e última parte do README serão incluídos:

Próximos passos;

Roadmap do projeto;

AWS Well-Architected Framework;

Boas práticas implementadas;

Conclusão no estilo storytelling técnico;

Seção "Sobre o Autor";

Contribuições;

Licença;

Agradecimentos;




---
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



# .gitignore


Este .gitignore está preparado para futuras evoluções do projeto envolvendo:


AWS Lambda
AWS Step Functions
Terraform
AWS CDK
Docker
GitHub Actions
Testes automatizados
Python 3.13+
Serverless Framework
e segue um padrão semelhante ao utilizado em projetos profissionais e open source. 



---


