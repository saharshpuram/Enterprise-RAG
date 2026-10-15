# Architecture decisions

## ADR-001: Modular monolith first

**Decision:** Begin with one FastAPI service split into API, schema, and service modules.

**Why:** Easier to understand, test, and evolve in a ten-day interview-focused learning program.

**Trade-off:** Future high-volume ingestion can be separated into worker processes without prematurely splitting the API into microservices.
