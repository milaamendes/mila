from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from pathlib import Path
from utils.analysis import calculate_clv, run_kmeans, prepare_campanha_data

app = FastAPI()
DATA_PATH = Path(__file__).resolve().parent.parent / "data"

@app.get("/api/analises/clv")
def clv():
    transacoes = pd.read_csv(DATA_PATH / "transacoes.csv")
    return JSONResponse(content=calculate_clv(transacoes))

@app.get("/api/analises/cluster")
def cluster():
    clientes = pd.read_csv(DATA_PATH / "clientes.csv")
    return JSONResponse(content=run_kmeans(clientes))

@app.get("/api/analises/campanhas")
def campanhas():
    campanhas = pd.read_csv(DATA_PATH / "campanhas.csv")
    return JSONResponse(content=prepare_campanha_data(campanhas))

