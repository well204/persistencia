from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import httpx

app = FastAPI()

BASE_URL = "http://127.0.0.1:8000"

alunos_pd = pd.DataFrame(
    {
        "nome": [str],
        "nota": [float]
    }
)

class Aluno(BaseModel):
    nome: str
    nota: float


@app.post("/alunos")
def adicionar_aluno(nome: str, nota: float):
    global alunos_pd
    aluno = alunos_pd.index[alunos_pd["nome"] == nome]
    if (not aluno.empty):
        novo_aluno = {
            "nota": nota
        }
    else: 
        novo_aluno = {
            "nome": nome,
            "nota": nota
         }
    
    alunos_pd = alunos_pd._append(novo_aluno, ignore_index = True)

    return {
            "mensagem": "Aluno criado com sucesso!",
            "aluno": novo_aluno
        }

@app.get("/alunos/{nome}")
def obter_nota(nome: str):
    global alunos_pd

    filter = alunos_pd["nome"] == nome
    aluno = alunos_pd[filter]
    
    if aluno.empty:
        raise HTTPException(status_code=404, detail=f"Aluno com o nome: {nome} não encontrado")
    return aluno.to_dict(orient="records")[0]



@app.get("/alunos")
def listar_alunos():
    return alunos_pd.to_dict(orient = "records")

def obter_nota_cliente(nome):
    resp = httpx.get(f"{BASE_URL}/alunos/{nome}")
    return resp.json()

def add_aluno_cliente(nome, nota):
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json= {"nome": nome, "nota": nota}
    )
    return resp

def listar_aluno_cliente():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print(resp.json())


if __name__=="__main__":
    adicionar_aluno("João", 8.9)
    listar_aluno_cliente()
    obter_nota_cliente("João")