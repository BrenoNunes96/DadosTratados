🔍 Motor de Busca Semântico: Notícias Econômicas (Desafio Técnico FGV IBRE)
Este repositório contém a solução para o desafio técnico de Ciência de Dados, cujo objetivo é construir um mini motor de busca semântico aplicado a um corpus de notícias econômicas. O projeto foca em extração, limpeza de dados textuais não estruturados e recuperação de informações relevantes utilizando processamento de linguagem natural (NLP).

🚀 Visão Geral do Pipeline
O projeto foi dividido em dois scripts principais que cobrem as três etapas do desafio:

etapa1.py (Limpeza e Tratamento): Recebe o arquivo noticias_brutas.json e gera arquivos .txt limpos.

etapa2.py (Geração de Embeddings e Busca): Transforma os textos em vetores, processa a query do usuário e retorna as 3 notícias mais relevantes baseadas em similaridade semântica.

🧠 Decisões Técnicas e Arquitetura
Etapa 1: Limpeza e Tratamento de Texto (etapa1.py)
Para lidar com as "sujeiras" do formato HTML e caracteres especiais embutidos no JSON bruto:

BeautifulSoup: Utilizado para fazer o parsing do HTML, removendo facilmente tags e extraindo apenas o conteúdo textual limpo.

Expressões Regulares (re): Aplicado o padrão re.sub(r"\s+", " ", ...) para normalizar espaços e quebras de linha excessivas, garantindo um texto coeso.

Armazenamento: Cada notícia foi salva em um arquivo de texto individual (.txt) nomeado com seu respectivo ID dentro da pasta dados/, facilitando a leitura iterativa na próxima etapa.

Etapas 2 e 3: Embeddings e Busca Semântica (etapa2.py)
A lógica de busca foi construída para comparar o que o usuário pesquisa com a base de dados de forma semântica (pelo significado, não apenas por palavras-chave):

Modelo Escolhido (all-MiniLM-L6-v2): Utilizado através da biblioteca sentence-transformers. A escolha deste modelo se dá por ser extremamente leve, rápido de rodar localmente e altamente eficiente para tarefas de similaridade semântica em sentenças e pequenos parágrafos.

Processo de Busca:

Os textos limpos são carregados e convertidos em representações vetoriais (embeddings).

A pesquisa do usuário (ex: "mudanças na taxa de juros") também é transformada em embedding.

A comparação é feita utilizando o método de similaridade do próprio modelo.

Através da função torch.topk, o script identifica os 3 valores mais altos no tensor de similaridade.

Os índices desses 3 maiores tensores são extraídos e convertidos para uma lista (lista_de_indices).

Por fim, um laço for mapeia esses índices de volta para o array original de textos (texts), imprimindo na tela a pontuação de relevância e o conteúdo das notícias mais compatíveis com a busca.

⚙️ Como Executar o Projeto
Certifique-se de ter o Python instalado. É recomendado o uso de um ambiente virtual (venv).

1. Instale as dependências:

Bash
pip install beautifulsoup4 sentence-transformers torch
2. Prepare o ambiente:
Certifique-se de que o arquivo original noticias_brutas.json esteja dentro de uma pasta chamada dados/ na raiz do projeto.

3. Execute a limpeza dos dados:

Bash
python etapa1.py
Isso irá popular a pasta dados/ com os arquivos .txt limpos.

4. Execute o motor de busca:

Bash
python etapa2.py
O script irá calcular as similaridades e imprimir no terminal as notícias mais relevantes para as queries configuradas.

📊 Avaliação Qualitativa
A abordagem utilizando o modelo all-MiniLM-L6-v2 demonstrou grande capacidade de conectar o termo pesquisado ao contexto real do texto. A conversão da pontuação de similaridade em tensores e o isolamento dos índices garantem que a recuperação da informação ocorra em tempo hábil e de forma escalável. Ao iterar diretamente sobre os índices extraídos via PyTorch, o motor atinge o objetivo de retornar resultados coerentes para queries complexas como "mercado de trabalho e desemprego" e "inflação e preços ao consumidor".

Desenvolvido por Breno Nunes de Almeida GitHub: brenonunes96 
