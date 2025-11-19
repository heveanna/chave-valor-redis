import pymongo
from datetime import datetime

def sistema_matriculas():
    print(" SISTEMA DE MATRÍCULAS - FACULDADE")
    print("=" * 50)
    
    try:
        # 1. CONEXÃO COM MONGODB LOCAL
        client = pymongo.MongoClient("mongodb+srv://Anabwooc:=========@anabeatrizoliveira.paviryf.mongodb.net/?appName=AnabeatrizOliveira")
        
        # Testar se a conexão funciona
        client.admin.command('ping')
        print(" Conectado ao MongoDB!")
        
        # Criar/Carregar banco e coleção
        db = client["faculdade_db"]
        alunos = db["matriculas"]
        
        # Limpar coleção para teste (opcional)
        alunos.delete_many({})
        print(" Banco preparado para demonstração...")
        
        # 2. CREATE - Matricular alunos
        print("\n MATRICULANDO ALUNOS...")
        
        aluno1 = {
            "_id": "2024001001",
            "nome": "Ana Beatriz Oliveira Florentino",
            "curso": "Ciência de Dados",
            "periodo": 2,
            "disciplinas": ["Programação II", "Cálculo II", "Banco de Dados I"],
            "bolsista": True,
            "data_matricula": datetime.now()
        }
        
        aluno2 = {
            "_id": "2024001002", 
            "nome": "Thauãn Rodrigues Leite",
            "curso": "Ciências de Dados",
            "periodo": 1,
            "disciplinas": ["Estrutura de Dados", "Banco de Dados", "Lógica de Programação"],
            "bolsista": False,
            "data_matricula": datetime.now()
        }
        
        alunos.insert_many([aluno1, aluno2])
        print(" 2 alunos matriculados!")
        
        # 3. READ - Consultar matrícula
        print("\n CONSULTANDO MATRÍCULA...")
        matricula_busca = "2024001001"
        aluno = alunos.find_one({"_id": matricula_busca})
        
        if aluno:
            print(f" Aluno encontrado: {aluno['nome']}")
            print(f"   Curso: {aluno['curso']}")
            print(f"   Período: {aluno['periodo']}")
            print(f"   Disciplinas: {', '.join(aluno['disciplinas'])}")
            print(f"   Bolsista: {'Sim' if aluno.get('bolsista') else 'Não'}")
        
        # 4. UPDATE - Atualizar matrícula
        print("\n ATUALIZANDO MATRÍCULA...")
        alunos.update_one(
            {"_id": "2024001001"},
            {
                "$set": {
                    "periodo": 3,
                    "disciplinas": ["Pré-Processamento de Dados", "Banco de Dados Não Relacionais", "Visualização de Dados"],
                    "bolsista": False
                }
            }
        )
        print(" Matrícula atualizada (Ana Beatriz Oliveira Florentino -> 3º período)")
        
        # Verificar atualização
        aluno_atualizado = alunos.find_one({"_id": "2024001001"})
        print(f"   Novas disciplinas: {', '.join(aluno_atualizado['disciplinas'])}")
        
        # 5. READ - Listar todos os alunos
        print("\n LISTANDO TODOS OS ALUNOS...")
        todos_alunos = alunos.find()
        for aluno in todos_alunos:
            print(f"   {aluno['_id']} - {aluno['nome']} ({aluno['curso']})")
        
        # 6. DELETE - Cancelar matrícula
        print("\n CANCELANDO MATRÍCULA...")
        resultado = alunos.delete_one({"_id": "2024001002"})
        
        if resultado.deleted_count > 0:
            print(" Matrícula de Thauãn Rodrigues Leite cancelada!")
        
        # Contar alunos restantes
        total = alunos.count_documents({})
        print(f"\n Total de alunos ativos: {total}")
        
    except pymongo.errors.ServerSelectionTimeoutError:
        print(" ERRO: MongoDB não está rodando!")
        print("   Execute 'mongod' no terminal primeiro")
    except Exception as e:
        print(f" Erro: {e}")
    finally:
        if 'client' in locals():
            client.close()
            print("\n Conexão fechada.")

# Executar o sistema
if __name__ == "__main__":
    sistema_matriculas()