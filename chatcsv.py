import streamlit as st                                           # Develop web applications
from dotenv import load_dotenv                                   # Load environment variables into python environment
from langchain_community.chat_models import ChatOpenAI           # OpenAI GPT models
from langchain_groq import ChatGroq                              # Use Groq LLMS
from langchain_experimental.agents import create_csv_agent       # Create a CSV agent
from langchain.schema import SystemMessage, HumanMessage, AIMessage # Import the message schema
from streamlit_chat import message 

def main():
    load_dotenv()

    # Intialize LLMS
    # llm = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0) 
    llm = ChatGroq(model="llama3-8b-8192",temperature = 0)

    st.set_page_config(page_title="Chat CSV", page_iconcls=":speech_balloon:", layout="wide")

    st.title("Ask Questions From Your CSV")

    # Initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content="Hello! How can I help you?")]

    user_question = st.chat_input("Enter Your Question:")

    st.sidebar.title("Upload Your CSV File")
    csv_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if user_question is not None:  # Ensure user input is valid
        st.session_state.messages.append(HumanMessage(content=user_question))

        with st.spinner("Thinking..."):


            if csv_file:
                # Convert file to a readable format
                agent = create_csv_agent(llm, csv_file, verbose=True, allow_dangerous_code=True)
                response = agent.run(user_question)

                # Append AI response to message history
                st.session_state.messages.append(AIMessage(content=response))

        # Display message history
        for i, msg in enumerate(st.session_state.messages):
            if isinstance(msg, HumanMessage):
                message(msg.content, is_user=True, key=f"{i}_user")
            elif isinstance(msg, AIMessage):
                message(msg.content, is_user=False, key=f"{i}_ai")

if __name__ == '__main__':
    main()
