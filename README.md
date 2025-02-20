# AI Agent For Analyse CSV File

This repository contains the code how to create a Simple AI Agent using  langchain_experimental.agents  Python, streamlit, LangChain and LLM models with Open AI and Llama

## Steps Should Follow

create Virtual env

  ```
  python -m venv <environment_name>
  ```

activate Virtual env

  ```
  cd <environment_name>\Scripts\activate
  ```

creating .gitignore file , .env file , requirements.txt and python File

  ```
  echo "# Files to ignore" > .gitignore && echo "OPENAI_API_KEY=your_api_key_here" && echo "GROQ_API_KEY=your_api_key_here" > .env && echo "# python script" > <python File>
  ```

Here i used LangSmith which is the part of lanchain and it can be used for monitor the our built AI models also we can make dashboard as well. For that you need to setup follows in .env file

  ```
  LANGSMITH_TRACING = true
  LANGSMITH_ENDPOINT = https://api.smith.langchain.com
  LANGSMITH_API_KEY = <LangSmith API Key>
  LANGSMITH_PROJECT = <Project Name>
  ```

Insatalling Required dependencies

  ```
  pip install -r requirements.txt
  ```



