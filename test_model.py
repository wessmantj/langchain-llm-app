from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

# Test the model directly
model = pipeline(
    "text-generation", 
    model="openai-community/gpt2",
    max_new_tokens=150,
    temperature=0.7,
    do_sample=True,
    top_p=0.9
)

# Test different prompts
prompts = [
    "Here are 10 great dog names:\n1. Buddy\n2. Max\n3.",
    "Popular pet dog names include: Buddy, Max, Charlie, Cooper, Rocky, Bear, Duke, Zeus, Apollo,",
    "Good names for a brown dog: Max, Charlie, Bruno, Cooper, Bear"
]

print("Testing GPT-2 output:\n")
for i, prompt in enumerate(prompts, 1):
    print(f"=== Test {i} ===")
    print(f"Prompt: {prompt}")
    result = model(prompt, max_new_tokens=100)
    print(f"Output: {result[0]['generated_text']}\n")
