# tests/test_tasks.py
# Testes unitários do CRUD de tarefas — TechFlow Solutions
# Executar com: pytest tests/ -v

import pytest
import sys
import os

# Adiciona o diretório src ao path para importar o app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import app, tasks


@pytest.fixture(autouse=True)
def limpar_tarefas():
    """Limpa a lista de tarefas e reseta o ID antes de cada teste."""
    import app as app_module
    app_module.tasks.clear()
    app_module.next_id = 1
    yield


@pytest.fixture
def client():
    """Cria um cliente de teste Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---- TESTES DE CRIAÇÃO (CREATE) ----

def test_criar_tarefa_valida(client):
    """Deve criar uma tarefa com dados válidos."""
    response = client.post("/tasks", json={
        "title": "Implementar login",
        "priority": "Alta",
        "responsible": "Ana"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Implementar login"
    assert data["priority"] == "Alta"
    assert data["status"] == "A Fazer"


def test_criar_tarefa_sem_titulo_retorna_erro(client):
    """Deve retornar erro 400 se o título estiver ausente."""
    response = client.post("/tasks", json={"description": "Sem título"})
    assert response.status_code == 400
    assert "error" in response.get_json()


# ---- TESTES DE LEITURA (READ) ----

def test_listar_tarefas_vazia(client):
    """Deve retornar lista vazia quando não há tarefas."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_listar_tarefas_com_dados(client):
    """Deve retornar todas as tarefas criadas."""
    client.post("/tasks", json={"title": "Tarefa 1"})
    client.post("/tasks", json={"title": "Tarefa 2"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_buscar_tarefa_por_id(client):
    """Deve retornar a tarefa correta pelo ID."""
    client.post("/tasks", json={"title": "Tarefa X"})
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.get_json()["title"] == "Tarefa X"


def test_buscar_tarefa_inexistente(client):
    """Deve retornar 404 para ID inexistente."""
    response = client.get("/tasks/999")
    assert response.status_code == 404


# ---- TESTES DE ATUALIZAÇÃO (UPDATE) ----

def test_atualizar_status_tarefa(client):
    """Deve atualizar o status de uma tarefa existente."""
    client.post("/tasks", json={"title": "Deploy"})
    response = client.put("/tasks/1", json={"status": "Em Progresso"})
    assert response.status_code == 200
    assert response.get_json()["status"] == "Em Progresso"


def test_atualizar_status_invalido(client):
    """Deve retornar erro para status inválido."""
    client.post("/tasks", json={"title": "Deploy"})
    response = client.put("/tasks/1", json={"status": "Inventado"})
    assert response.status_code == 400


# ---- TESTES DE EXCLUSÃO (DELETE) ----

def test_excluir_tarefa(client):
    """Deve excluir uma tarefa existente."""
    client.post("/tasks", json={"title": "Remover isso"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    # Confirma que foi removida
    assert client.get("/tasks/1").status_code == 404


def test_excluir_tarefa_inexistente(client):
    """Deve retornar 404 ao tentar excluir tarefa que não existe."""
    response = client.delete("/tasks/999")
    assert response.status_code == 404


# ---- TESTE DE FILTRO (MUDANÇA DE ESCOPO) ----

def test_filtrar_por_prioridade(client):
    """Deve retornar apenas tarefas com a prioridade solicitada."""
    client.post("/tasks", json={"title": "Urgente", "priority": "Alta"})
    client.post("/tasks", json={"title": "Normal", "priority": "Baixa"})
    response = client.get("/tasks?priority=Alta")
    result = response.get_json()
    assert len(result) == 1
    assert result[0]["priority"] == "Alta"
