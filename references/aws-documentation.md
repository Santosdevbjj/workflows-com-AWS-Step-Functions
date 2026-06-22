# Documentações Oficiais AWS

Este documento centraliza as principais documentações utilizadas neste projeto.

---

# AWS Step Functions

Serviço de orquestração de workflows utilizado para coordenar aplicações distribuídas.

## Documentação

https://docs.aws.amazon.com/step-functions/

## Guia do Desenvolvedor

https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html

## Amazon States Language

https://states-language.net/spec.html

---

# AWS Lambda

Serviço serverless para execução de código sob demanda.

## Documentação

https://docs.aws.amazon.com/lambda/

## Python Runtime

https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html

## Best Practices

https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html

---

# Amazon SNS

Serviço de mensageria baseado no padrão Publish/Subscribe.

## Documentação

https://docs.aws.amazon.com/sns/

---

# Amazon SQS

Serviço de filas utilizado para comunicação assíncrona.

## Documentação

https://docs.aws.amazon.com/AWSSimpleQueueService/

---

# Amazon DynamoDB

Banco NoSQL totalmente gerenciado.

## Documentação

https://docs.aws.amazon.com/dynamodb/

---

# Amazon ECS

Serviço de orquestração de containers.

## Documentação

https://docs.aws.amazon.com/ecs/

---

# Amazon EKS

Serviço gerenciado de Kubernetes.

## Documentação

https://docs.aws.amazon.com/eks/

---

# Amazon EventBridge

Serviço de barramento de eventos.

## Documentação

https://docs.aws.amazon.com/eventbridge/

---

# Amazon CloudWatch

Serviço de monitoramento e observabilidade.

## Documentação

https://docs.aws.amazon.com/cloudwatch/

---

# AWS X-Ray

Serviço de rastreamento distribuído.

## Documentação

https://docs.aws.amazon.com/xray/

---

# AWS CloudTrail

Serviço de auditoria e rastreamento de chamadas de API.

## Documentação

https://docs.aws.amazon.com/awscloudtrail/

---

# AWS IAM

Gerenciamento de identidades e permissões.

## Documentação

https://docs.aws.amazon.com/iam/

---

# AWS Well-Architected Framework

Conjunto de boas práticas para construção de sistemas na nuvem.

## Documentação

https://docs.aws.amazon.com/wellarchitected/

### Pilares

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability

---

# AWS Architecture Center

Coleção de arquiteturas de referência e padrões.

## Documentação

https://aws.amazon.com/architecture/

---

# Boto3

SDK oficial da AWS para Python.

## Documentação

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

---

# AWS CDK

Framework para Infraestrutura como Código.

## Documentação

https://docs.aws.amazon.com/cdk/

---

# AWS CLI

Interface de linha de comando da AWS.

## Documentação

https://docs.aws.amazon.com/cli/

---

# Terraform AWS Provider

Integração Terraform com AWS.

## Documentação

https://registry.terraform.io/providers/hashicorp/aws/latest/docs

---

# Referências Utilizadas no Projeto

Os principais serviços utilizados neste laboratório foram:

- AWS Step Functions
- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Amazon CloudWatch

Esses serviços foram integrados para construir uma arquitetura serverless baseada em eventos, seguindo os princípios do AWS Well-Architected Framework.

---

# Conclusão

Toda a implementação deste projeto foi baseada nas recomendações e documentações oficiais da AWS, garantindo aderência às melhores práticas de:

- Escalabilidade;
- Resiliência;
- Segurança;
- Observabilidade;
- Automação;
- Arquiteturas orientadas a eventos.
