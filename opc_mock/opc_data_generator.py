import asyncio
import logging
import random

from asyncua import Server, ua


async def run_opcue():
    # Configuração do logger para o módulo asyncua.
    _logger = logging.getLogger("asyncua")

    # Configuração do servidor OPC UA.
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # Configuração do namespace.
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)
    ns = "ns=2;s=freeopcua.Tags.pressure"

    min_val = -0.5
    max_val = 0.6

    # Preenchimento do espaço de endereçamento.
    my_object = await server.nodes.objects.add_object(idx, "my_object")
    pressure = await my_object.add_variable(ns, "pressure", 10.5)

    # Configuração da variável como gravável pelos clientes.
    await pressure.set_writable()
    opcs = [pressure]

    _logger.info("Iniciando o servidor OPC UA!")

    # Inicialização do servidor OPC UA e execução do loop principal.
    async with server:
        while True:
            await asyncio.sleep(1)
            # Simulação de valores de pressão aleatórios.
            counter = random.uniform(min_val, max_val)
            for opc in opcs:
                new_value = await opc.get_value() + counter
                # Limitação dos valores entre 0.0 e 100.0.
                new_value = min(100.0, max(0.0, new_value))
                _logger.info("Definir valor de %s para %.1f", opc, new_value)
                await opc.write_value(new_value)


if __name__ == "__main__":
    # Configuração do logger principal e execução da função principal utilizando o asyncio.
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(run_opcue(), debug=True)
