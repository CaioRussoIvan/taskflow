
# 📋 TaskFlow — Sistema de Gerenciamento de Tarefas
> Projeto desenvolvido para a disciplina de Engenharia de Software — UniFECAF  
> Empresa fictícia: **TechFlow Solutions** | Cliente: Startup de Logística

---

## 🎯 Objetivo do Projeto

O **TaskFlow** é um sistema web de gerenciamento de tarefas desenvolvido com metodologia ágil para atender às necessidades de uma startup de logística. O sistema permite:

- Acompanhar o fluxo de trabalho em tempo real
- Criar, visualizar, atualizar e excluir tarefas (CRUD completo)
- Priorizar tarefas críticas
- Monitorar o status do desenvolvimento da equipe

---

## 📦 Escopo Inicial

O escopo inicial contempla as seguintes funcionalidades:

1. **Autenticação de usuários** — Login e logout com validação de credenciais
2. **Gerenciamento de tarefas (CRUD)** — Criar, listar, atualizar e excluir tarefas
3. **Priorização de tarefas** — Classificação por prioridade (Alta, Média, Baixa)
4. **Status de tarefas** — Controle de estado: A Fazer → Em Progresso → Concluído

---

## ⚙️ Metodologia Adotada

Este projeto utiliza o **Kanban** como metodologia ágil principal, gerenciado pela aba **GitHub Projects**.

### Por que Kanban?

- Fluxo contínuo de entrega, sem sprints fixas
- Visualização clara do trabalho em andamento (WIP)
- Fácil adaptação a mudanças de escopo
- Ideal para equipes pequenas com demandas variáveis

### Quadro Kanban (GitHub Projects)

| A Fazer | Em Progresso | Concluído |
|---------|--------------|-----------|
| Estrutura de diretórios | Implementação do CRUD | Configuração do repositório |
| Diagrama de Classes | Pipeline CI/CD | README inicial |
| Testes unitários | Sistema de login | ... |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.11 | Linguagem principal |
| Flask | Framework web |
| SQLite | Banco de dados local |
| Pytest | Testes automatizados |
| GitHub Actions | Pipeline CI/CD |
| GitHub Projects | Gestão ágil (Kanban) |

---

## 📁 Estrutura de Diretórios

```
taskflow/
├── src/
│   ├── app.py           # Aplicação Flask principal
│   ├── models.py        # Modelos de dados (Task, User)
│   ├── routes.py        # Rotas da API
│   └── auth.py          # Autenticação de usuários
├── tests/
│   ├── test_tasks.py    # Testes do CRUD de tarefas
│   └── test_auth.py     # Testes de autenticação
├── docs/
│   ├── diagrama_casos_de_uso.png
│   └── diagrama_classes.png
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline GitHub Actions
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar o Sistema

### Pré-requisitos

- Python 3.11+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/taskflow.git
cd taskflow

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python src/app.py
```

### Executar os Testes

```bash
pytest tests/ -v
```

---

## 🧪 Testes Automatizados

Os testes foram implementados com **Pytest** e cobrem:

- Criação de tarefa com dados válidos
- Leitura de lista de tarefas
- Atualização de status de tarefa
- Exclusão de tarefa
- Validação de login com credenciais corretas e incorretas

O pipeline de CI/CD (GitHub Actions) executa esses testes automaticamente a cada `push` ou `pull request` na branch `main`.

---

## 🔄 Gestão de Mudanças — Alteração de Escopo

### Mudança Realizada

**Nova funcionalidade adicionada:** *Filtro de tarefas por prioridade e responsável*

### Justificativa

Durante o desenvolvimento, o cliente (startup de logística) sinalizou que a equipe precisava filtrar tarefas por responsável e por nível de urgência para facilitar a triagem diária. Essa funcionalidade não estava no escopo original, mas foi incorporada pois agrega alto valor com baixo esforço de implementação.

### Impacto no Kanban

- ✅ Novo card criado: `feat: filtro por prioridade e responsável`
- ✅ Card movido de "A Fazer" → "Em Progresso"
- ✅ Commit registrado com a implementação

---

## 📌 Histórico de Commits (Semântico)

Os commits seguem o padrão **Conventional Commits**:

```
feat:     nova funcionalidade
fix:      correção de bug
docs:     atualização de documentação
test:     adição ou ajuste de testes
ci:       configuração de pipeline
refactor: refatoração sem mudança de comportamento
chore:    tarefas de manutenção
```

---

## 👤 Autor

Desenvolvido por Caio Vieira Mendes — Engenharia de Software — UniFECAF — 2025
