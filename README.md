# Prova P1 – Category com Serialização e Eventos de Domínio

Projeto desenvolvido para a disciplina de Engenharia de Software.

## 📋 Descrição
Implementação da entidade **Category** com:
- **Dataclasses** para simplificar a modelagem.
- Métodos de **serialização** (`to_dict` / `from_dict`).
- **Eventos de domínio** (Created, Updated, Activated, Deactivated).
- Testes demonstrando criação, atualização, ativação/desativação, serialização e registro de eventos.

## 📂 Estrutura do Projeto
projeto/
│
├─ domain/
│ ├─ category.py # Entidade Category (serialização + eventos)
│ └─ events/
│ └─ category_events.py # Classes de eventos de domínio
│
├─ test.py # Testes principais (serialização e eventos)
└─ test_events.py # Teste adicional de demonstração

perl
Copiar código

## ⚙️ Requisitos
- Python 3.8 ou superior

## ▶️ Como Executar
Na raiz do projeto:

python test.py
Esse comando cria categorias, demonstra serialização e exibe todos os eventos de domínio gerados.

🧩 Conceitos Utilizados
@staticmethod

Dataclasses

Eventos de Domínio

Decoradores

DDD (Domain-Driven Design)
