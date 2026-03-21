# Squad9
Porto Digital Unit Embarque - Squad 9

# O Problema

## Low-Code Reativo

Métodos de desenvolvimento de soluções Low-Code para Power Platform (Dataverse e o Power Apps) facilitam a criação, mas pulverizam a telemetria, levando a débitos técnicos e problemas estruturais que afetam a segurança, a performance e privacidade de aplicações e dados. 

## Low-Code Governado por IA (AIOps)

Criar uma camada de APIs agênticas que consolide esses silos é o caminho para transformar o o "Low-Code reativo" para o "Low-Code Governado por IA" (AIOps para Power Platform), convertendo os resultados de logs e relatórios do Solution Checker de uma ferramenta de "ponto de verificação" em um motor de "correção contínua".

Essa abordagem de **Micro-Agentes Especializados (Multi-SLM)** é o que há de mais moderno em engenharia de IA, assemelhando-se ao conceito de *Mixture of Agents* (MoA). Em vez de um modelo pesado tentando entender tudo, temos "especialistas" em contêineres leves, o que reduz drasticamente o custo de inferência e a latência.

Para um serviço centralizado que atende múltiplos ambientes (Dev, Test, Prod), a arquitetura funcionaria como um **Hub de Governança Agêntica**.

---
# Solução Proposta

## Arquitetura de Micro-Agentes Especializados

Imagine um barramento central (Orquestrador) que recebe o "payload" de um ambiente e o distribui para SLMs (**Phi-3.5-mini**) treinados especificamente em domínios distintos:

### 1. O Agente de Eficiência de Código (Power Fx & Performance)
* **Input:** Logs do App Insights + Código extraído do `.msapp`.
* **Foco:** Identificar problemas de delegação, N+1 queries no Dataverse e loops ineficientes no Power Automate.
* **SLM Strategy:** Fine-tuning em padrões de *High Performance Power Apps*. Ele ignora segurança e foca apenas em milissegundos e consumo de API.

### 2. O Agente de Postura de Segurança e Privacidade (Cyber-Guardian)
* **Input:** Metadados do Solution Checker + Configurações de DLP (Data Loss Prevention) + Definições de Tabelas no Dataverse.
* **Foco:** Identificar campos sensíveis (PII) sem máscara, conectores customizados sem autenticação robusta e compartilhamento excessivo de permissões.
* **SLM Strategy:** RAG focado em políticas internas de conformidade e ISO 27001.

### 3. O Agente de Débito Técnico e Manutenibilidade (Clean Code)
* **Input:** Estrutura da Solução + Nomenclatura de Variáveis + Documentação interna.
* **Foco:** Verificar se a solução segue o *benchmarking* público de legibilidade. Ele detecta "código spaghetti" e falta de tratamento de erros (`Try/Catch` no Power Automate).

---

## O Fluxo de Trabalho Centralizado (Multi-Tenant)

Para que isso funcione em múltiplos ambientes de forma agnóstica, o serviço centralizado operaria assim:

| Etapa | Ação do Sistema | Ferramenta |
| :--- | :--- | :--- |
| **Ingestão** | Coleta telemetria via **Data Exporter** do Power Platform para um Azure Log Analytics central. | Azure Monitor / Event Hub |
| **Triagem** | O Orquestrador identifica o tipo de telemetria e "chama" os SLMs necessários. | Azure Functions / Semantic Kernel |
| **Consenso** | Os SLMs geram diagnósticos independentes. Um modelo supervisor (ou regra lógica) consolida os riscos. | LLM de Orquestração (ou lógica C#) |
| **Ação** | O sistema gera um relatório de saúde ou dispara um **Auto-fix** via PAC CLI / GitHub Actions. | Azure DevOps Pipelines |

---

## Vantagens da Especialização de SLMs

* **Agnosticismo de Dados:** Você pode plugar um novo ambiente (ex: um novo Tenant de uma subsidiária) e o sistema apenas começa a rotear os logs para os agentes existentes.
* **Escalabilidade Horizontal:** Se o volume de logs de "Performance" aumentar no ambiente de Prod, você escala apenas o SLM de Performance, mantendo os outros com recursos mínimos.
* **Custo Granular:** SLMs de 3B ou 7B parâmetros podem rodar em GPUs mais simples (ou até CPUs otimizadas), tornando o serviço de governança viável financeiramente para empresas com centenas de soluções.

### Exemplo de Diagnóstico Consolidado:
> **Agente Perf:** "O fluxo 'Sync_Vendas' está atingindo limites de throttling (429)."
>
> **Agente Sec:** "O conector usado no fluxo tem acesso de 'Owner' desnecessário."
>
> **Conclusão Agêntica:** "Redesenhar o fluxo para processamento em batch (Perf) e aplicar o Princípio de Privilégio Mínimo na conexão (Sec)."

---
