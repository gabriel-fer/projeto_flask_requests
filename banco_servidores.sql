drop table servidores;

CREATE TABLE servidores (
    id INTEGER PRIMARY KEY,
    categoria TEXT NOT NULL,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    matricula TEXT UNIQUE NOT NULL,
    campus TEXT NOT NULL);


select * from  servidores;

