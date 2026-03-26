nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota (0 a 10): "))

nota2 = float(input("Digite a segunda nota (0 a 10): "))

nota3 = float(input("Digite a segunda nota (0 a 10): "))

nota4 = float(input("Digite a segunda nota (0 a 10): "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10 or nota4 < 0 or nota4 > 10:
    print("\nNota inválida! Digite valores entre 0 e 10.")

else:
    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"Aluno: {nome}")
    print(f"Primeira nota: {nota1}")
    print(f"Segunda nota: {nota2}")
    print(f"Terceira nota: {nota3}")
    print(f"Quarta nota: {nota4}")
    print(f"Média final: {media:.1f}")

if media >= 7:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")

