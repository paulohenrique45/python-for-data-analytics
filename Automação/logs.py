import logging

logging.basicConfig(level=logging.INFO)

def processar_dados():

    logging.info("Processamento Iniciado")

    vendas = [100,200,150]

    total = sum(vendas)

    logging.info("Total calculado: %s",total)


processar_dados()