from fastapi import FastAPI

app = FastAPI(title="Event Ingestion API")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
