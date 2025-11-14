from pathlib import Path

PASTA_LAB = Path("laboratorio")
ARQUIVO_ORIGINAL = PASTA_LAB / "arquivo_teste.txt"
ARQUIVO_MODIFICADO = PASTA_LAB / "arquivo_teste_simulado.lock"


def preparar_ambiente():
    """Garante que a pasta de laboratório e o arquivo de teste existam."""
    PASTA_LAB.mkdir(exist_ok=True)

    if not ARQUIVO_ORIGINAL.exists():
        ARQUIVO_ORIGINAL.write_text(
            "Este é um arquivo de teste para a simulação de ransomware.\n",
            encoding="utf-8",
        )


def pseudo_criptografar(texto: str) -> str:
    """
    Pseudo-criptografia simples:
    aqui apenas invertendo o texto como demonstração.
    """
    return texto[::-1]


def simular_ransomware():
    """Fluxo principal da simulação de ransomware."""
    preparar_ambiente()

    # Ler conteúdo do arquivo original
    conteudo = ARQUIVO_ORIGINAL.read_text(encoding="utf-8")

    # Aplicar transformação
    conteudo_modificado = pseudo_criptografar(conteudo)

    # Gravar em novo arquivo "criptografado"
    ARQUIVO_MODIFICADO.write_text(conteudo_modificado, encoding="utf-8")

    # Remover o arquivo original da pasta de laboratório
    ARQUIVO_ORIGINAL.unlink()

    # Exibir mensagem de "resgate" simulada
    mensagem_resgate = """
SEUS ARQUIVOS FORAM "CRIPTOGRAFADOS" (SIMULAÇÃO)

Para fins educacionais, este script demonstra o fluxo básico
de um ransomware em um ambiente controlado.

Nenhum arquivo pessoal fora da pasta 'laboratorio' foi afetado.
"""
    print(mensagem_resgate)


if __name__ == "__main__":
    simular_ransomware()