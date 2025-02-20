# AI Agent For Analyse CSV File

This repository contains the code how to create a Simple AI Agent using  langchain_experimental.agents, Python, streamlit, LangChain and LLM models with Open AI and Llama

## Steps Should Follow

create Virtual env

  ```
  python -m venv <Environment_Name>
  ```

activate Virtual env

  ```
  cd <Environment_Name>\Scripts\activate
  ```

creating .gitignore file , .env file , requirements.txt and python File

  ```
  echo "# Files to ignore" > .gitignore && echo "OPENAI_API_KEY=your_api_key_here" && echo "GROQ_API_KEY=your_api_key_here" > .env && echo "# python script" > <Python_File>
  ```

Here i used LangSmith which is the part of lanchain and it can be used for monitor the our built AI models also we can make dashboard as well. For that you need to setup follows in .env file

  ```
  LANGSMITH_TRACING = true
  LANGSMITH_ENDPOINT = https://api.smith.langchain.com
  LANGSMITH_API_KEY = <LangSmith_API_Key>
  LANGSMITH_PROJECT = <Project_Name>
  ```

Insatalling Required dependencies

  ```
  pip install -r requirements.txt
  ```

Run python file

  ```
  streamlit run <Python_File>
  ```

## Key Notes
- This project is a simple implementation of usage of AI Agent.
- The AI models used are OpenAI’s model and Llama, with the temperature variable set to 0 to prevent randomness.
- The AI Agent takes input from the user-submitted CSV file and the user's question.
- Based on the user's question, the AI Agent generates Python code and executes it.
- Finally, it provides the results as a response
- Additionally, by enabling verbose=True during AI Agent development, we can see how the AI Agent makes decisions.

---

## AIM of this project
- Even if the user has no knowledge of Python, they should still have the ability to analyze the data in the CSV file.
  
---

## Linkedin Profile

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Isuru%20Madhushan-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/isuru-madhushan-096878273/)


---

Feel free to contribute or report any issues you encounter. Let's build smarter AI together!

#AI_Agent #LLMS #Streamlit #Python #LangChain #LangSmith
