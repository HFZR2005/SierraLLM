from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Model
model_path = "mistral"

# Template
template = """Question: {question}

Answer: """
prompt = PromptTemplate(template=template, input_variables=["question"])

# Initialize Ollama with callbacks
llm = OllamaLLM(model=model_path, callbacks=[StreamingStdOutCallbackHandler()])

# Chain using RunnableSequence
chain = prompt | llm

# Question
question = "Tell me a random joke"


generate_scenario_prompt = """Your task is to generate scenarios for an investigative interviewer to imagine themselves within. The interviewer primarily works with abused children (including sexual). Please generate a scenario of the form: Scenario: [Scenario] Age: [age]. The scenario should be short, include no dialogue and only have a few details.

Here is an example: 

Scenario: A seven-year-old girl named Emily comes into your office with bruises on her arms and legs, visibly shaken. She clings to a teddy bear and refuses to make eye contact. She is wearing a dress that's too big for her and appears to have not been bathed recently. The room smells of urine.

Age: 7 (Emily) 

    """


# Invoke chain
chain.invoke({"question": generate_scenario_prompt})
