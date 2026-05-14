from bs4 import BeautifulSoup;
import json
import re
import sentence_transformers
with open("dados/noticias_brutas.json","r",encoding='utf-8' ) as noticias:    # abre pra ver o json
        dados= json.load(noticias)


for x in dados:
        soup = BeautifulSoup(x['texto'],"html.parser")       #limpa as tags de html dentro da chave  texto

        dadosTHtml = soup.get_text()         


        dadosEspaço = re.sub(r"\s+"," ",dadosTHtml)     
       
 

        with open(f'dados/{x['id']}.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(dadosEspaço)
        





