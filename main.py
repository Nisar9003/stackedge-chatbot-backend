from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import voyageai
from pinecone import Pinecone
from groq import Groq
import os

app = FastAPI()

# CORS — WordPress se connect hone ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Clients
voyage = voyageai.Client(api_key=os.environ.get("VOYAGE_API_KEY"))
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index = pc.Index("stackedge-knowledge")
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

GROQ_API_KEYS = [
    os.environ.get("GROQ_API_KEY"),
    os.environ.get("GROQ_API_KEY_2"),
    os.environ.get("GROQ_API_KEY_3"),
    os.environ.get("GROQ_API_KEY_4"),
    os.environ.get("GROQ_API_KEY_5"),
]

current_key_index = 0

class ChatRequest(BaseModel):
    message: str
    history: list = []

def get_groq_client():
    global current_key_index
    keys = [k for k in GROQ_API_KEYS if k]
    return Groq(api_key=keys[current_key_index % len(keys)])

async def call_groq(messages, retries=0):
    global current_key_index
    keys = [k for k in GROQ_API_KEYS if k]
    if retries >= len(keys):
        raise Exception("All Groq keys exhausted")
    try:
        client = Groq(api_key=keys[current_key_index % len(keys)])
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=800,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        if "429" in str(e) or "rate_limit" in str(e):
            current_key_index += 1
            return await call_groq(messages, retries + 1)
        raise e

@app.get("/")
def root():
    return {"status": "Stack Edge Digital Chatbot Backend Running!"}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # 1. Voyage AI se question ka embedding banao
        embedding = voyage.embed(
            [req.message],
            model="voyage-large-2",
            input_type="query"
        ).embeddings[0]

        # 2. Pinecone se top 5 relevant chunks nikalo
        results = index.query(
            vector=embedding,
            top_k=5,
            include_metadata=True
        )

        # 3. Context banao retrieved chunks se
        context = "\n\n".join([
            match.metadata.get("text", "")
            for match in results.matches
            if match.score > 0.5
        ])

        # 4. System prompt
        system_prompt = f"""You are the official AI assistant for Stack Edge Digital — a premium digital agency. 
Answer questions using ONLY the context provided below. Be friendly, concise, and professional. 
Always respond in English only.
Do NOT add contact information unless directly asked.

IMPORTANT PORTFOLIO RULES:
- When asked about portfolio, first give brief platform overview, then ask which platform interests them
- Show MAX 2-3 projects at a time with name, description, and link
- Never dump all projects at once — keep it conversational
- Format projects as: **Project Name** — description — link
- End with: "Want to see more? Or explore another platform?"

CONTEXT:
{context}

If the context does not contain relevant information, politely say you don't have that information and suggest contacting Stack Edge Digital directly."""

        # 5. Messages banao history ke saath
        messages = [{"role": "system", "content": system_prompt}]
        
        # Last 4 messages history se
        for msg in req.history[-4:]:
            messages.append(msg)
        
        messages.append({"role": "user", "content": req.message})

        # 6. Groq se answer lo
        reply = await call_groq(messages)

        return {"reply": reply}

    except Exception as e:
        return {"reply": "Sorry, something went wrong. Please try again or contact contact@stackedgedigital.com", "error": str(e)}
