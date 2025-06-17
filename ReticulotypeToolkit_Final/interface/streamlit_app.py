import streamlit as st
import json
from core.Reticulotype_Core import ReticulotypeCore

# 配置路径
SYMPTOM_VOCAB_PATH = "config/symptom_vocab.json"
MECHANISM_GRAPH_PATH = "config/mechanism_graph.json"

# 加载机制图谱 & 词汇
with open(SYMPTOM_VOCAB_PATH, "r", encoding="utf-8") as f:
    symptom_vocab = json.load(f)
with open(MECHANISM_GRAPH_PATH, "r", encoding="utf-8") as f:
    mechanism_graph = json.load(f)

# 初始化模型
model = ReticulotypeCore(mechanism_graph, symptom_vocab)

st.set_page_config(layout="wide")
st.title("🧠 Reticulotype-IBS 药物推荐专家伙伴系统")
st.markdown("### 输入你的状态问卷（范围 0~7）：")

state = []
for symptom in symptom_vocab:
    score = st.slider(f"{symptom}", 0, 7, 3)
    state.append(score)

drug_candidates = list(mechanism_graph.keys())
symptom_focus = st.multiselect("选择你最关注的症状", options=symptom_vocab, default=symptom_vocab[:2])
patient_id = st.text_input("病人编号", value="demo001")

if st.button("🔍 生成推荐路径"):
    with st.spinner("推荐中..."):
        recommendation, decision, detail = model.recommend(
            patient_id, state, drug_candidates, symptom_focus
        )
        st.success(f"推荐结果: {recommendation}")
        st.info(f"系统判定: {decision}")
        if isinstance(detail, dict):
            st.json(detail)

        try:
            image_path = f"fsm_path_{patient_id}_{recommendation}.png"
            st.image(image_path, caption="机制路径图")
        except Exception:
            st.warning("机制图尚未生成。")