# Instagram Channel Analyzer

## Setup

```bash
cd instagram-analyzer
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn backend.main:app --reload --port 8000
```

Open API docs: http://127.0.0.1:8000/docs

## Run Frontend

```bash
streamlit run frontend/app.py
```

UI: http://localhost:8501
