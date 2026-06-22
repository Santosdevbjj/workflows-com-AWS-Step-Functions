# 🚀 Workflows Automatizados com AWS Step Functions

<img width="105" height="120" alt="AWS Step Functions" src="https://github.com/user-attachments/assets/19a72c1f-9f5d-4efc-93db-3fdae64064a0" />

> *Orquestrando sistemas distribuídos com AWS Step Functions, Lambda, SNS e SQS — aplicando resiliência, observabilidade e Event-Driven Architecture em arquiteturas serverless de nível corporativo.*

[![Portfólio](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)

---

## 1. Problema de Negócio

Aplicações modernas são compostas por múltiplos serviços distribuídos que precisam trabalhar em conjunto — validar arquivos, processar dados, publicar eventos, notificar consumidores e registrar resultados. Quando essa coordenação é implementada diretamente no código da aplicação, surgem efeitos colaterais críticos: alto acoplamento entre componentes, tratamento de falhas manual e disperso, baixa observabilidade sobre o que acontece entre os serviços, e escalabilidade comprometida.

O desafio central deste projeto é: **como orquestrar um pipeline de processamento de arquivos de forma resiliente, observável e desacoplada, sem aumentar a complexidade do código de negócio?**

---

## 2. Contexto

Em ambientes financeiros e corporativos, pipelines de ingestão e processamento de arquivos são infraestrutura crítica. Uma falha em qualquer etapa — validação, processamento ou notificação — pode gerar inconsistências nos dados, reprocessamentos manuais e perda de rastreabilidade.

A operação envolve variáveis que impactam diretamente a confiabilidade do sistema:

- Natureza assíncrona dos serviços distribuídos
- Necessidade de retry automático em falhas transitórias
- Múltiplos consumidores com velocidades de processamento distintas
- Obrigatoriedade de auditoria e rastreamento de todas as execuções

O AWS Step Functions, combinado com Lambda, SNS, SQS e DynamoDB, forma a base dessa arquitetura — permitindo que cada serviço mantenha responsabilidade única enquanto o fluxo é coordenado por uma State Machine visual e auditável.

---

## 3. Premissas da Análise

Para o desenvolvimento foram adotadas as seguintes premissas:

- O arquivo recebido (`filename`) é o gatilho inicial do workflow
- Extensões válidas para processamento: `.csv`, `.json`, `.txt`
- Falhas são eventos esperados em sistemas distribuídos e devem ser tratadas por padrão, não como exceção
- Observabilidade (logs, métricas, traces) faz parte da arquitetura desde o início — não é adicionada posteriormente
- O período de estudo representa a Fase 1 do roadmap; integrações com ECS, EKS e EventBridge estão previstas para fases subsequentes
- Credenciais AWS nunca são hardcoded — variáveis de ambiente são o padrão adotado (`TOPIC_ARN`)

---

## 4. Estratégia da Solução

A estratégia seguiu uma abordagem estruturada em seis etapas:

**Etapa 1 — Modelagem do problema de negócio**
Identificar quais etapas do pipeline precisam ser coordenadas, onde ocorrem falhas e qual o impacto de cada ponto de falha.

**Etapa 2 — Construção da State Machine**
Modelar o fluxo completo no AWS Step Functions, definindo estados (Task, Choice, Succeed, Fail), transições e regras de Retry/Catch via Amazon States Language (ASL/JSON).

**Etapa 3 — Implementação das funções Lambda**
Três funções com responsabilidade única, escritas em Python 3.13 com boto3:
- `validate_file` — verifica extensão e integridade
- `process_data` — executa o processamento e registra timestamp e volume
- `notify_execution` — publica evento no SNS via variável de ambiente `TOPIC_ARN`

**Etapa 4 — Integração com mensageria assíncrona**
SNS para distribuição de eventos (Pub/Sub) e SQS para absorção de picos de carga e desacoplamento entre produtores e consumidores.

**Etapa 5 — Tratamento de falhas por design**
Retry com backoff exponencial, Catch para desvio controlado ao estado de falha, e Fail State para encerramento auditável.

**Etapa 6 — Observabilidade**
CloudWatch Logs integrado nativamente nas Lambdas com logging estruturado, métricas de execução do Step Functions e CloudTrail para auditoria de chamadas de API.

---

## 5. Arquitetura da Solução

```
Amazon S3 (trigger)
        │
        ▼
AWS Step Functions — State Machine
        │
        ├─► validate_file (Lambda)
        │         │
        │    válido? ──► Fail State (extensão inválida)
        │         │
        ├─► process_data (Lambda)
        │         │
        ├─► notify_execution (Lambda)
        │         │
        ├─► Amazon SNS ──► Subscribers (SQS, Lambda, Email)
        │         │
        ├─► Amazon SQS ──► Consumer Services
        │         │
        ├─► Amazon DynamoDB (persistência de metadados)
        │
        └─► Amazon CloudWatch (logs, métricas, alarmes)
```

**Workflows implementados:**

| Arquivo | Responsabilidade |
|---|---|
| `file-validation-workflow.json` | Validação isolada com Choice State |
| `lambda-execution-workflow.json` | Orquestração sequencial com tratamento de erros |
| `sns-notification-workflow.json` | Publicação de eventos via integração nativa SNS |
| `sqs-processing-workflow.json` | Envio assíncrono para fila SQS |
| `complete-serverless-workflow.json` | Pipeline completo: Validate → Process → SNS → SQS → DynamoDB |

---

## 6. Decisões Técnicas e Trade-offs

**AWS Step Functions como orquestrador central**
Alternativa considerada: implementar toda a lógica de coordenação em uma única Lambda "master" que chamaria as demais em sequência. Racional: o Step Functions externaliza o fluxo para uma State Machine auditável, com retry nativo, histórico de execução no console e observabilidade sem código adicional. Trade-off aceito: custo por transição de estado em Standard Workflows — justificado pelo ganho em rastreabilidade e pela redução de código de orquestração nas Lambdas.

**Três Lambdas com responsabilidade única em vez de uma Lambda monolítica**
Alternativa considerada: consolidar validate + process + notify em uma única função para reduzir latência entre invocações. Racional: responsabilidade única permite testar, versionar e escalar cada função de forma independente, além de facilitar reutilização por outros workflows (EventBridge, API Gateway). Trade-off aceito: latência adicional de ~10-50ms por invocação — irrelevante para o cenário de processamento assíncrono de arquivos.

**SNS → SQS (Fanout Pattern) em vez de integração direta Lambda → consumidores**
Alternativa considerada: a Lambda `notify_execution` chamar diretamente cada consumidor. Racional: o fanout via SNS→SQS desacopla produtores de consumidores, permite múltiplos subscribers independentes e garante que uma falha em um consumidor não afete os demais. Trade-off aceito: eventual consistency — as mensagens não são processadas de forma estritamente síncrona, o que é aceitável para notificações de eventos de arquivo.

**Standard Workflow em vez de Express Workflow**
Alternativa considerada: Express Workflow para menor custo por execução. Racional: Standard Workflow mantém histórico completo de execução no console por 90 dias, essencial para auditoria e diagnóstico em ambientes corporativos. Trade-off aceito: custo ligeiramente superior — justificado pelo ganho em rastreabilidade.

---

## 7. Tecnologias Utilizadas

**Serviços AWS**
- AWS Step Functions (orquestração, State Machine, ASL)
- AWS Lambda + Python 3.13 + boto3 (execução serverless)
- Amazon SNS (Pub/Sub, distribuição de eventos)
- Amazon SQS (fila assíncrona, absorção de picos)
- Amazon DynamoDB (persistência de metadados)
- Amazon CloudWatch (logs, métricas, alarmes)
- AWS CloudTrail (auditoria de API)
- AWS X-Ray (distributed tracing — roadmap Fase 2)

**Conceitos e Padrões**
- Event-Driven Architecture
- State Machine Pattern
- Publish/Subscribe Pattern
- Queue-Based Load Leveling
- Retry + Backoff Exponencial
- Fail Fast
- Idempotency Pattern
- Serverless Computing
- AWS Well-Architected Framework (6 pilares)

---

## 8. Como Executar o Projeto

**Pré-requisitos**
- Conta AWS ativa com permissões para Step Functions, Lambda, SNS, SQS e DynamoDB
- AWS CLI configurado (`aws configure`)
- Python 3.13+
- Git

**Clonar o repositório**
```bash
git clone https://github.com/Santosdevbjj/workflows-com-AWS-Step-Functions.git
cd workflows-com-AWS-Step-Functions
```

**Criar ambiente virtual**
```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows
```

**Instalar dependências**
```bash
cd lambda/validate_file && pip install -r requirements.txt
cd ../process_data && pip install -r requirements.txt
cd ../notify_execution && pip install -r requirements.txt
```

**Configurar variável de ambiente (notify_execution)**
```bash
export TOPIC_ARN="arn:aws:sns:us-east-1:123456789012:file-processing-topic"
```

**Testar localmente com exemplo de entrada**
```bash
# Entrada válida
cat examples/input.json
# { "filename": "clientes.csv" }

# Saída esperada (workflow completo)
cat examples/output.json
```

**Deploy no AWS**
1. Criar as três funções Lambda e fazer upload dos arquivos em `lambda/`
2. Configurar variável de ambiente `TOPIC_ARN` na Lambda `notify_execution`
3. Criar a State Machine no Step Functions com o conteúdo de `workflows/complete-serverless-workflow.json`
4. Executar com o input: `{ "filename": "clientes.csv" }`

---

## 9. Exemplos de Execução

**Entrada**
```json
{ "filename": "clientes.csv" }
```

**Saída — sucesso**
```json
{
  "filename": "clientes.csv",
  "validation": { "valid": true, "message": "Arquivo válido." },
  "processing": { "status": "processed", "records_processed": 1000, "processed_at": "2026-06-22T15:30:10.123456" },
  "notification": { "status": "notification_sent", "message_id": "7caa6b5f-..." }
}
```

**Saída — arquivo inválido**
```json
{ "status": "failed", "error": "InvalidFile", "message": "Extensão de arquivo não suportada.", "filename": "clientes.exe" }
```

---

## 10. Insights da Análise

**O Step Functions não substitui arquitetura — ele a torna visível.**
A lógica de negócio permanece nas Lambdas. O que o Step Functions faz é tornar explícito o fluxo, os pontos de falha e as transições — o que em código procedural ficaria oculto em try/catch aninhados e chamadas diretas entre serviços.

**Falhas são o estado normal em sistemas distribuídos.**
O Retry com backoff exponencial (`IntervalSeconds: 2`, `BackoffRate: 2`, `MaxAttempts: 3`) trata falhas transitórias automaticamente. O Catch desvia para um estado de falha controlado. O Fail State encerra com `Error` e `Cause` auditáveis. Esses três mecanismos juntos eliminam a necessidade de código de resiliência nas próprias Lambdas.

**Serverless não significa ausência de responsabilidades arquiteturais.**
Segurança (IAM roles com menor privilégio, TOPIC_ARN via variável de ambiente, sem hardcoding de credenciais), custos (Standard vs Express Workflow), observabilidade e escalabilidade continuam sendo decisões do arquiteto — o provedor gerencia a infraestrutura, não as decisões.

**O padrão SNS → SQS (Fanout) é o padrão correto para múltiplos consumidores.**
Chamar consumidores diretamente da Lambda cria acoplamento temporal: se um consumidor está indisponível, a Lambda falha. Com SNS → SQS, cada consumidor tem sua própria fila, processa no seu ritmo e uma falha em um não afeta os demais.

---

## 11. Resultados Obtidos

Ao final do projeto foi possível:

- Construir um pipeline serverless completo com 5 workflows distintos e um workflow consolidado cobrindo todo o fluxo
- Implementar tratamento de falhas por design em todos os estados críticos (Retry + Catch + Fail State)
- Separar orquestração (Step Functions) de lógica de negócio (Lambda) — reduzindo o código de cada Lambda a uma única responsabilidade
- Aplicar os 6 pilares do AWS Well-Architected Framework de forma rastreável
- Criar documentação técnica cobrindo arquitetura, integração de cada serviço, boas práticas, lições aprendidas e roadmap de evolução
- Estabelecer uma base replicável para pipelines de dados, ETL e workflows empresariais em ambientes AWS

---

## 12. Próximos Passos

**Fase 2 — Observabilidade avançada**
- [ ] AWS X-Ray para distributed tracing e service map
- [ ] Dashboards CloudWatch com métricas de `ExecutionsFailed`, `ExecutionTime` e throughput de SQS
- [ ] Dead Letter Queue (DLQ) para mensagens com falha persistente

**Fase 3 — Infraestrutura como Código**
- [ ] AWS CDK para deploy reprodutível de toda a stack
- [ ] Terraform como alternativa multi-cloud
- [ ] GitHub Actions para CI/CD com testes automatizados e deploy contínuo

**Fase 4 — Padrões avançados de Step Functions**
- [ ] Parallel State para execuções simultâneas
- [ ] Map State e Distributed Map para processamento em lote de múltiplos arquivos
- [ ] Saga Pattern para transações distribuídas com compensação
- [ ] Callback Pattern para aprovações humanas no fluxo

**Fase 5 — Containers e microsserviços**
- [ ] Amazon ECS Fargate para workloads que excedem os limites do Lambda
- [ ] Amazon EKS para microsserviços complexos baseados em Kubernetes
- [ ] Amazon EventBridge como barramento de eventos entre domínios

---

## 13. Estrutura do Repositório

```
workflows-com-AWS-Step-Functions/
│
├── docs/
│   ├── architecture.md              # Arquitetura detalhada da solução
│   ├── step-functions-concepts.md   # Conceitos: State Machine, ASL, tipos de estado
│   ├── lambda-integration.md        # Integração Step Functions ↔ Lambda
│   ├── validation-workflow.md       # Workflow de validação com Choice State
│   ├── sns-sqs-integration.md       # Fanout Pattern: SNS → SQS
│   ├── ecs-eks-integration.md       # Containers como alternativa ao Lambda
│   ├── monitoring-and-observability.md  # CloudWatch, X-Ray, CloudTrail
│   ├── best-practices.md            # Boas práticas e checklist de produção
│   └── lessons-learned.md           # Lições aprendidas e insights
│
├── workflows/
│   ├── file-validation-workflow.json
│   ├── lambda-execution-workflow.json
│   ├── sns-notification-workflow.json
│   ├── sqs-processing-workflow.json
│   └── complete-serverless-workflow.json
│
├── lambda/
│   ├── validate_file/
│   │   ├── lambda_function.py
│   │   └── requirements.txt
│   ├── process_data/
│   │   ├── lambda_function.py
│   │   └── requirements.txt
│   └── notify_execution/
│       ├── lambda_function.py
│       └── requirements.txt
│
├── examples/
│   ├── input.json
│   ├── output.json
│   ├── success-response.json
│   └── error-response.json
│
├── notes/
│   ├── lab-notes.md
│   ├── insights.md
│   └── study-plan.md
│
├── references/
│   ├── aws-documentation.md
│   └── useful-links.md
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 14. AWS Well-Architected Framework — Aplicação no Projeto

| Pilar | O que foi aplicado |
|---|---|
| **Excelência Operacional** | Logging estruturado em todas as Lambdas, histórico completo de execução no Step Functions, automação de retry |
| **Segurança** | IAM roles com menor privilégio, TOPIC_ARN via variável de ambiente, sem credenciais hardcoded, .gitignore cobrindo `.aws/`, `*.pem`, `secrets/` |
| **Confiabilidade** | Retry + Catch + Fail State em todos os estados críticos, SQS como buffer de mensagens, DLQ prevista no roadmap |
| **Eficiência de Performance** | Serverless (Lambda + Step Functions), escalabilidade automática, SNS → SQS para absorção de picos |
| **Otimização de Custos** | Pay-as-you-go, sem servidores dedicados, Standard Workflow escolhido com trade-off consciente sobre Express |
| **Sustentabilidade** | Serviços gerenciados reduzem recursos ociosos, escalabilidade sob demanda evita superprovisionamento |

---

## 15. Referências

- [AWS Step Functions — Documentação oficial](https://docs.aws.amazon.com/step-functions/)
- [Amazon States Language — Especificação](https://states-language.net/spec.html)
- [AWS Lambda — Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/)
- [Serverless Land — Padrões e exemplos](https://serverlessland.com/)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [Boto3 — SDK Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

## 16. Contribuições

Contribuições são bem-vindas. Para contribuir:

```bash
git checkout -b feature/minha-feature
git commit -m "feat: descrição da melhoria"
git push origin feature/minha-feature
```

Abra um Pull Request descrevendo o problema que a contribuição resolve.

---

## 17. Autor

**Sérgio Luiz dos Santos** — Systems Analyst | Cloud & AI Solutions Specialist

15+ anos em sistemas de missão crítica (Banco Bradesco S.A.) · DIO Campus Expert

[![Portfólio](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)
[![GitHub](https://img.shields.io/badge/GitHub-Santosdevbjj-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Santosdevbjj)



---

📜 Licença MIT — consulte o arquivo [LICENSE](LICENSE).

⭐ Se este projeto foi útil, considere deixar uma estrela no repositório.
