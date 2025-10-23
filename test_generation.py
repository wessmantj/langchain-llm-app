"""
Simple test script to verify models are working
Run this before using the web app to test generation
"""

import langchain_helper as lch
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("Testing Pet Name Generator Models")
print("=" * 50)

# Test 1: GPT-2 (faster)
print("\n📝 Test 1: GPT-2 Model (Fast)")
print("-" * 50)
try:
    result = lch.generate_pet_name("dog", use_better_model=False)
    print("✅ Success!")
    print(f"Result:\n{result}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 2: Phi-2 (better quality)
print("\n📝 Test 2: Phi-2 Model (Better Quality)")
print("-" * 50)
print("Note: First run will download ~2.7GB model")
try:
    result = lch.generate_pet_name("cat", "orange", use_better_model=True)
    print("✅ Success!")
    print(f"Result:\n{result}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

print("=" * 50)
print("Testing Complete!")
print("=" * 50)
