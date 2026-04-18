import streamlit as st
from openai import OpenAI

# 请替换成你自己的 DeepSeek API Key
DEEPSEEK_API_KEY = "sk-501194b49c724066a684ffcc6ac7b712"

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

st.title("AI 文案生成器")
product = st.text_input("输入产品名称")

if st.button("生成文案"):
    if product:
        with st.spinner("生成中..."):
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": f"为'{product}'写一句吸引人的广告词"}]
            )
            st.success(response.choices[0].message.content)
    else:
        st.warning("请输入产品名称")