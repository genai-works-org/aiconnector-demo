import asyncio
from AIConnector.session import Session, Config


async def message_handler(i, msg: str) -> str:
    return f"Response from client {i} on message: {msg}"


async def start_session():
    session = Session(
        client_name="client",
        # log_level='info',
        client_id="clientId",
        config=Config(
            connection_type="remote",
            azure_access_key="8WqDBAeLks29QSyUln4lYvbRXo3lo0rbHZMxCZrV1bRbjw0J3IN7JQQJ99BCAC5RqLJXJ3w3AAAAAWPSUXn8",
            azure_endpoint_url="https://tf-genai-webpubsub.webpubsub.azure.com",
        )
    )
    # await session.start(message_handler=lambda msg: message_handler(i, msg))
    await session.start()

    print(await session.get_client_list(30))

    is_agent1_ok, response = await session.send("agent1", "message to agent1")
    print(is_agent1_ok, response)
    if is_agent1_ok: 
        is_agent2_ok, response = await session.send("agent2", "message to agent2")
        print(is_agent2_ok, response)


async def main():
    await start_session()

    await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
