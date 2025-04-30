import streamlit as st
import openai

st.set_page_config(page_title="GPT-4.1-mini QA", page_icon="🤖")

st.title("💬 GPT-4.1-mini 질문 응답기")

# API 키 입력 받기
api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

# 질문 입력 받기
question = st.text_input("❓ 궁금한 질문을 입력하세요:")

if st.button("질문하기"):
    if not api_key:
        st.warning("⚠️ 먼저 OpenAI API 키를 입력해주세요.")
    elif not question:
        st.warning("⚠️ 질문을 입력해주세요.")
    else:
        try:
            openai.api_key = api_key

            with st.spinner("GPT가 응답 중입니다..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4-1106-preview",  # GPT-4.1-mini 이름
                    messages=[
                        {"role": "system", "content": "당신은 유용한 AI 도우미입니다."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.7
                )
                answer = response.choices[0].message.content
                st.success("✅ GPT 응답:")
                st.write(answer)

        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")

