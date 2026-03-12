FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

**File 2: `requirements.txt`**
```
fastapi
uvicorn
pinecone
voyageai
groq
python-dotenv
pydantic
httpx
