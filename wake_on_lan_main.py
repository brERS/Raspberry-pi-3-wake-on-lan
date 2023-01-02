import os

from dotenv import load_dotenv

from template.wake_on_lan import WakeOnLan


def main():

    load_dotenv()

    WakeOnLan(
        os.environ.get('BASE_DIR'),
        os.environ.get('MAC_ADDRESS'),
    ).send_magic_packet()


if __name__ == "__main__":
    main()
