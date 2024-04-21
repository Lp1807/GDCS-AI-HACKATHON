# Chatbot







### SINGLE_DOCUMENT



User: attachment

Chatbot: attachment in forma strutturata ( JSON)



User: Text

Chatbot: risponde alla domanda utilizzando i dati salvati nel JSON.



### DATABASE



User: attachment 

Chatbot: FERMO!!



User: text

Chatbot: effettua query su DB e risponde in linguaggio naturale.





### Stato attuale DB

1. recupero immagini dal DB.
2. recupero i metadati associati (JSON)
3. creo embedding dei JSON
4. inserisco gli embeddings in un vector database
5. computo similarity. tra query e vettori nel DB
6. restituisco knn.



### Obiettivo

abbiamo un CSV con info tabulare.

faccio query in linguaggio naturale

e il chatbot risponde



Gianvito parte già da un CSV.



​        **print**(f"INFORMAZIONE--------------------")



https://bitbucket.org/mlreply/mlr-poc-datatalkai/src/develop/src/



### 