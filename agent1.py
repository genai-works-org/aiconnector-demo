import asyncio
from AIConnector.session import Session, Config

AGENT_NAME = "agent1"

async def message_handler(message: str) -> str:
    return f"Response from {AGENT_NAME} on message '{message}'"

async def start_session():
    session = Session(
        client_name=AGENT_NAME,
        # log_level='info',
        config=Config(
            connection_type="remote",
            azure_access_key="8WqDBAeLks29QSyUln4lYvbRXo3lo0rbHZMxCZrV1bRbjw0J3IN7JQQJ99BCAC5RqLJXJ3w3AAAAAWPSUXn8",
            azure_endpoint_url="https://tf-genai-webpubsub.webpubsub.azure.com",
        )
    )
    await session.start(message_handler=message_handler)

async def main():
    await start_session()
    await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
