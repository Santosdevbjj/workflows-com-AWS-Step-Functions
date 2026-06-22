"""
Lambda Function: notify_execution

Responsável por publicar notificações no Amazon SNS.

Autor: Sergio Santos
Projeto: Workflows Automatizados com AWS Step Functions
"""

import json
import logging
import os

import boto3

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Cliente SNS
sns_client = boto3.client("sns")

# ARN do tópico SNS (configurado como variável de ambiente)
TOPIC_ARN = os.getenv("TOPIC_ARN")


def lambda_handler(event, context):
    """
    Função principal.

    Parameters
    ----------
    event : dict
        Evento recebido pelo AWS Step Functions.

    context : LambdaContext

    Returns
    -------
    dict
    """

    logger.info("Iniciando envio de notificação.")

    try:

        filename = event.get("filename", "unknown")
        status = event.get("status", "processed")

        message = {
            "event": "file_processed",
            "filename": filename,
            "status": status
        }

        logger.info(
            f"Publicando evento no SNS para arquivo {filename}"
        )

        response = sns_client.publish(
            TopicArn=TOPIC_ARN,
            Subject="File Processing Notification",
            Message=json.dumps(message)
        )

        logger.info(
            f"Mensagem publicada com sucesso. MessageId: {response['MessageId']}"
        )

        return {
            "status": "notification_sent",
            "message_id": response["MessageId"],
            "filename": filename
        }

    except Exception as error:

        logger.exception(
            f"Erro ao enviar notificação: {str(error)}"
        )

        return {
            "status": "failed",
            "message": str(error)
        }
