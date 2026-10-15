# Enterprise RAG Platform

Architecture-first, interview-focused enterprise RAG project. This repository grows through small, reviewed milestones.

## Day 1 — FastAPI starter

This starter supports a health check and local PDF upload. **It does not yet queue background jobs, extract text, or index vectors.**

### Run (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs and test `POST /documents/upload`.

### Tests

```powershell
pytest -q
```

### Structure

- `app/api/`: HTTP endpoints
- `app/schemas/`: Pydantic response models
- `app/services/`: business logic and file storage
- `docs/`: architecture, decisions and progress

### Starter limitations

File type is checked by filename extension only; production needs content validation, auth, malware scanning, durable storage, structured errors, size limits at the gateway and observability. The service has a 20 MB limit but its `ValueError` is not yet translated into a client-friendly HTTP response.
