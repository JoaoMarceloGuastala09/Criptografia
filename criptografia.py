alfabeto = list("abcdefghijklmnopqrstuvwxyzéçãá.1234567890")
chave = list("zyxwvutsrpqonmlkjihgfedcba[?:#!0987654321")

def criptografar(mensagem):
    mensagem = mensagem.lower()
    resultado = []
    for letra in mensagem:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            resultado.append(chave[indice])
        else:
            resultado.append(letra)
    return "".join(resultado)

def descriptografar(mensagem_criptografada):
    resultado = []
    for letra in mensagem_criptografada:
        if letra in chave:
            indice = chave.index(letra)
            resultado.append(alfabeto[indice])
        else:
            resultado.append(letra)
    return "".join(resultado)

while True:
    escolha = input("Deseja criptografar ou descriptografar uma mensagem? \n[1] Criptografar\n[2] Descriptografar\nDigite 1 ou 2: ")
    if escolha in ["1", "2"]:
        escolha = int(escolha)
        break
    print("Entrada inválida. Digite apenas 1 ou 2.")

mensagem = input("Digite a mensagem: ").strip()
if not mensagem:
    print("Você não digitou nenhuma mensagem!")
else:
    if escolha == 1:
        mensagem_criptografada = criptografar(mensagem)
        print("\nMensagem original:", mensagem)
        print("Mensagem criptografada:", mensagem_criptografada)
    else:
        mensagem_descriptografada = descriptografar(mensagem)
        print("\nMensagem criptografada:", mensagem)
        print("Mensagem descriptografada:", mensagem_descriptografada)