# 🐾 Pet Name Generator

A simple web application that generates creative pet names using AI and LangChain.

## Features

- Generate creative pet names based on pet type
- Optional color parameter for more personalized names
- Two model options:
  - **Phi-2** (Microsoft): Better quality, more creative names (~2.7GB)
  - **GPT-2**: Faster but simpler results (~500MB)
- Clean and intuitive web interface
- Powered by Hugging Face models

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test the models** (optional but recommended):
   ```bash
   python test_generation.py
   ```

3. **Create a `.env` file** (optional - only needed if using Hugging Face Hub features):
   ```
   HUGGINGFACE_TOKEN=your_token_here
   ```

## Running the App

Run the Streamlit app with:

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Select your pet type from the dropdown
2. Optionally enter your pet's color
3. Choose which model to use (Phi-2 recommended for better results)
4. Click "Generate Names" to get AI-generated name suggestions

## Model Comparison

| Model | Quality | Speed | Size | Best For |
|-------|---------|-------|------|----------|
| Phi-2 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 2.7GB | Best quality names |
| GPT-2 | ⭐⭐ | ⭐⭐⭐⭐⭐ | 500MB | Quick testing |

## Project Structure

```
langchain-llm-app/
├── main.py                 # Streamlit web interface
├── langchain_helper.py     # LangChain logic and model initialization
├── test_generation.py      # Test script to verify models work
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (optional)
└── README.md              # This file
```

## Technologies Used

- **LangChain**: Framework for building LLM applications
- **Hugging Face Transformers**: AI models (Phi-2, GPT-2)
- **Streamlit**: Web application framework
- **PyTorch**: Deep learning backend

## Notes

- First run will download the selected model
- On Apple Silicon Macs, models will use MPS (Metal Performance Shaders) for faster inference
- Models run locally, no API key required
- Phi-2 is recommended for production use

## Troubleshooting

If names aren't generating properly:
1. Run `python test_generation.py` to test models directly
2. Try switching to Phi-2 model in the sidebar
3. Check that all dependencies are installed correctly
