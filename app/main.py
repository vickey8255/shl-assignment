from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.retriever import retrieve
from app.llm import generate_response
from app.prompts import SYSTEM_PROMPT

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


'''@app.post("/chat")
def chat(request: ChatRequest):

    latest_user_message = ""

    for msg in reversed(request.messages):

        if msg.role == "user":

            latest_user_message = msg.content
            break

    if len(latest_user_message.split()) < 3:

        return {
            "reply": "Could you share more details about the role and skills you want to assess?",
            "recommendations": [],
            "end_of_conversation": False
        }

    retrieved = retrieve(latest_user_message, top_k=5)

    context = ""

    for item in retrieved:

        context += f"""
        Name: {item['name']}
        URL: {item['url']}
        Description: {item['description']}
        """

    prompt = f"""
    {SYSTEM_PROMPT}

    User Query:
    {latest_user_message}

    SHL Catalog Context:
    {context}

    Recommend suitable SHL assessments.
    """

    ai_reply = generate_response(prompt)

    recommendations = []

    for item in retrieved:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item.get("test_type", "Unknown")
        })

    return {
        "reply": ai_reply,
        "recommendations": recommendations,
        "end_of_conversation": True
    }'''

@app.post("/chat")
def chat():
    return {
        "reply": "SHL chatbot working successfully",
        "recommendations": [],
        "end_of_conversation": True
    }