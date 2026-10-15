# Architecture — Day 1

The first milestone is a modular FastAPI application with a document upload endpoint.

- API layer: HTTP validation and responses.
- Schema layer: typed response contracts.
- Service layer: file persistence.

Later milestones add PostgreSQL metadata, Redis/Celery ingestion jobs, object storage, Qdrant, retrieval, evaluation and security. This starter **does not** process, embed, or index documents.
