import streamlit as st
import langchain_helper as lch

# Page configuration
st.set_page_config(
    page_title="Pet Name Generator",
    page_icon="🐾",
    layout="centered"
)

# Title and description
st.title("🐾 Pet Name Generator")
st.markdown("Generate creative names for your pet using AI!")

# Sidebar for information
with st.sidebar:
    st.header("About")
    st.info(
        "This app uses AI language models and LangChain to generate "
        "creative pet names based on your pet's type and color."
    )
    
    st.markdown("---")
    st.header("Model Selection")
    use_better_model = st.radio(
        "Choose model:",
        options=[True, False],
        format_func=lambda x: "Phi-2 (Better quality, slower)" if x else "GPT-2 (Faster, lower quality)",
        index=0,
        help="Phi-2 generates better names but takes longer. GPT-2 is faster but may produce lower quality results."
    )
    
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("1. Select your pet type")
    st.markdown("2. Optionally add a color")
    st.markdown("3. Choose a model")
    st.markdown("4. Click 'Generate Names'")

# Main content
col1, col2 = st.columns(2)

with col1:
    animal_type = st.selectbox(
        "What type of pet do you have?",
        ("Dog", "Cat", "Bird", "Hamster", "Rabbit", "Fish", "Guinea Pig", "Turtle", "Snake", "Other"),
        index=0
    )

with col2:
    color = st.text_input(
        "What color is your pet? (optional)",
        placeholder="e.g., brown, white, black"
    )

# Generate button
if st.button("🎲 Generate Names", type="primary", use_container_width=True):
    if animal_type:
        loading_msg = "Generating creative names... 🤔" if use_better_model else "Generating names quickly... ⚡"
        with st.spinner(loading_msg):
            try:
                # Generate names
                animal_lower = animal_type.lower()
                if color and color.strip():
                    response = lch.generate_pet_name(animal_lower, color.lower(), use_better_model)
                else:
                    response = lch.generate_pet_name(animal_lower, use_better_model=use_better_model)
                
                # Display results
                st.success("Here are some name suggestions!")
                st.markdown("---")
                
                # Display the generated text
                st.markdown("### 🎯 Suggested Names:")
                st.write(response)
                
                # Add a tip
                if not use_better_model:
                    st.info("💡 Tip: Try the Phi-2 model for better quality names!")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please try again or contact support if the issue persists.")
    else:
        st.warning("Please select a pet type!")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Made with ❤️ using LangChain and Streamlit"
    "</div>",
    unsafe_allow_html=True
)
