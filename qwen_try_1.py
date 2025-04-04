from smolagents import LiteLLMModel, DuckDuckGoSearchTool
from smolagents import CodeAgent, HfApiModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    api_key="1122",
    num_ctx=8192,
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model, add_base_tools=True)

agent.run(
    "How many seconds would it take for a leopard at full speed to run through Pont des Arts?",
)

