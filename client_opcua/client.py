import asyncio
import requests
import os

from datetime import datetime
from asyncua import Client


class OPCUA_Client:
    def __init__(self, server_url):
        self.server_url = server_url
        self.client = None

    async def __aenter__(self):
        self.client = Client(url=self.server_url)
        await self.client.connect()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.disconnect()

    async def read_variable(self, variable_path):
        variable_node = self.client.get_node(variable_path)
        value = await variable_node.read_value()
        return value

    async def disconnect(self):
        if self.client:
            await self.client.disconnect()


async def send_to_logstash(value, timestamp):
    logstash_url = os.environ.get("LOGSTASH_URL", "http://logstash:8080")
    json_data = {
        "pressao": float(value),
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
    }

    try:
        response = requests.post(logstash_url, json=json_data)
        response.raise_for_status()
        print("Dados enviados com sucesso para o Logstash.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar dados para o Logstash: {e}")


async def main():
    opc_url = os.environ.get("OPC_DATA_URL", "opc.tcp://opc_data_generator:4840")
    server_url = opc_url + "/freeopcua/server/"
    variable_path = "ns=2;s=freeopcua.Tags.pressure"

    async with OPCUA_Client(server_url) as opcua_client:
        try:
            while True:
                value = await opcua_client.read_variable(variable_path)
                print(f"Valor da variável de pressão: {value}")

                # Envie o valor para o Logstash a cada leitura
                timestamp = datetime.now()
                await send_to_logstash(value, timestamp)

                # Aguarde um intervalo (por exemplo, 5 segundos) antes de ler novamente
                await asyncio.sleep(10)
        except KeyboardInterrupt:
            print("Script interrompido manualmente. Encerrando o loop.")


if __name__ == "__main__":
    asyncio.run(main())
