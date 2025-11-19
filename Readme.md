#  Projeto: Banco NoSQL Chave-Valor - MongoDB

Este projeto tem como objetivo demonstrar, como o **MongoDB**, um banco NoSQL orientado a documentos, pode funcionar de forma eficiente como uma **loja Chave-Valor (Key-Value Store)**.  
O MongoDB possui características que o tornam uma solução poderosa para o modelo, principalmente por meio do campo **`_id`**, que serve como chave única para cada valor armazenado.


#  Objetivo do Projeto

Demonstrar como aplicar o **modelo Chave-Valor** utilizando o MongoDB:

- Uso de **_id como chave**
- Armazenamento de valores simples e complexos
- CRUD completo no modelo K-V
- Modelagem (Embedding x Referencing)
- Justificativa técnica do uso de NoSQL
- Vantagens e limitações do MongoDB neste contexto

---

# Modelagem Utilizada


Neste projeto, o MongoDB foi utilizado como uma **loja Chave-Valor (Key-Value)**, onde cada documento possui um identificador único definido no campo `_id`, funcionando como a “chave”, e o documento completo representa o “valor”.

A modelagem foi construída considerando dois tipos principais de valores:


# Embedding vs Referencing

O Embedding consiste em colocar os dados diretamente dentro do documento principal.
É usado quando aquela informação pertence ao valor e deve ser recuperada junto com ele.

Quando usar:

* Dados pequenos e estáveis

* Relação natural 1-para-1

* Quando se deseja leitura rápida com apenas uma consulta

* Quando os dados não são compartilhados com outros documentos

{
  "_id": "user:123",
  "nome": "Carla",
  "preferencias": {
    "tema": "claro",
    "notificacoes": true
  }
}
