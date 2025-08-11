# Termux Assistant

Um assistente pessoal de linha de comando para o Termux, que oferece um painel com informações úteis, comandos de voz e monitoramento de rede.

## 📜 Sobre o Projeto

Este é um script em Python que fornece um painel para exibir informações meteorológicas com base em uma cidade especificada, além de outras funcionalidades para auxiliar no dia a dia.

## ✨ Funcionalidades

O Termux Assistant oferece os seguintes recursos:

  * **Dashboard:** Exibe um painel com as seguintes informações:
      * **Clima:** Temperatura, umidade, e se é dia ou noite na sua cidade.
      * **Bateria:** Status, nível e ciclos da bateria do seu dispositivo.
      * **Frase do Dia:** Uma citação inspiradora para começar bem o seu dia.
  * **Comandos de Voz:** Permite que você adicione tarefas e lembretes usando a sua voz.
  * **Monitor de Rede Wi-Fi:** Verifica se você está conectado a uma rede Wi-Fi segura e o notifica.

## 🚀 Começando

Siga estas instruções para colocar o projeto em funcionamento no seu ambiente.

### Pré-requisitos

  * Termux
  * Python
  * termux-api

### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/williansilva51/termuxassistant.git
    ```
2.  Entre no diretório do projeto:
    ```bash
    cd termuxassistant
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Uso

O script principal é o `assistant.py`. Você pode usá-lo com as seguintes opções:

  * **Exibir o Dashboard:**
    ```bash
    python assistant.py --dashboard
    ```
  * **Iniciar a interface de comando de voz:**
    ```bash
    python assistant.py --voice
    ```
  * **Executar o monitor de rede Wi-Fi:**
    ```bash
    python assistant.py --wifi
    ```

Se nenhum argumento for fornecido, a ajuda será impressa.

## 🐳 Usando com Docker

Você também pode executar a aplicação usando o Docker.

1.  Construa a imagem do Docker:
    ```bash
    docker build -t termux-assistant .
    ```
2.  Execute o contêiner:
    ```bash
    docker run termux-assistant
    ```
    Por padrão, o comando `--dashboard` será executado. Você pode passar outros argumentos, como faria normalmente:
    ```bash
    docker run termux-assistant --voice
    ```

## ⚙️ Configuração

Você pode personalizar as configurações do assistente editando o arquivo `config.json`.

```json
{
  "city": "Quixadá",
  "secure_networks": [
    "WIFI_DE_CASA",
    "WIFI_DO_TRABALHO"
  ],
  "task_file": "/data/data/com.termux/files/home/task.txt"
}
```

  * `city`: A cidade padrão a ser usada se a localização não puder ser determinada.
  * `secure_networks`: Uma lista de nomes de redes Wi-Fi (SSIDs) que são consideradas seguras.
  * `task_file`: O caminho para o arquivo onde as tarefas serão salvas.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
