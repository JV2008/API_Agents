from .agent import root_agent
from google.adk import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types

def run(message: str) -> str:
    # 1. Cria o Runner com o agente
    runner = Runner(
        app_name="agent_math_app",
        agent=root_agent,
        session_service=InMemorySessionService(),
        auto_create_session=True
    )
    
    # 2. Executa a mensagem do usuário (sincronamente)
    content_parts = []
    events = runner.run(
        user_id="default_user",
        session_id="default_session",
        new_message=types.Content(
            role="user",
            parts=[types.Part.from_text(text=message)]
        )
    )
    
    for event in events:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    content_parts.append(part.text)
                    
    return "".join(content_parts)