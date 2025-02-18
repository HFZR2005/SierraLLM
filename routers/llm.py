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


generate_scenario_prompt = """Your task is to generate scenarios for an investigative interviewer to imagine themselves within. The interviewer primarily works with abused children (including sexual), up to age 18. Please generate a scenario of the form: Scenario: [Scenario] Age: [age]. The scenario should be short, include no dialogue and only have a few details. The setting is a court, so the scenario should just be some brief information about evidence. Also include the name and age of the child as separate fields.

Here is an example: 

Scenario: A six-year-old girl named Emily is brought to testify in court regarding allegations of physical abuse. The interviewer is provided with photographs and drawings made by Emily, depicting unexplained bruises and injuries on her body. There are also medical reports detailing multiple fractures, some healing and others still active. A worn teddy bear, belonging to Emily, has been collected as evidence from the home and shows signs of being used as a weapon. The courtroom is filled with tension as Emily bravely faces her accused abuser in the witness box

Name: Emily
Age: 6
    """


# Invoke chain
# chain.invoke({"question": generate_scenario_prompt})


def generate_scenario():
    output = chain.invoke({"question": generate_scenario_prompt})
    return output
