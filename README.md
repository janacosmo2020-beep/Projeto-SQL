#  Acervo: CRUD Básico com SQLite e Python

Este projeto é um exercício prático que demonstra os comandos fundamentais de SQL (CRUD - Create, Read, Update, Delete) utilizando a biblioteca nativa `sqlite3` do Python.

## Parte 1: Explicação do Código

### Descrição Resumida do que foi Implementado

O script `acervo_sqlite.py` implementa um sistema simples de gestão de acervo (livros e usuários), cobrindo:

1.  **Criação de Tabelas:** `Livros` e `Usuario`.
2.  **Manipulação de Dados:** Inserção de registros (`INSERT`), atualização de um campo (`UPDATE`), e exclusão de registros com base em uma condição (`DELETE`).
3.  **Consulta de Dados:** Seleção de registros filtrados (`SELECT WHERE`) e ordenados (`SELECT ORDER BY`).
4.  **Estrutura do Banco:** Uso de funções separadas para cada operação, garantindo modularidade e a utilização de consultas parametrizadas para evitar Injeção de SQL.

### Como Executar o Projeto

1.  **Clone o repositório:** (Após enviar para o GitHub)
    ```bash
    git clone https://github.com/Evelynsilva07/Projeto-SQL.git
    cd Acervo
    ```
2.  **Crie e ative o ambiente virtual (Windows):**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3.  **Instale as dependências** (não há externas, mas é a boa prática):
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o script:**
    ```bash
    python acervo.db
    ```

### Estrutura das Tabelas Criadas

#### Tabela `Livros`

| CAMPO | TIPO | RESTRIÇÕES | OBJETIVO |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PK, Auto-Increment | Identificador único do livro. |
| `titulo` | TEXT | NOT NULL, UNIQUE | Título do livro. |
| `autor` | TEXT | - | Autor do livro. |
| `ano` | INTEGER | - | Ano de publicação. |
| `genero` | TEXT | - | Gênero do livro. |
| `disponivel` | INTEGER | - | Status (1=Disponível, 0=Indisponível). |

#### Tabela `Usuario`

| CAMPO | TIPO | RESTRIÇÕES | OBJETIVO |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PK, Auto-Increment | Identificador único do usuário. |
| `nome` | TEXT | - | Nome completo do usuário. |
| `idade` | INTEGER | (Adicionada via ALTER TABLE) | Idade do usuário. |

## Parte 2: Questões Respondidas
## Fundamentos de Bancos de Dados

1-Por que os bancos de dados são essenciais em aplicações modernas?(Explique a importância dos bancos de dados em sistemas atuais)

R.:Os bancos de dados são essenciais em aplicações modernas por servirem como a memória central e organizada de qualquer sistema digital, permitindo o armazenamento, a recuperação e o gerenciamento eficiente e seguro de grandes volumes de informações.

* Organização e Centralização: Os BDs estruturam dados de diferentes naturezas (clientes, transações, produtos, etc.) em um local único e coerente, facilitando o acesso e a manipulação.

* Integridade e Consistência: Eles aplicam regras e validações para garantir que os dados sejam precisos e consistentes, evitando erros e redundâncias (duplicação de informações).

* Segurança: Oferecem recursos avançados de controle de acesso, criptografia e auditoria, protegendo as informações sensíveis contra acessos não autorizados ou perdas acidentais.

* Disponibilidade e Acesso Simultâneo: Permitem que múltiplos usuários e aplicações acessem e atualizem os dados de forma segura e simultânea, crucial para sistemas online e em tempo real (como e-commerce, redes sociais e sistemas bancários).

* Tomada de Decisão (Business Intelligence): São a base para a análise de dados (Analytics), transformando informações brutas em insights valiosos que otimizam processos, melhoram produtos e impulsionam a estratégia de negócios.

* Escalabilidade: Os bancos de dados modernos são projetados para lidar com o crescimento exponencial do volume de dados (Big Data), garantindo que a aplicação possa crescer e manter o desempenho.

Fonte: https://www.oracle.com/br/database/what-is-database/

2-Quais são as duas principais categorias de bancos de dados existentes? (Diferencie bancos de dados relacionais e não relacionais)

R.:As duas principais categorias de bancos de dados existentes são os Bancos de Dados Relacionais (SQL) e os Bancos de Dados Não Relacionais (NoSQL).

A diferença fundamental entre eles reside na forma como os dados são estruturados e nas prioridades de cada sistema (consistência vs. flexibilidade e escalabilidade).

* Os Bancos de Dados Relacionais são a forma mais tradicional e seguem o Modelo Relacional, no qual os dados são organizados em tabelas rígidas (linhas e colunas).

Estrutura: Esquema Rígido. Os dados devem se encaixar em um conjunto predefinido de tabelas e colunas, com relacionamentos claros entre as tabelas (usando chaves).

Linguagem: Utilizam a Structured Query Language (SQL) para definir, manipular e consultar os dados.

Prioridade (ACID): Focam na Integridade e Consistência dos Dados. Eles garantem as propriedades ACID (Atomicidade, Consistência, Isolamento, Durabilidade), cruciais para transações financeiras e sistemas onde a precisão é vital.

Melhor Uso: Sistemas de gerenciamento financeiro, sistemas de inventário e quaisquer aplicações que exigem alta consistência e integridade transacional.

Exemplos: MySQL, PostgreSQL, Oracle, Microsoft SQL Server.

* A categoria NoSQL (que significa "Not Only SQL" - Não Apenas SQL) abrange uma variedade de bancos de dados que não utilizam o modelo de tabelas tradicional, sendo mais flexíveis e otimizados para alto desempenho e escalabilidade horizontal.

Estrutura: Esquema Flexível. Permitem o armazenamento de dados não estruturados ou semiestruturados (como documentos JSON, imagens ou vídeos), sem a necessidade de um esquema rígido predefinido.

Linguagem: Cada tipo NoSQL pode ter sua própria linguagem de consulta. O termo NoSQL é um guarda-chuva para vários modelos (documento, chave-valor, coluna ampla e grafo).

Prioridade (BASE): Focam na Disponibilidade e Escalabilidade. Geralmente, seguem o modelo BASE (Basic Availability, Soft State, Eventual Consistency), priorizando a disponibilidade do sistema, mesmo que isso signifique que a consistência dos dados possa demorar um pouco mais.

Melhor Uso: Aplicações de Big Data, gerenciamento de conteúdo, redes sociais e sistemas que precisam lidar com grandes volumes de dados não estruturados e alta taxa de tráfego.

Exemplos: MongoDB (Documento), Redis (Chave-Valor), Cassandra (Coluna Ampla), Neo4j (Grafo).

Fonte: [Banco de Dados relacional ou Não-relacional | Saiba quando usar SQL ou NoSQL](https://www.youtube.com/watch?v=o8i2KZiIW4Y)

3-Em quais cenários é recomendado utilizar um banco de dados relacional? (Descreva situações ideais para SQL)

R.:É altamente recomendado utilizar um Banco de Dados Relacional (SQL) em cenários que exigem alta integridade transacional, estrutura de dados consistente e relacionamentos complexos e bem definidos entre as informações.

* 1. Transações Financeiras e Contabilidade (ACID)
Necessidade: Garantir que todas as transações (como transferências bancárias, compras ou atualizações de inventário) sejam completas e precisas, sem perdas ou inconsistências.

Porquê SQL: Bancos de dados relacionais são projetados para cumprir as propriedades ACID (Atomicidade, Consistência, Isolamento, Durabilidade), que são essenciais para manter a confiabilidade de dados críticos.

2. Sistemas de Planejamento de Recursos Empresariais (ERP)
Necessidade: Gerenciar módulos interconectados (vendas, estoque, RH, finanças) onde as informações devem estar rigidamente integradas e consistentes em toda a empresa.

Porquê SQL: A estrutura tabular e os relacionamentos de chaves estrangeiras (Foreign Keys) permitem modelar as complexas relações entre entidades de negócios (por exemplo, um pedido de compra está relacionado a um cliente, vários produtos e um pagamento).

3. Gerenciamento de Conteúdo com Regras Rígidas
Necessidade: Sistemas onde o esquema de dados é estável e as regras de relacionamento são complexas, como um sistema de gerenciamento de biblioteca (livro -> autor -> editora).

Porquê SQL: A aplicação de restrições e chaves primárias/estrangeiras garante que o conteúdo seja inserido e atualizado de forma padronizada e coerente, mantendo a integridade referencial.

4. Aplicações Legadas e Ferramentas Analíticas Maduras
Necessidade: Utilizar um ecossistema de ferramentas de Business Intelligence e Reporting que foram historicamente desenvolvidas para interagir com o modelo tabular do SQL.

Porquê SQL: A linguagem SQL é um padrão amplamente conhecido e suportado, facilitando a consulta, relatórios complexos (JOINs) e a integração com softwares legados ou middleware.

5. Cenários Onde a Consistência é Mais Crítica que a Velocidade de Escrita
Necessidade: Aplicações onde a precisão dos dados é absolutamente prioritária em relação à velocidade de escrita (inserção de dados), como em registros médicos ou registros de patentes.

Porquê SQL: O foco na Consistência do modelo ACID garante que, a qualquer momento, todos os usuários visualizem os dados mais corretos, mesmo que isso exija um pequeno custo em tempo de processamento.

Fonte: https://aws.amazon.com/pt/nosql/

4-De que forma os recursos de hardware (CPU, memória, disco) afetam a performance de um banco de dados? (Explique o impacto dos componentes do servidor)

R.: Os recursos de hardware (CPU, memória e disco) são os alicerces da performance de um banco de dados, pois determinam a velocidade com que o Sistema Gerenciador de Banco de Dados (SGBD) pode processar consultas, lidar com transações simultâneas e acessar os dados armazenados.

Qualquer gargalo em um desses componentes impactará diretamente a experiência do usuário, resultando em lentidão e timeouts.


* CPU Insuficiente:

Causa: Muitas consultas complexas ou alto volume de requisições concorrentes.

Efeito: O tempo que o SGBD leva para analisar e executar as consultas aumenta, resultando em alta latência de resposta para os aplicativos.

* Memória Insuficiente (A Pior Inimiga):

Causa: O Buffer Pool (área da RAM usada pelo BD) é muito pequeno para armazenar os dados quentes (mais acessados).

Efeito: O banco sofre de "troca de página" ou "paginação", onde ele precisa constantemente mover dados entre a RAM e o disco. Isso transforma uma operação rápida em memória em uma operação lenta de I/O de disco, estrangulando o desempenho.

* Disco Lento (Gargalo de I/O):

Causa: Utilização de discos rígidos (HDDs) ou SSDs com baixo IOPS para cargas de trabalho intensivas.

Efeito: O SGBD fica esperando a leitura ou gravação de dados, especialmente durante a inicialização, checkpoints (gravação do estado atual) ou transações que geram muitos logs. A performance se torna limitada pela velocidade do I/O, independente da velocidade da CPU.

Fonte: https://cloud.google.com/mysql/optimization?hl=pt-BR

5-O que significa escalabilidade no contexto de bancos de dados? (Defina escalabilidade vertical e horizontal)

R.: A escalabilidade em bancos de dados é a capacidade de um sistema de se adaptar e lidar com o aumento contínuo na carga de trabalho (mais dados, mais usuários e mais transações) sem que haja uma degradação significativa no seu desempenho ou qualidade do serviço.

Em essência, é a habilidade de crescer junto com a demanda da aplicação. Existem duas abordagens principais para alcançar essa expansão: Vertical e Horizontal.

* Escalabilidade Vertical (Scale-Up)
A escalabilidade vertical, ou "scale-up", consiste em aumentar a capacidade de um único servidor. É a forma mais simples e tradicional de expandir um banco de dados.

* Escalabilidade Horizontal (Scale-Out)
A escalabilidade horizontal, ou "scale-out", envolve adicionar mais servidores (nós) ao sistema e distribuir a carga de trabalho entre eles.

Fonte: https://www.youtube.com/watch?v=p2hVskMDT9U

6-Qual a relevância de organizar corretamente os dados em bancos relacionais? (Explique a importância da estruturação/normalização)

R.: A organização correta dos dados em bancos relacionais, um processo conhecido como Normalização, é de relevância fundamental. Ela garante que a estrutura do banco de dados seja eficiente, consistente e robusta, evitando problemas sérios que degradam a performance e a confiabilidade das informações.

*A Importância da Normalização (Estruturação Correta)
A normalização envolve aplicar um conjunto de regras (Formas Normais, como 1NF, 2NF e 3NF) para dividir uma tabela grande em tabelas menores e mais específicas, estabelecendo relacionamentos claros entre elas.

Os principais benefícios dessa estruturação correta são:

1.  Redução da Redundância de Dados (Duplicação)
Relevância: A redundância (dados repetidos em vários locais) desperdiça espaço de armazenamento e é a principal causa de inconsistência. Ao normalizar, cada fato é armazenado em um único local.

Exemplo: O nome de um cliente deve ser armazenado apenas na tabela Clientes, e não repetido em todas as linhas da tabela Pedidos dele.

2.  Melhoria na Integridade e Consistência dos Dados
Relevância: A integridade garante que os dados sejam precisos e confiáveis. Sem normalização, se a informação de um cliente (ex: seu endereço) precisar ser atualizada, seria necessário alterá-la em todos os lugares onde ela aparece. Se uma atualização for esquecida, o banco de dados se torna inconsistente.

Normalização: Garante que a atualização seja feita em um único lugar, refletindo-se automaticamente em todas as relações. Isso evita as chamadas anomalias de atualização, inserção e exclusão.

3.  Otimização da Performance de Consultas e Operações
Relevância: Tabelas menores, focadas em um único tipo de entidade, são mais rápidas de serem pesquisadas e manipuladas.

Benefício: Consultas se tornam mais eficientes (embora às vezes exijam mais JOINs), pois o Sistema Gerenciador de Banco de Dados (SGBD) precisa processar menos dados irrelevantes em cada tabela. Além disso, operações de escrita (INSERT, UPDATE, DELETE) são mais rápidas, pois afetam menos registros.

4.  Simplificação da Manutenção e Flexibilidade
Relevância: Um esquema bem estruturado e normalizado é mais fácil para os desenvolvedores entenderem e manterem ao longo do tempo.

Benefício: Se um novo requisito surgir (ex: adicionar um campo de telefone alternativo ao cliente), a mudança é aplicada em apenas uma tabela (Clientes), sem afetar inúmeras outras tabelas.

Fonte: https://www.datacamp.com/pt/tutorial/normalization-in-sql

7- Como escolher entre SQL e NoSQL para um novo projeto? (Critérios para decisão entre os modelos)

R.: A escolha entre SQL (Relacional) e NoSQL (Não Relacional) para um novo projeto deve ser baseada em uma análise dos requisitos específicos do sistema, priorizando as necessidades de estrutura de dados, integridade, escalabilidade e velocidade de desenvolvimento.

* Escolha SQL (Exemplos de Projetos)
Sistemas bancários e de pagamento.

Sistemas de gerenciamento de pedidos e inventário (ERP).

Sistemas de registro de clientes (CRM) onde a integridade dos dados é prioritária.

* Escolha NoSQL (Exemplos de Projetos)
Plataformas de analytics e logs (alto volume de escrita).

Redes sociais e sistemas de conteúdo em tempo real (alta disponibilidade).

Catálogos de produtos de e-commerce com atributos variáveis.

Aplicações que usam dados de sessão ou caching (Chave-Valor).

Fonte: https://learn.microsoft.com/pt-br/dotnet/architecture/modern-web-apps-azure/data-storage

## Comandos SQL

1-Qual é a finalidade do comando SELECT em SQL? (Descreva sua função e uso básico)

R.:A finalidade primordial do comando SELECT em SQL (Structured Query Language) é recuperar dados de um ou mais bancos de dados. Ele é o comando mais fundamental e frequentemente usado para realizar consultas (queries).

* Função e Uso Básico do Comando SELECT
O SELECT funciona como o ponto de partida para qualquer consulta, especificando quais dados você deseja ver.

Função Principal:
A função principal do SELECT é projetar os dados, ou seja, determinar quais colunas (atributos) de uma tabela devem ser exibidas no resultado da consulta.

Uso Básico:
A sintaxe básica do comando exige que você especifique as colunas que deseja selecionar, seguidas da palavra-chave FROM e do nome da tabela onde essas colunas estão armazenadas.

Uso do Asterisco (*):
Para selecionar todas as colunas de uma tabela, utiliza-se o asterisco (*):

Combinação com a Cláusula WHERE:
Na prática, o SELECT é quase sempre combinado com a cláusula WHERE para filtrar os resultados, restringindo quais linhas (registros) devem ser incluídas na saída da consulta.

Fonte: https://www.w3schools.com/sql/sql_select.asp

2-O que significam as siglas DML e DDL em bancos de dados? (Defina e
diferencie Data Manipulation Language e Data Definition Language)

R.: As siglas DML e DDL representam duas categorias principais de comandos SQL, classificando suas funções dentro do gerenciamento de um banco de dados relacional.

* DDL: Data Definition Language (Linguagem de Definição de Dados)
DDL refere-se aos comandos SQL usados para definir ou modificar a estrutura e o esquema do banco de dados e seus objetos (tabelas, índices, usuários, etc.). Esses comandos afetam a forma como os dados serão armazenados e organizados.

Finalidade: Gerenciar a estrutura do banco de dados.

Foco: O esquema (a definição e organização dos dados).

Comandos Chave:

CREATE: Cria novos objetos no banco de dados (ex: CREATE TABLE).

ALTER: Modifica a estrutura de um objeto existente (ex: ALTER TABLE ADD COLUMN).

DROP: Remove completamente um objeto e todos os seus dados (ex: DROP TABLE).

TRUNCATE: Remove todos os registros de uma tabela, mas mantém a estrutura intacta.

* DML: Data Manipulation Language (Linguagem de Manipulação de Dados)
DML refere-se aos comandos SQL usados para gerenciar e manipular os dados reais armazenados dentro dos objetos do esquema (as tabelas).

Finalidade: Gerenciar o conteúdo dos objetos do banco de dados.

Foco: Os dados (os registros e suas informações).

Comandos Chave:

SELECT: Recupera dados de uma ou mais tabelas.

INSERT: Adiciona novos registros (linhas) a uma tabela.

UPDATE: Modifica os dados existentes em uma ou mais linhas de uma tabela.

DELETE: Remove linhas (registros) específicas de uma tabela.

Fonte: https://www.ibm.com/docs/en/db2/11.5?topic=sql-data-manipulation-language-dml (Para DML) e https://www.ibm.com/docs/en/db2/11.5?topic=sql-data-definition-language-ddl (Para DDL)

3-Para que serve a cláusula WHERE em consultas SQL? (Explique seu
papel na filtragem de dados)

R.: A cláusula WHERE em consultas SQL serve para filtrar os registros (linhas) que serão retornados pela consulta. Seu papel é estabelecer uma condição lógica que cada linha do banco de dados deve satisfazer para ser incluída no resultado final.

* Papel da Cláusula WHERE
O WHERE é usado em conjunto com comandos DML, principalmente o SELECT, mas também pode ser aplicado em UPDATE e DELETE.

1. Filtragem de Registros (SELECT)
Quando usada com SELECT, a cláusula WHERE limita o número de linhas na saída da consulta. Em vez de retornar todos os dados de uma tabela, ela retorna apenas aqueles registros que atendem aos critérios especificados.

A cláusula WHERE em consultas SQL serve para filtrar os registros (linhas) que serão retornados pela consulta. Seu papel é estabelecer uma condição lógica que cada linha do banco de dados deve satisfazer para ser incluída no resultado final.

 Papel da Cláusula WHERE
O WHERE é usado em conjunto com comandos DML, principalmente o SELECT, mas também pode ser aplicado em UPDATE e DELETE.

1. Filtragem de Registros (SELECT)
Quando usada com SELECT, a cláusula WHERE limita o número de linhas na saída da consulta. Em vez de retornar todos os dados de uma tabela, ela retorna apenas aqueles registros que atendem aos critérios especificados.

2. Condicionamento de Alterações (UPDATE e DELETE)
Quando usada com UPDATE ou DELETE, a cláusula WHERE define quais registros terão seus valores modificados (UPDATE) ou serão removidos permanentemente (DELETE). É crucial usá-la com esses comandos para evitar modificar ou apagar todos os dados da tabela.

A cláusula WHERE em consultas SQL serve para filtrar os registros (linhas) que serão retornados pela consulta. Seu papel é estabelecer uma condição lógica que cada linha do banco de dados deve satisfazer para ser incluída no resultado final.

 Papel da Cláusula WHERE
O WHERE é usado em conjunto com comandos DML, principalmente o SELECT, mas também pode ser aplicado em UPDATE e DELETE.

1. Filtragem de Registros (SELECT)
Quando usada com SELECT, a cláusula WHERE limita o número de linhas na saída da consulta. Em vez de retornar todos os dados de uma tabela, ela retorna apenas aqueles registros que atendem aos critérios especificados.

Exemplo:

SQL

SELECT nome, preco
FROM Produtos
WHERE preco < 100.00; -- Filtra apenas produtos com preço inferior a 100
2. Condicionamento de Alterações (UPDATE e DELETE)
Quando usada com UPDATE ou DELETE, a cláusula WHERE define quais registros terão seus valores modificados (UPDATE) ou serão removidos permanentemente (DELETE). É crucial usá-la com esses comandos para evitar modificar ou apagar todos os dados da tabela.

3. Uso de Operadores Lógicos e de Comparação
A condição dentro do WHERE é construída usando operadores de comparação e operadores lógicos

Fonte: https://support.microsoft.com/en-us/office/access-sql-where-clause-753bbc13-debc-4b28-b527-42eb7885c862

4-Por que é fundamental estabelecer uma chave primária (PRIMARY KEY)
em tabelas? (Importância da chave primária)

R.: É fundamental estabelecer uma Chave Primária (PRIMARY KEY) em tabelas de bancos de dados relacionais porque ela garante a identificação única de cada registro e é essencial para a integridade dos dados e o relacionamento entre tabelas.

Fonte: https://learn.microsoft.com/pt-br/sql/relational-databases/tables/primary-and-foreign-key-constraints?view=sql-server-ver16

5-Como funciona o comando UPDATE e qual sua sintaxe básica? (Explique
a atualização de registros)

R.:O comando UPDATE em SQL é usado para modificar os dados existentes em um ou mais registros (linhas) de uma tabela. Ele permite alterar os valores de colunas específicas, afetando apenas as linhas que atendem a uma condição determinada.

* Funcionamento do Comando UPDATE
O UPDATE funciona em duas etapas principais:

Seleção (Cláusula WHERE): A cláusula WHERE identifica quais registros (linhas) devem ser afetados pela modificação. Este passo é crucial; sem a cláusula WHERE, o comando tentará atualizar todos os registros da tabela, o que geralmente é um erro grave.

Modificação (Cláusula SET): A cláusula SET especifica quais colunas terão seus valores alterados e qual será o novo valor atribuído.

Fonte: https://www.w3schools.com/sql/sql_update.asp

6-Qual a função do comando DELETE em SQL? (Diferença entre DELETE e
DROP)

R.:A função primária do comando DELETE em SQL é remover registros (linhas) específicos de uma tabela existente no banco de dados, sem alterar a estrutura da tabela em si.

* DELETE limpa o conteúdo da "caixa".

* DROP destrói a caixa inteira.

7-Como a cláusula ORDER BY organiza os resultados de uma consulta?(Ordenação ascendente e descendente)

R.: A cláusula ORDER BY em consultas SQL organiza os resultados de uma consulta, determinando a ordem na qual os registros (linhas) serão exibidos. Ela classifica os dados com base nos valores de uma ou mais colunas especificadas.

* Tipos de Ordenação

Você pode especificar a direção da ordenação usando duas palavras-chave:

1. Ascendente (ASC) 
Função: Ordena os dados do menor para o maior (do início para o fim).

Padrão: É a ordem padrão se nenhuma palavra-chave for especificada.

Exemplos:

Números: 1, 2, 3, 4...

Texto: A, B, C...

Datas: Data mais antiga para a data mais recente.

2. Descendente (DESC) ⬇
Função: Ordena os dados do maior para o menor (do fim para o início).

Exemplos:

Números: 10, 9, 8, 7...

Texto: Z, Y, X...

Datas: Data mais recente para a data mais antiga.


Fonte: https://www.datacamp.com/pt/tutorial/sql-order-by

7-Para que serve o comando LIMIT em consultas SQL? (Controle de
quantidade de registros retornados)

R.: O comando LIMIT em consultas SQL serve para controlar e restringir o número máximo de registros (linhas) que serão retornados pela consulta. Ele é essencial para otimização de performance, paginação de resultados e amostragem de dados.

* Função e Uso Básico do LIMIT
O LIMIT é usado no final de uma instrução SELECT (após as cláusulas FROM, WHERE, GROUP BY e ORDER BY) para definir um teto para o conjunto de resultados.

1. Restrição da Quantidade
A função mais básica é garantir que a consulta não retorne uma quantidade excessiva de dados.

2. Otimização e Top N
Quando combinado com ORDER BY, o LIMIT é usado para encontrar os "melhores" ou os "piores" registros (o chamado problema Top N). Isso evita que o SGBD tenha que processar e retornar milhões de linhas, melhorando drasticamente a performance.

3. Paginação de Resultados (Com OFFSET)
Em sistemas web e aplicativos, o LIMIT é usado junto com a cláusula OFFSET para implementar a paginação, ou seja, exibir os resultados em páginas discretas (Página 1, Página 2, etc.).

OFFSET: Especifica quantos registros devem ser pulados a partir do início do conjunto de resultados antes de aplicar o LIMIT.

Fonte: https://dev.mysql.com/doc/refman/8.0/en/select.html

##  Outros Conceitos

1-Por que é importante integrar o banco de dados com a camada de back
end da aplicação? (Relação entre BD e servidor)

R.: É fundamental integrar o banco de dados (BD) com a camada de back-end da aplicação porque o back-end (servidor) atua como a ponte de comunicação e a camada de lógica de negócios entre o usuário (front-end) e os dados persistentes no BD.

Essa integração é o que permite que uma aplicação moderna armazene, recupere, manipule e proteja as informações de forma eficiente.

* A Relação Essencial entre Back-end e Banco de Dados
A camada de back-end é responsável por gerenciar todo o ciclo de vida dos dados, cumprindo as seguintes funções críticas:

1.  Comunicação e Tradução
O back-end utiliza drivers e conectores para estabelecer e gerenciar a conexão com o banco de dados. Ele traduz as requisições complexas vindas do front-end (como um clique no botão "Comprar") em comandos SQL ou NoSQL que o BD pode entender e executar (SELECT, INSERT, UPDATE, DELETE).

2.  Imposição da Lógica de Negócios
O back-end é o local onde a lógica de negócios (as regras de como a empresa funciona) é aplicada antes que os dados cheguem ao BD ou sejam exibidos ao usuário.

Exemplo: Antes de registrar uma compra no BD, o back-end verifica se o estoque está disponível e calcula os impostos, garantindo que apenas dados válidos e processados sejam armazenados.

3.  Segurança e Autorização
É no back-end que ocorre a validação da identidade e das permissões do usuário.

Ele impede que o usuário final acesse o banco de dados diretamente, agindo como um portão de segurança.

Ele garante que usuários mal-intencionados não possam executar comandos SQL maliciosos ou ter acesso a dados confidenciais (como senhas), que devem ser criptografados no servidor antes de serem armazenados.

4.  Gerenciamento de Conexões e Performance
O servidor back-end é responsável por gerenciar de forma eficiente o pool de conexões com o BD, garantindo que múltiplas requisições de usuários simultâneos sejam tratadas sem sobrecarregar o banco de dados ou a aplicação. Isso é crucial para a escalabilidade e o desempenho do sistema.

Fonte: ttps://www.datacamp.com/pt_BR/blog/o-que-e-back-end-guia-completo

2-O que são views (visões) em bancos de dados e quais suas vantagens?
(Conceito e utilidade de views)

R.:Uma View (Visão) em SQL é uma tabela virtual baseada no conjunto de resultados de uma query (consulta) SELECT. Ela não armazena dados fisicamente como uma tabela comum; em vez disso, a View é uma estrutura lógica que armazena a definição da consulta.

Quando você consulta uma View, o banco de dados executa a consulta SELECT subjacente e apresenta o resultado como se fosse uma tabela real.

* Vantagens e Utilidade das Views
A criação e utilização de Views oferecem vantagens significativas para o gerenciamento, segurança e simplificação de um banco de dados:

1.  Segurança e Restrição de Acesso (Controle de Dados)
Views permitem implementar uma camada de segurança fina. Você pode conceder a usuários acesso a uma View que exibe apenas um subconjunto de colunas ou linhas de uma tabela sensível.

Exemplo: Um atendente pode ter acesso a uma View que mostra apenas o nome do cliente e o ID do pedido, mas não a colunas confidenciais da tabela original, como o salário ou o número do cartão de crédito.

2. упро Simplificação de Consultas Complexas
Views permitem encapsular lógica de negócios complexa ou consultas que envolvem múltiplos JOINs (junções de tabelas).

Utilidade: Em vez de reescrever uma query longa e complexa várias vezes, os desenvolvedores e usuários consultam a View com um SELECT * FROM nome_da_view, simplificando drasticamente o código e reduzindo erros.

3.  Consistência e Reutilização
Ao centralizar a lógica de um cálculo ou um conjunto de regras de filtragem na View, você garante que todos os usuários estejam consultando os mesmos dados e aplicando a mesma lógica.

Exemplo: Uma View pode ser criada para calcular o "Valor Total do Pedido" (Preço * Quantidade - Desconto), e essa definição será consistente em todas as partes da aplicação que a utilizarem.

4.  Camada de Abstração e Estabilidade
As Views podem fornecer uma interface estável para aplicações, mesmo que o esquema subjacente da tabela (o nome de uma coluna, por exemplo) precise mudar.

Utilidade: Se você renomear uma coluna na tabela base, você só precisará atualizar a definição da View; a aplicação que consulta a View não precisará de alterações.

Fonte: https://sae.unb.br/cae/conteudo/unbfga/lbd/banco2_visoes.html

3- Quais são as propriedades ACID e por que são cruciais para
transações? (Atomicidade, Consistência, Isolamento, Durabilidade)

R.: As propriedades ACID (Atomicidade, Consistência, Isolamento e Durabilidade) são um conjunto de regras essenciais que os sistemas de gerenciamento de banco de dados (SGBDs), especialmente os relacionais (SQL), devem seguir para garantir que as transações sejam processadas de maneira confiável e íntegra.

Elas são cruciais porque garantem que o banco de dados permaneça em um estado válido, mesmo diante de falhas, erros ou acessos simultâneos.

* As Propriedades ACID e Sua Importância
1. Atomicidade (A - Atomicity)
A transação é tratada como uma unidade única e indivisível de trabalho.

Significado: Ou a transação é completamente executada (commit), ou ela é totalmente desfeita (rollback), como se nunca tivesse acontecido.

Crucialidade: Evita estados parciais. Por exemplo, em uma transferência bancária, se o débito da Conta A ocorrer, mas o crédito na Conta B falhar (devido a uma queda de energia), a Atomicidade garante que o débito da Conta A também seja desfeito, mantendo a integridade do dinheiro.

2. Consistência (C - Consistency)
A transação deve levar o banco de dados de um estado válido para outro estado válido.

Significado: Garante que a transação respeite todas as regras predefinidas (restrições de integridade, chaves primárias, chaves estrangeiras, triggers).

Crucialidade: Impede que a transação crie dados inválidos. Por exemplo, se uma regra de negócios exige que a soma do estoque seja sempre positiva, uma transação que resultaria em estoque negativo será rejeitada, mantendo a Consistência.

3. Isolamento (I - Isolation)
As transações simultâneas devem ser executadas de forma independente e isolada umas das outras.

Significado: O resultado da execução de várias transações ao mesmo tempo deve ser o mesmo que se elas tivessem sido executadas sequencialmente (uma após a outra). Nenhuma transação pode "ver" os resultados parciais de outra transação em andamento.

Crucialidade: Evita problemas de concorrência (lost updates, leituras sujas, leituras não repetíveis) que poderiam levar a resultados incorretos em ambientes multiusuário.

4. Durabilidade (D - Durability)
Uma vez que a transação é confirmada (commitada), suas alterações são permanentes no sistema.

Significado: As alterações são registradas em um armazenamento não volátil (disco rígido ou SSD) e persistem mesmo que ocorra uma falha no sistema (como queda de energia ou falha de hardware) logo após o commit.

Crucialidade: Garante a confiança no sistema. O banco de dados deve ser capaz de recuperar o estado da transação por meio de logs de transação quando o sistema for reiniciado.

Fonte: https://learn.microsoft.com/pt-br/windows/win32/cossdk/acid-properties

4-O que estabelece o Princípio do Privilégio Mínimo em segurança de
bancos de dados? (Conceito de menor privilégio e suas aplicações)

R.: O Princípio do Privilégio Mínimo (Principle of Least Privilege - PoLP), em segurança de bancos de dados, estabelece que a um usuário, processo, ou aplicação deve ser concedido apenas o nível de acesso e as permissões estritamente necessárias para executar suas funções e nada mais.

É um conceito fundamental de segurança que visa minimizar a superfície de ataque e limitar os danos potenciais causados por falhas, erros ou atores mal-intencionados.


* Conceito e Aplicações
O PoLP não significa nenhum privilégio, mas sim o menor privilégio necessário.

1. Conceito Central
Controle Rigoroso: Define que todas as entidades (usuários, aplicações web, microserviços, stored procedures) devem operar com as permissões mínimas funcionais.

Foco: Se um usuário só precisa ler dados de uma tabela específica, ele não deve ter permissão para escrever, atualizar ou apagar dados dessa ou de qualquer outra tabela.

2. Aplicações Cruciais em Bancos de Dados
A aplicação do PoLP é vital para a segurança e integridade do SGBD:

Contas de Aplicação (Backend): O servidor back-end (onde reside a lógica de negócios) não deve se conectar ao banco de dados usando a conta de administrador (root ou sa). Deve usar uma conta dedicada que só tenha permissões SELECT, INSERT, UPDATE e DELETE nas tabelas que o aplicativo realmente usa.

Usuários Finais e Clientes: Um cliente em um site de e-commerce deve ter permissão apenas para ver seus próprios pedidos e informações pessoais. Ele não deve conseguir ver os dados de outros clientes ou acessar tabelas de inventário e preços de forma irrestrita.

Administração: Mesmo os administradores (DBAs) devem usar contas com privilégios elevados (SUPERUSER) apenas quando estritamente necessário para tarefas de manutenção. Para operações diárias e consultas, devem usar contas com privilégios reduzidos.

3. Impacto na Segurança
A implementação correta do PoLP mitiga os riscos de segurança de várias maneiras:

Limita o Dano: Se uma aplicação for comprometida (ex: ataque de injeção SQL), o invasor só poderá atuar dentro das permissões limitadas dessa conta. Ele não conseguirá apagar todo o banco de dados ou comprometer dados não relacionados.

Reduz Erros: Impede que um erro humano (acidentalmente executando um DELETE sem a cláusula WHERE) cause uma catástrofe sistêmica, pois a conta pode não ter permissão para apagar a tabela inteira.

Fonte: https://www.datacamp.com/pt/tutorial/principle-of-least-privilege