# ==========================================
# 1. FUNÇÕES E PROCEDIMENTOS (MODULARES)
# ==========================================

def calcular_media(nota1, nota2):
    """Função específica para calcular a média (Opção A)"""
    return (nota1 + nota2) / 2


def verificar_status(media):
    """Função específica para decidir a situação do aluno (Opção A)"""
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorio(nomes, medias, status):
    """Procedimento que imprime os dados linha por linha (Opção A do Relatório)"""
    print("\n" + "="*40)
    print("      RELATÓRIO DE DESEMPENHO ESCOLAR      ")
    print("="*40)
    print(f"{'ALUNO':<15} | {'MÉDIA':<6} | {'STATUS':<10}")
    print("-"*40)
    
    # Percorre as listas usando o mesmo índice 'i' (Opção 1 - Vetores Separados)
    for i in range(len(nomes)):
        print(f"{nomes[i]:<15} | {medias[i]:<6.1f} | {status[i]:<10}")
        
    print("="*40)


# ==========================================
# 2. PROGRAMA PRINCIPAL (EXECUÇÃO)
# ==========================================

# Nossos 3 vetores (listas) paralelos para armazenar os dados (Opção 1)
lista_nomes = ["Ana Silva", "Bruno Lima", "Carlos Souza", "Daniela Reis"]
lista_medias = []
lista_status = []

# Simulando as notas que os professores digitaram no sistema para cada aluno
notas_alunos = [
    (8.5, 7.5),  # Notas da Ana
    (4.0, 5.5),  # Notas do Bruno
    (6.0, 6.5),  # Notas do Carlos
    (3.0, 4.5)   # Notas da Daniela
]

# Processando os dados de cada aluno
for i in range(len(lista_nomes)):
    n1, n2 = notas_alunos[i]
    
    # 1. Calcula a média usando a função específica
    media_final = calcular_media(n1, n2)
    lista_medias.append(media_final)
    
    # 2. Define o status usando a outra função específica
    situacao = verificar_status(media_final)
    lista_status.append(situacao)

# 3. Exibe o relatório na tela linha por linha
gerar_relatorio(lista_nomes, lista_medias, lista_status)