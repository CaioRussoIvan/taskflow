# src/app.py
# Sistema de Gerenciamento de Tarefas — TechFlow Solutions
# Disciplina: Engenharia de Software — UniFECAF

from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados em memória (simulação simples)
tasks = []
next_id = 1


def find_task(task_id):
    """Busca uma tarefa pelo ID."""
    return next((t for t in tasks if t["id"] == task_id), None)


# CREATE — Criar nova tarefa
@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()

    # Validação básica dos campos obrigatórios
    if not data or not data.get("title"):
        return jsonify({"error": "O campo 'title' é obrigatório"}), 400

    task = {
        "id": next_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "priority": data.get("priority", "Media"),  # Alta, Media, Baixa
        "status": "A Fazer",
        "responsible": data.get("responsible", "Não atribuído"),
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


# READ — Listar todas as tarefas
@app.route("/tasks", methods=["GET"])
def list_tasks():
    # Filtro opcional por prioridade (mudança de escopo)
    priority = request.args.get("priority")
    responsible = request.args.get("responsible")

    result = tasks
    if priority:
        result = [t for t in result if t["priority"] == priority]
    if responsible:
        result = [t for t in result if t["responsible"] == responsible]

    return jsonify(result), 200


# READ — Buscar tarefa por ID
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    return jsonify(task), 200


# UPDATE — Atualizar tarefa
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    data = request.get_json()
    valid_statuses = ["A Fazer", "Em Progresso", "Concluído"]

    # Atualiza apenas os campos enviados
    if "title" in data:
        task["title"] = data["title"]
    if "description" in data:
        task["description"] = data["description"]
    if "priority" in data:
        task["priority"] = data["priority"]
    if "responsible" in data:
        task["responsible"] = data["responsible"]
    if "status" in data:
        if data["status"] not in valid_statuses:
            return jsonify({"error": f"Status inválido. Use: {valid_statuses}"}), 400
        task["status"] = data["status"]

    return jsonify(task), 200


# DELETE — Excluir tarefa
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa excluída com sucesso"}), 200


if __name__ == "__main__":
    app.run(debug=True)
