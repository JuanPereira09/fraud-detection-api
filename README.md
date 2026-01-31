# Fraud Detection API

API REST desenvolvida em Python para análise de risco de transações financeiras.

O objetivo do projeto é simular um serviço backend capaz de receber dados de uma transação, aplicar regras de negócio para classificação de risco e armazenar o histórico dessas análises em banco de dados.

---

## 🚀 Funcionalidades

- Análise de risco de transações financeiras
- Classificação de risco: LOW, MEDIUM ou HIGH
- Persistência de dados em banco SQLite
- Consulta do histórico de transações analisadas
- Documentação automática via Swagger

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:
git clone https://github.com/SEU_USUARIO/fraud-detection-api.git
cd fraud-detection-api
Crie e ative o ambiente virtual:

python -m venv venv
venv\Scripts\activate
Instale as dependências:

pip install -r requirements.txt
Execute a aplicação:

python -m uvicorn app.main:app --reload
Acesse a documentação interativa:

http://127.0.0.1:8000/docs
📌 Endpoints
POST /fraud/analyze
Analisa o risco de uma transação financeira.

Exemplo de requisição:

{
  "user_id": 1,
  "amount": 15000,
  "country": "US"
}
Exemplo de resposta:

{
  "id": 1,
  "user_id": 1,
  "amount": 15000,
  "country": "US",
  "risk": "HIGH",
  "reasons": [
    "High transaction amount",
    "International transaction"
  ]
}
GET /fraud/history
Retorna o histórico de todas as transações analisadas.

🧪 Cliente de Teste
O arquivo client.py simula um sistema externo consumindo a API, enviando requisições HTTP e exibindo as respostas no terminal.

📚 Objetivo do Projeto
Este projeto foi desenvolvido com foco em aprendizado e portfólio, abordando conceitos fundamentais de backend como:

APIs REST

Validação de dados

Regras de negócio

Persistência em banco de dados

Consumo de API via cliente HTTP

---

## 🟢 COMO USAR AGORA (bem direto)
1. No GitHub → **Add file → Create new file**
2. Nome: `README.md`
3. Cola **TUDO** isso
4. Commit
5. No seu PC:
```bash
git pull
