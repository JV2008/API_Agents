from google.adk.agents.llm_agent import Agent
import math

MAX_TOKENS = 200
TOKENS_ATUAIS = 0

# Calculadora Python para expressões matemáticas complexas

def executar_calculo_python(codigo: str) -> str:
    """
     Ferramenta matemática avançada.

    Resolve:
    - potências
    - raízes
    - trigonometria
    - frações
    - expressões matemáticas complexas

    Recebe apenas expressões matemáticas válidas.
    """
    
    global TOKENS_ATUAIS
    
    if TOKENS_ATUAIS > MAX_TOKENS:
        return "Limite de tokens excedido."
   
    try:
        ambiente_seguro = {
            "math": math,
            "__builtins__": {}
        }

        resultado = eval(codigo, ambiente_seguro)

        return str(resultado)

    except Exception as error:
        print(f"Erro detectado no Agente: {error}")
        
        # Transforma o erro em string para buscar o padrão
        error_msg = str(error)
        
        # Identifica se o erro foi na chamada da função
        if "MALFORMED_FUNCTION_CALL" in error_msg:
            # Se estiver usando FastAPI, mude para: return JSONResponse(...)
            # Se for Flask, mude para: return jsonify(...), 422
            return "Desculpe, tive um problema técnico ao processar esse comando. Pode tentar reescrever o pedido?"
        
        return f"Erro na execução do cálculo: {error_msg}"


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions and math calculations.',
    instruction='Answer user questions to the best of your knowledge. Use the executar_calculo_python tool for complex math calculations.',
    tools=[executar_calculo_python]
)
