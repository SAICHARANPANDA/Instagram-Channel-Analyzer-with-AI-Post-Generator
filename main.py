from fastapi import FastAPI, HTTPException, Request
import time

# Use absolute imports instead of relative
import models
import utils
import ai

app = FastAPI(title="Instagram Channel Analyzer")

metrics = {"requests": {}, "latency": {}}


@app.middleware("http")
async def track_metrics(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    path = request.url.path
    metrics["requests"][path] = metrics["requests"].get(path, 0) + 1
    metrics["latency"][path] = duration
    return response


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def get_metrics():
    return metrics


@app.post("/collect-data")
def collect_data(payload: models.CollectRequest):
    try:
        utils.safe_write_json("data/channel_data.json", payload.dict())
        return {"status": "success", "file": "data/channel_data.json"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/summarize", response_model=models.SummaryResponse)
def summarize():
    data = utils.safe_read_json("data/channel_data.json")
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    summary = ai.generate_summary(data)
    return {"summary": summary}


@app.get("/recommend", response_model=models.RecommendResponse)
def recommend():
    data = utils.safe_read_json("data/channel_data.json")
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    recommendation = ai.generate_recommendation(data)
    return recommendation


# Entry point for running with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
