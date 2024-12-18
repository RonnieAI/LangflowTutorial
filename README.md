# Langflow API Integration

This repository demonstrates how to integrate and deploy Langflow workflows using Python APIs. It contains two main files:

## Files

### 1. `Goals_Flow.json`
This file represents the Langflow flow we created. It contains all the components, including the input fields for `profile`, `physical goals`, and `mental goals`, as well as the connections to the OpenAI API (e.g., GPT-4o Mini). The flow structure is saved in JSON format, which can be used for deploying and running the workflow via API.

### 2. `goals.py`
This Python script interacts with the Langflow API. It securely handles API keys using `dotenv` and allows you to call the Langflow flow defined in `Goals_Flow.json` via Python. The script makes the flow accessible programmatically and prints the results based on the input data provided. You can easily modify this script to deploy the flow on platforms like Streamlit or Gradio.

---

### How to Use
1. **Set up API Keys**  
   Store your Langflow and OpenAI API keys in a `.env` file for security.  
   
2. **Run the Python Script**  
   Use the `goals.py` script to access the flow and interact with it through the Python API.

3. **Deploy**  
   Deploy the flow on platforms like Streamlit or Gradio by integrating the Python API call into your application.
