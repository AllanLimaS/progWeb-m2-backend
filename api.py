# pip install fastapi
# pip install uvicorn
# pip install mysqlclient
# pip install mysql-connector-python
# python -m uvicorn api:app --reload

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()


# porta do servidor
porta = 3306

# Classe de modelo para o usuário
class Usuario(BaseModel):
    id: int
    nome: str
    senha: str
    data_nasc: str
    sexo: int
    cidade: str
    bairro: str
    insta: str
    email: str
    telefone: str
    foto: str
    nota: float

# Rota para criar um novo usuário
@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    try:
        conn = mysql.connector.connect(
        host="localhost",
        port=porta,
        user="root",
        password="",
        database="uniride"
        )

        cursor = conn.cursor()

        sql = "INSERT INTO usuario (nome, senha, data_nasc, sexo, cidade, bairro, insta, email, telefone, foto, nota) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            
            usuario.nome,
            usuario.senha,
            usuario.data_nasc,
            usuario.sexo,
            usuario.cidade,
            usuario.bairro,
            usuario.insta,
            usuario.email,
            usuario.telefone,
            usuario.foto,
            usuario.nota
        )

        cursor.execute(sql, values)
        conn.commit()

        usuario.id = cursor.lastrowid

        cursor.close()
        conn.close()

        return usuario
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para obter um usuário pelo ID
@app.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int):
    try:
        conn = mysql.connector.connect(
        host="localhost",
        port=porta,
        user="root",
        password="",
        database="uniride"
        )

        cursor = conn.cursor()

        sql = "SELECT * FROM usuario WHERE id = %s"
        values = (usuario_id,)

        cursor.execute(sql, values)
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        usuario = Usuario(
            id=row[0],
            nome=row[1],
            senha=row[2],
            data_nasc=row[3].strftime('%Y-%m-%d'),
            sexo=row[4],
            cidade=row[5],
            bairro=row[6],
            insta=row[7],
            email=row[8],
            telefone=row[9],
            foto=row[10],
            nota=row[11]
        )

        cursor.close()
        conn.close()

        return usuario
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para atualizar um usuário pelo ID
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: Usuario):
    try:
        conn = mysql.connector.connect(
        host="localhost",
        port=porta,
        user="root",
        password="",
        database="uniride"
        )

        cursor = conn.cursor()

        sql = "UPDATE usuario SET nome = %s, senha = %s, data_nasc = %s, sexo = %s, cidade = %s, bairro = %s, insta = %s, email = %s, telefone = %s, foto = %s, nota = %s WHERE id = %s"
        values = (
            usuario.nome,
            usuario.senha,
            usuario.data_nasc,
            usuario.sexo,
            usuario.cidade,
            usuario.bairro,
            usuario.insta,
            usuario.email,
            usuario.telefone,
            usuario.foto,
            usuario.nota,
            usuario_id
        )

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        usuario.id = usuario_id

        cursor.close()
        conn.close()

        return usuario
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para excluir um usuário pelo ID
@app.delete("/usuarios/{usuario_id}")
def excluir_usuario(usuario_id: int):
    try:
        conn = mysql.connector.connect(
        host="localhost",
        port=porta,
        user="root",
        password="",
        database="uniride"
        )

        cursor = conn.cursor()

        sql = "DELETE FROM usuario WHERE id = %s"
        values = (usuario_id,)

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        cursor.close()
        conn.close()

        return {"message": "Usuário excluído com sucesso"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")


# Classe de modelo para o motorista
class Motorista(BaseModel):
    id: int
    carro: str
    placa: str
    usuario_id: int

# Rota para criar um novo motorista
@app.post("/motoristas")
def criar_motorista(motorista: Motorista):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "INSERT INTO motorista (carro, placa, usuario_id) VALUES (%s, %s, %s)"
        values = (
            motorista.carro,
            motorista.placa,
            motorista.usuario_id
        )

        cursor.execute(sql, values)
        conn.commit()

        motorista.id = cursor.lastrowid

        cursor.close()
        conn.close()

        return motorista
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para obter um motorista pelo ID
@app.get("/motoristas/{motorista_id}")
def obter_motorista(motorista_id: int):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "SELECT * FROM motorista WHERE id = %s"
        values = (motorista_id,)

        cursor.execute(sql, values)
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail="Motorista não encontrado")

        motorista = Motorista(
            id=row[0],
            carro=row[1],
            placa=row[2],
            usuario_id=row[3]
        )

        cursor.close()
        conn.close()

        return motorista
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para atualizar um motorista pelo ID
@app.put("/motoristas/{motorista_id}")
def atualizar_motorista(motorista_id: int, motorista: Motorista):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "UPDATE motorista SET carro = %s, placa = %s, usuario_id = %s WHERE id = %s"
        values = (
            motorista.carro,
            motorista.placa,
            motorista.usuario_id,
            motorista_id
        )

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Motorista não encontrado")

        motorista.id = motorista_id

        cursor.close()
        conn.close()

        return motorista
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para excluir um motorista pelo ID
@app.delete("/motoristas/{motorista_id}")
def excluir_motorista(motorista_id: int):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "DELETE FROM motorista WHERE id = %s"
        values = (motorista_id,)

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Motorista não encontrado")

        cursor.close()
        conn.close()

        return {"message": "Motorista excluído com sucesso"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

from datetime import time

# Classe de modelo para a carona
class Carona(BaseModel):
    id: int
    cidade: str
    bairro: str
    obs: str
    horario: time
    dias: str
    motorista_id: int
    passageiro_id1: int
    passageiro_id2: int
    passageiro_id3: int
    passageiro_id4: int

# Rota para criar uma nova carona
@app.post("/caronas")
def criar_carona(carona: Carona):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "INSERT INTO carona (cidade, bairro, obs, horario, dias, motorista_id, passageiro_id1, passageiro_id2, passageiro_id3, passageiro_id4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            carona.cidade,
            carona.bairro,
            carona.obs,
            carona.horario,
            carona.dias,
            carona.motorista_id,
            carona.passageiro_id1,
            carona.passageiro_id2,
            carona.passageiro_id3,
            carona.passageiro_id4
        )

        cursor.execute(sql, values)
        conn.commit()

        carona.id = cursor.lastrowid

        cursor.close()
        conn.close()

        return carona
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para obter uma carona pelo ID
@app.get("/caronas/{carona_id}")
def obter_carona(carona_id: int):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "SELECT * FROM carona WHERE id = %s"
        values = (carona_id,)

        cursor.execute(sql, values)
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=404, detail="Carona não encontrada")

        print(row)
        carona = Carona(
            id=row[0],
            cidade=row[1],
            bairro=row[2],
            obs=row[3],
            horario=(datetime.datetime.min +row[4] ).time(),
            dias=row[5],
            motorista_id=row[6],
            passageiro_id1=row[7],
            passageiro_id2=row[8],
            passageiro_id3=row[9],
            passageiro_id4=row[10]
        )

        cursor.close()
        conn.close()

        return carona
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para atualizar uma carona pelo ID
@app.put("/caronas/{carona_id}")
def atualizar_carona(carona_id: int, carona: Carona):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "UPDATE carona SET cidade = %s, bairro = %s, obs = %s, horario = %s, dias = %s, motorista_id = %s, passageiro_id1 = %s, passageiro_id2 = %s, passageiro_id3 = %s, passageiro_id4 = %s WHERE id = %s"
        values = (
            carona.cidade,
            carona.bairro,
            carona.obs,
            carona.horario,
            carona.dias,
            carona.motorista_id,
            carona.passageiro_id1,
            carona.passageiro_id2,
            carona.passageiro_id3,
            carona.passageiro_id4,
            carona_id
        )

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Carona não encontrada")

        carona.id = carona_id

        cursor.close()
        conn.close()

        return carona
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")

# Rota para excluir uma carona pelo ID
@app.delete("/caronas/{carona_id}")
def excluir_carona(carona_id: int):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=porta,
            user="root",
            password="",
            database="uniride"
        )

        cursor = conn.cursor()

        sql = "DELETE FROM carona WHERE id = %s"
        values = (carona_id,)

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Carona não encontrada")

        cursor.close()
        conn.close()

        return {"message": "Carona excluída com sucesso"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro no banco de dados: {err}")
