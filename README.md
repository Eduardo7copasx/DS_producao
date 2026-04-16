# Previsão de Vendas - Drogaria Rossmann

## Resultado

Qualquer pessoa conectada à um dispositivo com internet pode acessar a previsão de faturamento de seis semanas de qualquer loja Rossmann, em tempo real, através de um bot no Telegram.

![Bot no Telegram](img/bot_telegram.jpeg)

## Contexto de Negócio

A Rossmann é uma das maiores redes de drogaria da Europa, com cerca de 56.200 funcionários e mais de 4.000 lojas. O CFO pretende reformar as lojas e precisa da previsão de vendas das próximas seis semanas de cada uma delas para gerenciar o orçamento disponível. A previsão é baseada em dados históricos de vendas e permite ao CFO e demais executivos acessarem previsões precisas, de forma prática e em tempo real.

## Objetivo do Projeto

O objetivo principal é fornecer ao CFO previsões de vendas confiáveis para cada loja da rede Rossmann. Atualmente, as previsões são feitas por gerentes individuais, gerando variações e incertezas. Esta solução ajudará na definição de orçamentos mais precisos para investimentos e reformas nas lojas, além de ser acessível em dispositivos móveis, permitindo consultas de qualquer local.

## Planejamento

Aplicação do ciclo CRISP (Cross-Industry Process) focado em Ciência de Dados como uma técnica de metodologia ágil para entrega de um projeto end-to-end de maneira rápida, analisando os dados disponíveis para mapear todos os possíveis problemas de negócio nas diferentes etapas do projeto e entregar valor rápido para os stakeholders.

![Ciclo CRISP](img/CRISP.jpg)

## Tecnologias Utilizadas

- **Linguagem**: Pytho
- **Bibliotecas e Frameworks**: Pandas, NumPy, Flask, Inflection, Matplotlib, Seaborn, Scikit-learn, Boruta, XGBoost
- **Modelos e Técnicas**: Linear Regression, Random Forest, XGBoost
- **Metodologia**: Metodologia Ágil CRISP
- **Versionamento**: Git e GitHub
- **Plataformas de Deploy**: Render, Railway e Heroku

## Etapas do Projeto

1. **Entendimento do Negócio**: Quem é o dono do problema? Entendimento do contexto e da causa raiz. Entender o formato da solução (Granularidade, Tipo do problema como classificação, previsão ou clusterização e Formato da entrega).
2. **Coleta e Limpeza de Dados**: Obtenção de dados públicos reais no Kaggle, tratados e interpretados por estatística descritiva.
3. **Exploração de Dados**: Análise exploratória de dados para investigar padrões, entender fatores que influenciam o negócio e validar hipóteses.
4. **Modelagem de Dados**: Separação dos dados em treino, validação e teste, preparação dos dados (normalização, rescaling e encoding) e seleção de variáveis relevantes para o modelo.
5. **Algoritmo de Machine Learning**: Aplicação dos dados e variáveis aos algoritmos como Regressão Linear, Random Forest e XGBoost, com ajustes para minimizar erros de previsão.
6. **Avaliação de Resultados**: Avaliação com dados de teste e validação para garantir a qualidade e confiabilidade do modelo, calculando as métricas de performance e se o resultado faz sentido para o negócio.
7. **Implementação e Deployment**: Interface simples, acessível via dispositivos móveis.

## Principais Insights

### Competidores Próximos Aumentam as Vendas

Na análise entre as variáveis Vendas x Distância entre competidores, apesar da baixa correlação, farmácias Rossmann localizadas próximas umas das outras fazem com que as vendas aumentem de maneira geral.

![Competidores próximos aumentam as vendas](img/stores_with_closer_competitors_sell_more.png)

### As lojas vendem menos aos finais de semana

Com alta correlação, aos finais de semana, especialmente aos domingos, há uma queda considerável nas vendas de produtos das lojas.

![Lojas vendem menos aos finais de semana](img/stores_sell_less_on_weekends.png)

### As lojas vendem menos no segundo semestre do ano

De agosto a dezembro há uma queda em torno de 30% nas vendas em relação ao restante do ano.

![Lojas vendem menos no segundo semestre](img/sales_by_month.png)

## 🤖 Machine Learning

Foi utilizada a metodologia do cross-validation para achar a performance real do modelo, mitigando possíveis vieses temporais.

![Cross validation](img/cross_validation.jpg)

### Avaliação dos Modelos

Foram testados cinco modelos de machine learning, testando a linearidade dos dados até os mais complexos para explorar sua capacidade de ajuste:

- Average Model
- Linear Regression Model
- Linear Regression Lasso
- Random Forest Regresor
- XGBoost Regressor



### Modelo Final

Após a otimização dos parâmetros, através do Random Search, foi adotado o modelo XGBoost, pelo bom desempenho e também pelo seu custo computacional e de armazenamento menor.

Assim, o resultado final do modelo adotado foi:



## Performance de Negócio

Avaliando a soma das vendas de todas as lojas, temos uma variação de +- 0,3%. 
Para cada loja, o erro médio é de aproximadamente 10%.




## Conclusão

Este projeto oferece uma ferramenta poderosa de previsões de vendas para a Rossmann, permitindo ao CFO tomar decisões estratégicas com mais segurança e precisão. 
A solução do problema, de forma prática e acessível, permite que com o código da loja seja previsto as vendas correspondentes.

## Próximos Passos

Nos ciclos seguintes do CRISP pretendo implementar algumas melhorias como:

- Investigar erros nas lojas 292 e 909: analisar porque apresentam erros acima de 50% e encontrar soluções
- Novos modelos de Machine Learning: explorar outros algoritmos e identificar se algum deles oferece uma performance melhor
- Métodos de otimização de parâmetros: testar novas técnicas como Baesyan Optimization
- Automação de processos: aplicar a modelagem do scikit-learn no fluxo de trabalho para tornar o processo mais eficiente
