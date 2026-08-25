from fastapi import FastAPI

app = FastAPI(title="api-mock")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
