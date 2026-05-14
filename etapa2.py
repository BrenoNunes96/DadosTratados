from sentence_transformers import SentenceTransformer
import os
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")     
import torch

texts = []
file_names = []
data_dir = "dados"

for file_name in os.listdir(data_dir):
     if file_name.endswith(".txt"):
         file_path = os.path.join(data_dir, file_name) # procura na pasta dados cada  arquivo de la dentro

         with open(file_path, "r", encoding="utf-8") as file:
             text = file.read()              # le o arquivo em si
 
         texts.append(text) # envia para texts
         file_names.append(file_name)


embeddings = model.encode(texts)   #embbeding  transforma em vetor

pergunta = "mudanças na taxa de juros",
"mercado de trabalho e desemprego",
"inflação e preços ao consumidor"

pergunta_embedding = model.encode(pergunta)   #embbeding

similarities = model.similarity(pergunta_embedding, embeddings)  # compara 
print(similarities)


quantidade_resultados = 3

valores, indices = torch.topk(similarities[0], k=quantidade_resultados)  # compara quais tensores sao mais altos, k a quantia a ser mostrado


lista_de_indices = indices.tolist()  # apenas puxa indices os tres apenas

print(f"Os índices das notícias mais relevantes são: {lista_de_indices}")

print("\n--- RESULTADOS DA BUSCA ---")
for idx in lista_de_indices:    # indices de similarities e de texts sao os mesmo pois estamos aplicando na mesma ordem nos elementos

    noticia_encontrada = texts[idx]  # usa os tres indices mais compativeis e entra em texts onde estao as noticias
 
    print(f"\nRelevância: {similarities[0][idx]:.4f}")        # tensor numeral explanado idx =[0,6,5] indices q tao no similaarities
    print(f"Texto: {noticia_encontrada}")