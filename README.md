# SoundTrack-Map 🎵🌍
Link do video explicativo = https://youtu.be/yOjNDBxzmU0
**A memory, a sound.**

O SoundTrack-Map é uma aplicação web interativa que conecta música, fotografia, lugares e memórias pessoais.

A proposta é permitir que cada usuário registre momentos especiais associando uma música, uma imagem, uma localização geográfica e uma descrição. Essas lembranças são exibidas em um mapa-múndi interativo, transformando experiências pessoais em um arquivo musical e visual.

## ✨ Funcionalidades

- **Mapa interativo:** visualização das memórias em diferentes lugares do mundo.
- **Cadastro de usuários:** criação de contas individuais.
- **Autenticação:** sistema de login e controle de sessões.
- **Registro de memórias:** associação de músicas, fotografias, lugares e descrições.
- **Edição e exclusão:** gerenciamento das próprias memórias.
- **Memórias compartilhadas:** visualização das publicações de outros usuários.
- **Armazenamento de dados:** persistência das informações em banco de dados SQLite.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Lógica e funcionamento do sistema |
| Flask | Framework web e gerenciamento das rotas |
| SQLite | Banco de dados |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e identidade visual |
| JavaScript | Interatividade e manipulação do mapa |
| Leaflet | Biblioteca de mapas interativos |
| Jinja2 | Integração entre Python e HTML |
| Flask-WTF | Proteção CSRF dos formulários |

## 📁 Estrutura do projeto

```text
soundtrack/
│
├── app/
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   └── soundtrack_controller.py
│   │
│   ├── models/
│   │   ├── soundtrack_model.py
│   │   └── user_model.py
│   │
│   ├── views/
│   │   ├── adicionar.html
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── static/
│   │   ├── css/
│   │   └── img/
│   │
│   ├── db.py
│   ├── middleware.py
│   └── __init__.py
│
├── requirements.txt
├── run.py
└── soundtrack_map.db
```

## 🚀 Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Git instalado.
- Visual Studio Code (recomendado).

### 2. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd soundtrack
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
python run.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## 🔐 Segurança

O projeto conta com mecanismos de proteção, incluindo:

- Hash de senhas para armazenamento seguro.
- Controle de autenticação por sessões.
- Proteção de rotas para usuários autenticados.
- Verificação de propriedade antes da edição e exclusão de memórias.
- Proteção CSRF nos formulários.
- Validação de extensões e limite de tamanho para imagens enviadas.
- Configurações de segurança para cookies de sessão.

## 🎨 Proposta do projeto

O SoundTrack-Map parte da ideia de que músicas podem estar associadas a lugares, pessoas e momentos específicos.

Mais do que armazenar músicas, a aplicação busca construir um arquivo pessoal de experiências, no qual cada localização representa uma lembrança e cada lembrança possui sua própria trilha sonora.

**Every place has a soundtrack. Every memory has a story.**
