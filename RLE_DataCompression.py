def comprimir(texto):
    """
    Comprime apenas sequências de espaços usando a flag '#'.
    Outros caracteres permanecem inalterados.
    """
    if not texto:
        return ""
    
    resultado = []
    contagem_espacos = 0
    
    for char in texto:
        if char == ' ':
            contagem_espacos += 1
        else:
            # Se havia espaços antes, adiciona a compressão
            if contagem_espacos > 0:
                resultado.append(f"#{contagem_espacos}")
                contagem_espacos = 0
            resultado.append(char)
    
    # Não esquecer dos espaços no final do texto
    if contagem_espacos > 0:
        resultado.append(f"#{contagem_espacos}")
    
    return "".join(resultado)

def descomprimir(texto_comprimido):
    """
    Descomprime o texto, interpretando apenas as flags 'b' para espaços.
    """
    if not texto_comprimido:
        return ""
    
    resultado = []
    i = 0
    
    try:
        while i < len(texto_comprimido):
            # Verifica se é uma sequência de espaços (flag 'b')
            if texto_comprimido[i] == '#':
                i += 1
                # Coleta o número após a flag 'b'
                count_str = ""
                while i < len(texto_comprimido) and texto_comprimido[i].isdigit():
                    count_str += texto_comprimido[i]
                    i += 1
                    
                # Verifica se encontrou algum número após '#'
                if not count_str:
                    raise ValueError("Número esperado após a flag '#'")
                    
                # Adiciona os espaços
                count = int(count_str)
                resultado.append(' ' * count)
            else:
                # Adiciona o caractere normalmente
                resultado.append(texto_comprimido[i])
                i += 1
                
        return "".join(resultado)
    
    except ValueError as e:
        raise ValueError(f"Erro no formato do texto comprimido: {str(e)}")

def comprimir_arquivo(arquivo_entrada, arquivo_saida):
    """
    Lê um arquivo de texto, comprime seu conteúdo e salva em outro arquivo.
    """
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            texto = f.read()
            
        texto_comprimido = comprimir(texto)
        
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(texto_comprimido)
            
        print(f"Arquivo comprimido com sucesso!")
        print(f"Tamanho original: {len(texto)} bytes")
        print(f"Tamanho comprimido: {len(texto_comprimido)} bytes")
        print(f"Taxa de compressão: {(1 - len(texto_comprimido)/len(texto))*100:.2f}%")
        
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro ao processar arquivo: {str(e)}")

def descomprimir_arquivo(arquivo_entrada, arquivo_saida):
    """
    Lê um arquivo comprimido e salva sua versão descomprimida em outro arquivo.
    """
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            texto_comprimido = f.read()
            
        texto_descomprimido = descomprimir(texto_comprimido)
        
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(texto_descomprimido)
            
        print("Arquivo descomprimido com sucesso!")
        
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado!")
    except ValueError as e:
        print(f"Erro ao descomprimir: {str(e)}")
    except Exception as e:
        print(f"Erro ao processar arquivo: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    # Para comprimir
    comprimir_arquivo("entrada.txt", "comprimido.txt")
    
    # Para descomprimir
    descomprimir_arquivo("comprimido.txt", "descomprimido.txt")
