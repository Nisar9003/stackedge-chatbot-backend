FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
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
