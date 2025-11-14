from datetime import datetime
from pathlib import Path

PASTA_LOGS = Path("logs")
ARQUIVO_LOG = PASTA_LOGS / "entrada_usuario.txt"


def registrar_entrada():
    """Loop de leitura de entrada do usuário e registro em arquivo."""
    PASTA_LOGS.mkdir(exist_ok=True)

    print(
        """
SIMULAÇÃO DE KEYLOGGER

Tudo o que você digitar será salvo no arquivo logs/entrada_usuario.txt,
junto com a data e hora. Digite 'sair' para encerrar.
"""
    )

    while True:
        texto = input("Digite algo (ou 'sair' para encerrar): ")

        if texto.lower().strip() == "sair":
            print("Encerrando simulação de keylogger.")
            break

        timestamp = datetime.now().isoformat(timespec="seconds")

        with ARQUIVO_LOG.open("a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {texto}\n")


if __name__ == "__main__":
    registrar_entrada()