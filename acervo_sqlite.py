import sqlite3
from pathlib import Path


DB_FILE = 'acervo.db'

def conectar_bd(db_name=DB_FILE):
    return sqlite3.connect(db_name)

def executar_e_comitar(conn, sql, parametros=()):
    try:
        cursor = conn.cursor()
        cursor.execute(sql, parametros)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao executar o comando: {e}")
        return False
    



def criar_tabela_livros(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS Livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT,
        ano INTEGER,
        genero TEXT,
        disponivel INTEGER
    );
    """
    return executar_e_comitar(conn, sql)

def testar_criacao_tabela(conn):
    criar_tabela_livros(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Livros';")
    resultado = cursor.fetchone()
    
    assert resultado is not None, "A tabela Livros não foi criada."
    print("✅ Teste 3: Tabela 'Livros' criada com sucesso.")

if __name__ == '__main__':
    with conectar_bd() as conn:
        print("--- Execução da Etapa 3: Criar Tabela Livros ---")
        if criar_tabela_livros(conn):
            testar_criacao_tabela(conn)   



def inserir_livro(conn, titulo, autor, ano, genero, disponivel=1):
    sql = "INSERT INTO Livros (titulo, autor, ano, genero, disponivel) VALUES (?, ?, ?, ?, ?)"
    parametros = (titulo, autor, ano, genero, disponivel)
    return executar_e_comitar(conn, sql, parametros)

def inserir_5_livros(conn):
    conn.execute("DELETE FROM Livros;") 
    conn.commit()
    
    livros_ficticios = [
        ("Pequeno Princepe", "Antoine de Saint-Exupéry", 1943, "Romance", 1),
        ("O Motorista e o Milionário", "Joachim de Posada", 2007, "Relato Pessoal", 1),
        ("Dom Quixote de la Mancha", "Miguel de Cervantes", 1605, "Ficção", 1),
        ("O Senhor dos Anéis", "J. R. R. Tolkien", "Ficção", 0),
        ("A Bíblia Sagrada", "Vários autores", 1000, "Investigativo e educativo sobre vida e comportamento em geral", 1)
    ]
    
    sucesso = True
    for livro in livros_ficticios:
        if not inserir_livro(conn, *livro):
            sucesso = False
            
    return sucesso


def testar_insercao_livros(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Livros;")
    count = cursor.fetchone()[0]
    
    assert count == 5, f"Esperado 5 livros, encontrado {count}."
    print("✅ Teste 4: 5 Livros inseridos com sucesso.")


if __name__ == '__main__':
    with conectar_bd() as conn:
        criar_tabela_livros(conn)
        
        print("--- Execução da Etapa 4: Inserir 5 Livros Fictícios ---")
        if inserir_5_livros(conn):
            testar_insercao_livros(conn)




def consultar_livros_disponiveis(conn):
    sql = "SELECT id, titulo, autor, ano, genero FROM Livros WHERE disponivel = 1 ORDER BY titulo"
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def testar_consulta_disponiveis(conn):
    livros_disponiveis = consultar_livros_disponiveis(conn)
    
    assert len(livros_disponiveis) == 4, f"Esperado 4 livros disponíveis, encontrado {len(livros_disponiveis)}."
    
    print("✅ Teste 5: Consulta de livros disponíveis correta.")
    print("   Livros disponíveis:")
    for livro in livros_disponiveis:
        print(f"     ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}")

if __name__ == '__main__':
    with conectar_bd() as conn:
        criar_tabela_livros(conn)
        inserir_5_livros(conn) 
        print("--- Execução da Etapa 5: Consultar Livros Disponíveis ---")
        testar_consulta_disponiveis(conn)




def atualizar_disponibilidade(conn, titulo_livro, novo_status):
    sql = "UPDATE Livros SET disponivel = ? WHERE titulo = ?"
    parametros = (novo_status, titulo_livro)
    return executar_e_comitar(conn, sql, parametros)


def testar_atualizacao_disponibilidade(conn):
    titulo_alvo = "O Encontro Marcado"
    novo_status = 0

    if not atualizar_disponibilidade(conn, titulo_alvo, novo_status):
        raise AssertionError(f"Falha ao atualizar disponibilidade de '{titulo_alvo}'.")

    cursor = conn.cursor()
    cursor.execute("SELECT disponivel FROM Livros WHERE titulo = ?", (titulo_alvo,))
    row = cursor.fetchone()
    assert row is not None, f"Livro '{titulo_alvo}' não encontrado."
    status_atual = row[0]

    assert status_atual == novo_status, f"Status de '{titulo_alvo}' não atualizado corretamente."
    print(f"✅ Teste 6: Disponibilidade de '{titulo_alvo}' atualizada para {novo_status} com sucesso.")


if __name__ == '__main__':
    with conectar_bd() as conn:
        criar_tabela_livros(conn)
        inserir_5_livros(conn)
        print("--- Execução da Etapa 6: Atualizar Disponibilidade ---")
        testar_atualizacao_disponibilidade(conn)




def ordenar_livros_por_ano(conn):
    sql = "SELECT id, titulo, ano FROM Livros ORDER BY ano DESC"
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def testar_ordenacao_por_ano(conn):
    livros_ordenados = ordenar_livros_por_ano(conn)
    
    anos_esperados = [2007, 1993, 1984, 1956, 1881]
    anos_reais = [livro[2] for livro in livros_ordenados]
    
    assert anos_reais == anos_esperados, f"Ordenação incorreta. Esperado {anos_esperados}, obtido {anos_reais}."
    
    print("✅ Teste 7: Livros ordenados por ano (mais recente para o mais antigo) com sucesso.")
    print("   Livros Ordenados:")
    for livro in livros_ordenados:
        print(f"     ID: {livro[0]}, Título: {livro[1]}, Ano: {livro[2]}")

if __name__ == '__main__':
    with conectar_bd() as conn:
        criar_tabela_livros(conn)
        inserir_5_livros(conn)
        print("--- Execução da Etapa 7: Ordenar Livros por Ano ---")
        testar_ordenacao_por_ano(conn)




def deletar_livros_antigos(conn, ano_limite):
    sql = "DELETE FROM Livros WHERE ano < ?"
    parametros = (ano_limite,)
    return executar_e_comitar(conn, sql, parametros)


def testar_delecao_livros(conn):
    ano_limite = 1940
    if not deletar_livros_antigos(conn, ano_limite):
        raise AssertionError(f"Falha ao deletar livros anteriores a {ano_limite}.")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Livros;")
    count_restante = cursor.fetchone()[0]
    
    assert count_restante == 4, f"Esperado 4 livros restantes, encontrado {count_restante}."
    
    
    cursor.execute("SELECT titulo FROM Livros WHERE ano = ?", (1881,))
    livro_deletado = cursor.fetchone()
    
    assert livro_deletado is None, "O livro antigo não foi deletado."
    
    print(f"✅ Teste 8: Livro(s) com ano anterior a {ano_limite} deletado(s) com sucesso. Restam {count_restante} livros.")


if __name__ == '__main__':
    with conectar_bd() as conn:
        criar_tabela_livros(conn)
        inserir_5_livros(conn)
        print("--- Execução da Etapa 8: Deletar Livros Antigos ---")
        testar_delecao_livros(conn)    




def criar_tabela_usuario(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    );
    """
    return executar_e_comitar(conn, sql)

def testar_criacao_tabela_usuario(conn):
    criar_tabela_usuario(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Usuario';")
    resultado = cursor.fetchone()
    
    assert resultado is not None, "A tabela Usuario não foi criada."
    print("✅ Teste 9: Tabela 'Usuario' criada com sucesso.")

if __name__ == '__main__':
    with conectar_bd() as conn:
        print("--- Execução da Etapa 9: Criar Tabela Usuario ---")
        testar_criacao_tabela_usuario(conn)



def alterar_tabela_usuario_idade(conn):
    sql = "ALTER TABLE Usuario ADD COLUMN idade INTEGER;"
    try:
        return executar_e_comitar(conn, sql)
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            return True 
        print(f"Erro ao alterar a tabela Usuario: {e}")
        return False


def testar_alteracao_tabela(conn):
    alterar_tabela_usuario_idade(conn)
    
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Usuario);")
    colunas = [coluna[1] for coluna in cursor.fetchall()]  # coluna[1] é o nome da coluna
    
    assert 'idade' in colunas, "A coluna 'idade' não foi adicionada à tabela Usuario."
    print("✅ Teste 10: Coluna 'idade' adicionada à tabela 'Usuario' com sucesso.")

if __name__ == '__main__':
    with conectar_bd() as conn:
        print("--- Execução da Etapa 10: Alterar Tabela Usuario ---")
        testar_alteracao_tabela(conn)


def inserir_usuario(conn, nome, idade):
    sql = "INSERT INTO Usuario (nome, idade) VALUES (?, ?)"
    parametros = (nome, idade)
    return executar_e_comitar(conn, sql, parametros)

def inserir_5_usuarios(conn):
    conn.execute("DELETE FROM Usuario;") 
    conn.commit()
    
    usuarios_ficticios = [
        ("Rafael", 30),
        ("ELIANA", 40),
        ("Cassiana", 36),
        ("Marilia", 45),
        ("Pedro", 20)
    ]
    
    sucesso = True
    for usuario in usuarios_ficticios:
        if not inserir_usuario(conn, *usuario):
            sucesso = False
            
    return sucesso

def testar_insercao_usuarios(conn):
    if not inserir_5_usuarios(conn):  # Executa a inserção
        raise AssertionError("Falha ao inserir os usuários.")
    
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Usuario;")
    count = cursor.fetchone()[0]
    
    assert count == 5, f"Esperado 5 usuários, encontrado {count}."
    print("✅ Teste 11: 5 Usuários inseridos com sucesso.")

if __name__ == '__main__':
    with conectar_bd() as conn:
        print("--- Execução da Etapa 11: Inserir 5 Usuários Fictícios ---")
        testar_insercao_usuarios(conn)




def apagar_tabela_usuario(conn):
    sql = "DROP TABLE IF EXISTS Usuario;"
    return executar_e_comitar(conn, sql)

def testar_delecao_tabela_usuario(conn):
    apagar_tabela_usuario(conn)
    
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Usuario';")
    resultado = cursor.fetchone()
    
    assert resultado is None, "A tabela Usuario não foi apagada."
    print("✅ Teste 12: Tabela 'Usuario' apagada com sucesso.")

if __name__ == '__main__':
    with conectar_bd() as conn:
        print("--- Execução da Etapa 12: Apagar Tabela Usuario ---")
        testar_delecao_tabela_usuario(conn)
