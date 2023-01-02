# Raspberry-pi-3-wake-on-lan
Inicializar host via rede

## Pré requisitos
- wakeonlan instalado no Raspberry Pi 3 
    ```
        sudo apt install etherwake -y
    ```
- Host remoto com placa de rede com suporte a Wake On Lan (WOL), em alguns casos é necessário habilitar o WOL na BIOS do host remoto.

- Ajuste o valor das variaveis no arquivo conf.toml conforme a necessidade.
    ```
    [environment]
    base_dir = '/CAMINHO/COMPLETO/ATÉ/O/DIRETORIO/DE/EXECUÇÃO/'

    [environment.host]
    mac = '00:11:22:33:44:55' # MAC DO HOST REMOTO
    ```
- Apos ajustar o arquivo conf.toml, execute o script.
    ```
    python wake_on_lan_main.py
    ```

