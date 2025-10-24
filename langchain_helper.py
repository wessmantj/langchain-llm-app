from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv
import torch
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()

# Initialize the model once (will be reused)
_model = None
_llm = None

def get_llm(use_better_model=True):
    """
    Get or create the LLM instance (singleton pattern)
    
    Args:
        use_better_model: If True, use Phi-2 (better but slower). 
                         If False, use GPT-2 (faster but less capable)
    """
    global _model, _llm
    if _llm is None:
        if use_better_model:
            # Use Microsoft's Phi-2 - much better at following instructions
            model_name = "microsoft/phi-2"
            print(f"Loading {model_name}... (this may take a moment on first run)")
            
            tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float32,  # Use float32 for Mac compatibility
                device_map="auto",
                trust_remote_code=True
            )
            
            _model = pipeline(
                "text-generation",
                model=model,
                tokenizer=tokenizer,
                max_new_tokens=200,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                repetition_penalty=1.1
            )
        else:
            # Use GPT-2 (smaller, faster, but less capable)
            _model = pipeline(
                "text-generation", 
                model="openai-community/gpt2",
                max_new_tokens=200,
                temperature=0.8,
                do_sample=True,
                top_p=0.95,
                repetition_penalty=1.2
            )
        
        _llm = HuggingFacePipeline(pipeline=_model)
    return _llm

def generate_pet_name(animal_type, color=None, use_better_model=True):
    """
    Generate pet names based on animal type and optional color.
    
    Args:
        animal_type (str): Type of pet (e.g., 'dog', 'cat', 'bird')
        color (str, optional): Color of the pet
        use_better_model (bool): Use Phi-2 for better results (recommended)
    
    Returns:
        str: Generated pet names
    """
    llm = get_llm(use_better_model)
    
    # Create a clear instruction-style prompt
    if color:
        template = """Generate a list of 10 creative names for a {color} {animal_type}.

Names:
1."""
    else:
        template = """Generate a list of 10 creative names for a {animal_type}.

Names:
1."""
    
    if color:
        prompt_template = PromptTemplate(
            input_variables=['animal_type', 'color'],
            template=template
        )
        chain = prompt_template | llm
        response = chain.invoke({"animal_type": animal_type, "color": color})
    else:
        prompt_template = PromptTemplate(
            input_variables=['animal_type'],
            template=template
        )
        chain = prompt_template | llm
        response = chain.invoke({"animal_type": animal_type})
    
    return response

def langchain_agent():
    llm = get_llm(use_better_model=True)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    
    
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result =agent.run(
        "What is the average age of a dog? Miltiply the result by 3"
    )
    print(result)
