import streamlit as st
import pandas as pd
import altair as alt

# CSV 파일 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 페이지 제목
st.title("🌍 MBTI 유형별 비율이 높은 국가 Top 10")

# MBTI 유형 리스트
mbti_types = [
    "INFJ", "ISFJ", "INTP", "ISFP",
    "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP",
    "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

# 사용자가 선택할 MBTI 유형
selected_type = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

# 해당 MBTI 유형 비율 기준 Top 10 국가 추출
top10 = df[['Country', selected_type]].sort_values(by=selected_type, ascending=False).head(10)

# Altair 막대 그래프 생성
chart = alt.Chart(top10).mark_bar().encode(
    x=alt.X(selected_type, title="비율", scale=alt.Scale(domain=[0, top10[selected_type].max()*1.1])),
    y=alt.Y('Country', sort='-x', title="국가"),
    tooltip=['Country', selected_type]
).properties(
    title=f"{selected_type} 유형 비율이 높은 국가 Top 10",
    width=600,
    height=400
)

# 그래프 출력
st.altair_chart(chart, use_container_width=True)
