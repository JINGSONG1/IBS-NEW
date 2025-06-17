#  ReticulotypeToolkit: Mechanism-Guided Personalized Drug Recommendation for IBS

This repository provides a complete end-to-end AI agent system for personalized IBS drug recommendation, combining symbolic FSM path control, reinforcement learning, explainability, and doctor-in-the-loop feedback.

---

##  Project Highlights

-  FSM-driven interpretable drug recommendation
-  Key–Lock matching for patient-state to mechanism alignment
-  Extractability score to prevent sticky/rebound drug paths
- Doctor feedback override system + memory replay
- Fully modular Python toolkit ready for deployment
- Nature Medicine-ready: from psychological questionnaire to FSM-path visualization

---

## 📁 Toolkit Structure

| Folder | Description |
|--------|-------------|
| `core/` | FSM-DQN training system with memory |
| `mechanism/` | KeyLock encoder, Extractability scorer, BuffGate |
| `feedback/` | Doctor override system & SecondMe memory |
| `validator/` | FSM path validity & insertion failure detection |
| `visual/` | FSM mechanism path visualizer |
| `interface/` | Streamlit or API interface (Web-Ready) |
| `config/` | Graph definitions and configuration files |

---

##  Getting Started

```bash
# Clone and setup
git clone https://github.com/yourname/ReticulotypeToolkit.git
cd ReticulotypeToolkit
pip install -r requirements.txt

# Run streamlit interface
streamlit run interface/streamlit_app.py

# Train model
python train.py
```

---

##  Example

- Input: Psychological scores, symptom vector
- Output: Recommended drug + Mechanism path graph
- Explanation: BuffGate decision + path explanation

![](demo/fsm_path_demo001_帕罗西汀.png)

---

##  Citation

If you use this toolkit in academic work, please cite:
> Reticulotype: A Symbolic FSM-Reinforced Agent for Personalized IBS Drug Recommendation (Under Submission)
