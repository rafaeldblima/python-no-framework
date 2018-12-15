from db.database_connection import db_connection, db

partido_table = "CREATE TABLE partido (id serial primary key , nome VARCHAR(150) not null, " \
                " sigla varchar(10)    not null, fundo  decimal(10, 2) null," \
                " numero integer   not null, created_at TIMESTAMP )"

resp = db.execute("select exists(select * from information_schema.tables where table_name=%s)", ('partido',))

# checando se a tabela já foi criada
if db.fetchone()[0]:
    print('Tabela partido já criada.')
else:
    db.execute(partido_table)

db_connection.commit()
# db_connection.close()
# db.close()
