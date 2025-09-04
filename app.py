from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "OK", "mensagem": "API funcionando"}

@app.get("/me")
def me():
    return {
        "nome": "Luan Diniz"
    }