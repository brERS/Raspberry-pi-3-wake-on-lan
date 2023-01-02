from datetime import datetime
from logging import basicConfig, warning
from subprocess import run


class WakeOnLan:

    def __init__(self, base_dir, ip, mac):
        self.base_dir = base_dir
        self.ip = ip
        self.mac = mac
        self.file_log = f'{self.base_dir}log/wake_on_lan.log'
        self.file_error = f'{self.base_dir}log/wake_on_lan.error'

    def send_magic_packet(self):

        try:
            res = run(
                ["wakeonlan", "-i", self.ip, self.mac],
                capture_output=True,
                text=True,
            )

            with open(self.file_log, "w") as log:
                log.write(
                    f"""
                    Wake on Lan: {res.stdout}
                    Return code: {res.returncode}
                    Run command: {res.args}
                    Running at: {self.date_time()}
                    """
                )

            self.output()

        except Exception as error:
            with open(self.file_error, "w") as file_error:
                file_error.write(
                    f"""
                    {str(error)}
                    Running at: {self.date_time()}
                    """
                )

    def date_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def output(self):
        basicConfig(format='%(asctime)s %(message)s')
        warning(
            f'\nExecutado com sucesso\nLog em: {self.file_log}'
        )
