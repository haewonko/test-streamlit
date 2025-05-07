import streamlit as st
import openai

st.set_page_config(page_title="GPT-4.1-mini Chat", layout="centered")

st.title("💬 GPT-4.1-mini Chat")

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

api_key_input = st.text_input("Enter your OpenAI API key", type="password", value=st.session_state.api_key)
st.session_state.api_key = api_key_input

user_question = st.text_input("질문을 입력하세요:")

@st.cache_data(show_spinner=False)
def get_gpt_response(api_key: str, user_input: str) -> str:
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()

if st.button("답변 받기"):
    if not st.session_state.api_key:
        st.error("❗ OpenAI API 키를 입력하세요.")
    elif not user_question:
        st.warning("❗ 질문을 입력하세요.")
    else:
        with st.spinner("GPT-4.1-mini가 응답 중..."):
            try:
                answer = get_gpt_response(st.session_state.api_key, user_question)
                st.success("✅ GPT 응답:")
                st.write(answer)
            except Exception as e:
                st.error(f"API 요청 중 오류 발생: {e}")
