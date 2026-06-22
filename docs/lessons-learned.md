# Lições Aprendidas com AWS Step Functions

# Introdução

Este projeto foi desenvolvido com o objetivo de consolidar conhecimentos sobre automação e orquestração de workflows utilizando o AWS Step Functions e outros serviços da AWS.

Mais do que executar um laboratório, a proposta foi compreender como arquiteturas modernas utilizam workflows distribuídos para construir sistemas escaláveis, resilientes e observáveis.

Ao longo da implementação, diversos conceitos e padrões arquiteturais foram explorados, permitindo transformar teoria em prática e aproximar a solução de cenários encontrados em ambientes corporativos.

---

# Objetivos do Projeto

Durante o desenvolvimento, os seguintes objetivos foram definidos:

- Compreender o funcionamento do AWS Step Functions;
- Aprender a modelar State Machines;
- Integrar serviços da AWS utilizando workflows;
- Aplicar conceitos de arquitetura orientada a eventos;
- Implementar tratamento de falhas;
- Desenvolver uma solução resiliente e observável;
- Consolidar boas práticas recomendadas pelo AWS Well-Architected Framework.

---

# Principais Aprendizados

## 1. O AWS Step Functions é mais do que um construtor visual

Inicialmente, o Step Functions pode parecer apenas uma ferramenta para desenhar fluxos.

Entretanto, durante os estudos ficou evidente que ele funciona como uma camada de orquestração responsável por coordenar aplicações distribuídas, centralizando:

- Fluxos de execução;
- Tratamento de erros;
- Regras de transição;
- Observabilidade;
- Recuperação automática.

Na prática, ele reduz significativamente a complexidade de sistemas compostos por múltiplos serviços.

---

## 2. State Machines tornam workflows mais claros

Modelar processos utilizando máquinas de estados permite visualizar a lógica da aplicação de forma explícita.

Antes do Step Functions, seria necessário implementar toda a lógica utilizando código.

Com State Machines, os fluxos ficam mais:

- Legíveis;
- Reutilizáveis;
- Manuteníveis;
- Auditáveis.

Esse modelo reduz a complexidade e facilita a identificação de gargalos.

---

## 3. Separar orquestração da lógica de negócio aumenta a manutenibilidade

Uma das principais lições aprendidas foi a importância de manter responsabilidades bem definidas.

### Step Functions

Responsável por:

- Coordenar o fluxo;
- Definir transições;
- Controlar exceções;
- Monitorar execuções.

### Lambda

Responsável por:

- Executar regras de negócio;
- Processar dados;
- Realizar validações.

Essa separação reduz o acoplamento e facilita futuras evoluções.

---

## 4. Falhas fazem parte dos sistemas distribuídos

Um dos conceitos mais importantes absorvidos durante o projeto foi que falhas não são exceções, mas sim eventos esperados em arquiteturas distribuídas.

Por isso, recursos como:

- Retry;
- Catch;
- Timeout;
- Fail State;

devem ser considerados desde o início.

Construir sistemas resilientes significa assumir que falhas acontecerão.

---

## 5. Event-Driven Architecture reduz acoplamento

A integração entre SNS e SQS mostrou como a comunicação baseada em eventos oferece benefícios importantes:

- Independência entre serviços;
- Escalabilidade;
- Processamento assíncrono;
- Maior disponibilidade;
- Resiliência.

Essa abordagem é amplamente utilizada em microsserviços modernos.

---

## 6. Serverless não significa ausência de arquitetura

Antes do projeto, era fácil associar Serverless apenas à ausência de servidores.

Durante a prática, ficou evidente que:

Serverless exige planejamento arquitetural.

Aspectos como:

- Observabilidade;
- Segurança;
- Tratamento de erros;
- Custos;
- Escalabilidade;

continuam sendo fundamentais.

---

## 7. Observabilidade é tão importante quanto a execução

Implementar workflows sem monitoramento reduz a capacidade de identificar problemas.

A integração com:

- CloudWatch;
- CloudTrail;
- AWS X-Ray;

mostrou a importância dos três pilares da observabilidade:

### Logs

Permitem entender o que aconteceu.

### Métricas

Permitem medir o comportamento.

### Traces

Permitem identificar onde ocorreu uma falha.

A observabilidade é indispensável em sistemas distribuídos.

---

## 8. O padrão Event-Driven é extremamente poderoso

A combinação:

```text
Step Functions
     ↓
Lambda
     ↓
SNS
     ↓
SQS
```

mostrou como aplicações podem ser construídas de forma desacoplada e altamente escalável.

Esse padrão é amplamente utilizado em:

- E-commerce;
- Streaming;
- IoT;
- Finanças;
- Data Engineering.

---

## 9. Containers e Serverless são complementares

Outro aprendizado importante foi compreender que Lambda, ECS e EKS não competem entre si.

Cada solução atende necessidades específicas.

### Lambda

Ideal para:

- Processamentos curtos;
- APIs;
- Serverless.

### ECS

Ideal para:

- Containers Docker;
- Processamentos intensivos.

### EKS

Ideal para:

- Kubernetes;
- Microsserviços complexos.

O Step Functions pode atuar como elemento de integração entre todas essas tecnologias.

---

## 10. AWS Step Functions favorece a adoção do princípio de responsabilidade única

Dividir os processos em estados independentes produz:

- Maior reutilização;
- Menor complexidade;
- Melhor testabilidade;
- Maior clareza.

Essa abordagem está alinhada aos princípios SOLID e às boas práticas de engenharia de software.

---

# Principais Desafios Encontrados

## Compreender State Machines

No início, pensar em fluxos baseados em estados exigiu uma mudança de mentalidade.

Com o tempo, tornou-se evidente que esse modelo facilita o entendimento da aplicação.

---

## Entender Retry e Catch

Perceber que falhas são normais e devem ser tratadas foi um dos aprendizados mais importantes.

---

## Compreender Arquiteturas Orientadas a Eventos

A comunicação assíncrona introduz novos desafios:

- Idempotência;
- Ordem das mensagens;
- Reprocessamento;
- Eventual consistency.

Esses conceitos são fundamentais em sistemas distribuídos.

---

# Conexão com o AWS Well-Architected Framework

Durante a implementação, diversos princípios foram aplicados.

## Excelência Operacional

- Automação;
- Observabilidade;
- Monitoramento.

---

## Segurança

- IAM Roles;
- Menor privilégio;
- Serviços gerenciados.

---

## Confiabilidade

- Retry;
- Catch;
- SQS;
- Alta disponibilidade.

---

## Eficiência de Performance

- Serverless;
- Escalabilidade automática.

---

## Otimização de Custos

- Pagamento sob demanda;
- Serviços gerenciados.

---

## Sustentabilidade

- Uso eficiente de recursos;
- Escalabilidade sob demanda.

---

# Insights Obtidos

## Workflows são código

Embora sejam representados visualmente, workflows fazem parte da arquitetura da aplicação e devem ser tratados com o mesmo rigor aplicado ao desenvolvimento de software.

---

## Observabilidade deve ser planejada desde o início

Logs e métricas não devem ser adicionados posteriormente.

Eles fazem parte da solução.

---

## Simplicidade é uma vantagem

Soluções simples tendem a ser:

- Mais fáceis de manter;
- Mais confiáveis;
- Mais escaláveis.

---

## Serviços gerenciados reduzem complexidade operacional

Ao utilizar Step Functions, Lambda, SNS e SQS, a equipe pode concentrar esforços no negócio em vez da infraestrutura.

---

# Próximos Passos

Com base nos conhecimentos adquiridos, as próximas evoluções planejadas incluem:

- EventBridge;
- Distributed Map;
- Parallel State;
- DynamoDB;
- AWS Batch;
- AWS Glue;
- SageMaker;
- AWS CDK;
- Terraform;
- GitHub Actions;
- CI/CD;
- AWS X-Ray;
- Microsserviços orientados a eventos.

---

# Conclusão

Este projeto permitiu consolidar conhecimentos sobre orquestração de workflows, integração entre serviços e arquitetura distribuída na AWS.

Mais do que aprender um serviço específico, foi possível compreender princípios fundamentais de engenharia de software e arquitetura em nuvem, como:

- Resiliência;
- Observabilidade;
- Escalabilidade;
- Baixo acoplamento;
- Automação;
- Event-Driven Architecture;
- Serverless Computing.

Esses conceitos constituem a base das arquiteturas modernas utilizadas por organizações que operam sistemas em larga escala.

O AWS Step Functions mostrou-se uma ferramenta poderosa para simplificar a coordenação de processos distribuídos, permitindo construir aplicações mais confiáveis, flexíveis e alinhadas às melhores práticas recomendadas pelo AWS Well-Architected Framework.
