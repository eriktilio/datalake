import asyncio
import logging
import random

from asyncua import Server, ua


async def run_opcue():
    _logger = logging.getLogger("asyncua")
    # Configurar nosso servidor
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # Configurar nosso próprio namespace, não é realmente necessário, mas recomendado
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)
    ns = "ns=2;s=freeopcua.Tags.pressure"

    min_val = -0.5
    max_val = 0.6

    # Preencher nosso espaço de endereçamento
    # server.nodes contém links para nós muito comuns como objetos e raiz
    my_object = await server.nodes.objects.add_object(idx, "my_object")
    pressure = await my_object.add_variable(ns, "pressure", 10.5)
    # Definir MinhaVariavel como gravável pelos clientes
    await pressure.set_writable()
    opcs = [pressure]

    _logger.info("Iniciando o servidor!")
    async with server:
        while True:
            await asyncio.sleep(1)
            counter = random.uniform(min_val, max_val)
            for opc in opcs:
                new_value = await opc.get_value() + counter
                if new_value > 100.0:
                    new_value = 100.0
                elif new_value < 0.0:
                    new_value = 0.0
                _logger.info("Definir valor de %s para %.1f", opc, new_value)
                await opc.write_value(new_value)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(run_opcue(), debug=True)
