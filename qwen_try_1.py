from smolagents import LiteLLMModel
from smolagents import CodeAgent, HfApiModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    api_key="1122",
    num_ctx=8192,
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)

