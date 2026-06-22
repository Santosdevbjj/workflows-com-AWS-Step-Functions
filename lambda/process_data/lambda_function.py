"""
Lambda Function: process_data

Responsável por processar arquivos previamente validados.

Autor: Sergio Santos
Projeto: Workflows Automatizados com AWS Step Functions
"""

import json
import logging
from datetime import datetime

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Função principal da Lambda.

    Parameters
    ----------
    event : dict
        Evento recebido pelo AWS Step Functions.

    context : LambdaContext

    Returns
    -------
    dict
    """

    logger.info("Iniciando processamento do arquivo")

    try:

        filename = event.get("filename")

        if not filename:

            logger.error(
                "Nome do arquivo não informado."
            )

            raise ValueError(
                "filename é obrigatório."
            )

        logger.info(
            f"Processando arquivo: {filename}"
        )

        processing_timestamp = datetime.utcnow().isoformat()

        # Simulação do processamento
        records_processed = 1000

        logger.info(
            f"{records_processed} registros processados com sucesso."
        )

        return {
            "status": "processed",
            "filename": filename,
            "records_processed": records_processed,
            "processed_at": processing_timestamp
        }

    except Exception as error:

        logger.exception(
            f"Erro durante o processamento: {str(error)}"
        )

        return {
            "status": "failed",
            "message": str(error)
        }
