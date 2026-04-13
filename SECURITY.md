# Política de Segurança

## Versões Suportadas

Atualmente, apenas a versão mais recente do Termux Assistant recebe atualizações de segurança.

| Versão | Suportada |
| :--- | :--- |
| 1.0.0 | ✅ Sim |
| < 1.0.0 | ❌ Não |

## Reportar uma Vulnerabilidade

A segurança do projeto e a privacidade dos utilizadores são prioridades. Se encontrar uma vulnerabilidade, por favor siga estes passos:

1. **Não abra um "Issue" público:** Para evitar a exploração da falha antes de existir uma correção, não publique detalhes técnicos publicamente.
2. **Contacto:** Envie um e-mail para o mantenedor (Willian Silva) ou utilize as ferramentas de reporte privado de segurança do GitHub, se disponíveis no repositório.
3. **Detalhes:** Inclua uma descrição da vulnerabilidade, os passos para a reproduzir e o potencial impacto.

## Considerações de Segurança do Projeto

### 1. Gestão de Dependências
O projeto utiliza o `uv` e o `Dependabot` para monitorizar e atualizar automaticamente as dependências. Recomendamos que:
* Mantenha o seu ambiente sempre atualizado executando `pip install -r requirements.txt` ou `uv sync` periodicamente.
* As principais bibliotecas externas incluem `requests` e `termux-api`.

### 2. Dados e Privacidade
O Termux Assistant acede a informações sensíveis para o seu funcionamento:
* **Localização:** Utilizada pelo módulo `dashboard.py` para obter dados meteorológicos via Termux API ou Nominatim.
* **Redes Wi-Fi:** O módulo `network_monitor.py` lê o SSID da sua rede para verificar se esta é segura, comparando-a com os dados em `config.json`.
* **Ficheiros Locais:** O assistente de voz escreve comandos num ficheiro de texto definido pelo utilizador (`task_file`).

**Nota:** Os dados de localização e redes são processados localmente ou enviados para APIs externas (como Open-Meteo e Nominatim) apenas para fins de consulta. O projeto não armazena estes dados em servidores externos próprios.

### 3. Utilização com Docker
Ao utilizar a imagem Docker fornecida, o processo corre sob um utilizador não-root (`appuser` ou `dev`) para limitar privilégios em caso de comprometimento do contentor.

## Boas Práticas para o Utilizador
* **Configuração:** Não partilhe o seu ficheiro `config.json` publicamente, especialmente se este contiver caminhos de ficheiros sensíveis ou nomes de redes privadas.
* **Permissões:** No Termux, conceda apenas as permissões necessárias para as funções que pretende utilizar (ex: localização, armazenamento).
