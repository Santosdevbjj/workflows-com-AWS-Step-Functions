# Insights Obtidos Durante os Estudos

## 1. O Step Functions é um orquestrador, não um executor

A lógica de negócio continua nas funções Lambda.

O Step Functions é responsável pela coordenação do fluxo.

---

## 2. State Machines tornam sistemas mais simples

Representar processos através de estados aumenta:

- Legibilidade;
- Manutenibilidade;
- Reutilização.

---

## 3. Falhas são normais em sistemas distribuídos

Por isso é fundamental implementar:

- Retry
- Catch
- Timeout

A resiliência deve ser planejada.

---

## 4. Event-Driven Architecture reduz acoplamento

SNS e SQS permitem construir sistemas desacoplados e escaláveis.

---

## 5. Observabilidade é indispensável

Logs e métricas são tão importantes quanto o código.

Ferramentas:

- CloudWatch
- X-Ray
- CloudTrail

---

## 6. Serverless não elimina arquitetura

Mesmo sem servidores, continuam existindo desafios relacionados a:

- Segurança;
- Custos;
- Escalabilidade;
- Monitoramento;
- Resiliência.

---

## 7. Step Functions favorece boas práticas

Permite aplicar:

- Single Responsibility Principle;
- Fail Fast;
- Retry Pattern;
- Event-Driven Architecture.

---

## 8. Simplicidade é uma vantagem

Workflows simples são:

- Mais confiáveis;
- Mais fáceis de manter;
- Mais fáceis de evoluir.

---

## 9. Serviços gerenciados reduzem carga operacional

O foco passa a ser:

Resolver problemas de negócio.

Não administrar infraestrutura.

---

## 10. Observabilidade deve ser projetada desde o início

Logs não devem ser adicionados posteriormente.

Eles fazem parte da arquitetura.

---

# Principal Aprendizado

O mercado não contrata quem conhece ferramentas.

O mercado contrata quem resolve problemas utilizando ferramentas.

Esse projeto mostrou que o AWS Step Functions é apenas um meio para construir sistemas distribuídos mais resilientes, escaláveis e observáveis.
