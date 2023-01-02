import toml

from template.wake_on_lan import WakeOnLan


def main():
    env = toml.load("conf.toml")

    WakeOnLan(
        env['environment']['base_dir'],
        env['environment']['host']['ip'],
        env['environment']['host']['mac']
    ).send_magic_packet()


if __name__ == "__main__":
    main()
