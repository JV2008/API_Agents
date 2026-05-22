function preencherExemplo(texto) {
    const input = document.getElementById("input");
    input.value = texto;
    input.focus();
}

function checarEnter(event) {
    if (event.key === "Enter") {
        enviar();
    }
}

async function enviar() {
    const input = document.getElementById("input");
    const mensagem = input.value.trim();
    if (!mensagem) return;

    // Limpa o input
    input.value = "";

    const chatMessages = document.getElementById("chat-messages");

    // Adiciona mensagem do usuário na tela
    const userDiv = document.createElement("div");
    userDiv.className = "message user-message";
    userDiv.innerText = mensagem;
    chatMessages.appendChild(userDiv);
    
    // Rolagem automática
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Adiciona indicador de digitando
    const typingDiv = document.createElement("div");
    typingDiv.className = "message agent-message typing-indicator";
    typingDiv.innerHTML = "<span></span><span></span><span></span>";
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
        const res = await fetch("http://localhost:8000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: mensagem })
        });

        const data = await res.json();
        
        // Remove indicador de digitando
        typingDiv.remove();

        // Adiciona mensagem do agente
        const agentDiv = document.createElement("div");
        agentDiv.className = "message agent-message";
        agentDiv.innerText = data.response;
        chatMessages.appendChild(agentDiv);
        
    } catch (error) {
        typingDiv.remove();
        const errorDiv = document.createElement("div");
        errorDiv.className = "message agent-message error-message";
        errorDiv.innerText = "Erro ao se conectar com o servidor.";
        chatMessages.appendChild(errorDiv);
    }

    // Rolagem automática final
    chatMessages.scrollTop = chatMessages.scrollHeight;
}