"""
Lambda Function: validate_file

Responsável por validar arquivos recebidos pelo AWS Step Functions.

Autor: Sergio Santos
Projeto: Workflows Automatizados com AWS Step Functions
"""

import json
import logging

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Extensões permitidas
ALLOWED_EXTENSIONS = [".csv", ".json", ".txt"]


def is_valid_extension(filename: str) -> bool:
    """
    Verifica se a extensão do arquivo é suportada.
    """
    return any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)


def lambda_handler(event, context):
    """
    Função principal da Lambda.

    Parameters
    ----------
    event : dict
        Evento recebido pelo Step Functions.

    context : LambdaContext

    Returns
    -------
    dict
    """

    logger.info("Iniciando validação do arquivo")

    try:

        filename = event.get("filename")

        if not filename:
            logger.error("Nome do arquivo não informado.")

            return {
                "valid": False,
                "message": "filename é obrigatório."
            }

        logger.info(f"Arquivo recebido: {filename}")

        if not is_valid_extension(filename):

            logger.warning(
                f"Extensão inválida para o arquivo {filename}"
            )

            return {
                "valid": False,
                "message": "Extensão de arquivo não suportada."
            }

        logger.info("Arquivo validado com sucesso.")

        return {
            "valid": True,
            "filename": filename,
            "message": "Arquivo válido."
        }

    except Exception as error:

        logger.exception(
            f"Erro durante a validação: {str(error)}"
        )

        return {
            "valid": False,
            "message": "Erro interno durante a validação."
        }
