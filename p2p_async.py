import asyncio
import socket

config = {}


async def handle_client(reader, writer):
    request = None
    while request != "quit":
        request = (await reader.read(255)).decode("utf8")
        response = str(eval(request)) + "\n"
        writer.write(response.encode("utf8"))
        await writer.drain()
    writer.close()


async def make_requests():
    message = f"hi from {config['local_IP']}"
    while True:
        reader, writer = await asyncio.open_connection(config['remote_IP'], 15555)

        print(f"Send: {message!r}")
        writer.write(message.encode())

        data = await reader.read(100)
        print(f"Received: {data.decode()!r}")

        print("Close the connection")
        writer.close()

        await asyncio.sleep(3)


def setup():
    global config
    config["local_IP"] = socket.gethostbyname(socket.gethostname())
    config["remote_IP"] = input("IP to connect to: ")


if __name__ == "__main__":
    setup()
    loop = asyncio.get_event_loop()
    loop.create_task(asyncio.start_server(handle_client, "localhost", 15555))
    loop.create_task(asyncio.run(make_requests()))
    loop.run_forever()
