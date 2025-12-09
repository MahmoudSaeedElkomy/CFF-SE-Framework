# 🛡️ Cognitive Fortress Framework: Sovereign Edition (CFF-SE v1.2)

> **A Deterministic Metacognitive Layer for LLM Governance & Alignment.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Powered by LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange)](https://langchain-ai.github.io/langgraph/)

## 📖 Overview
CFF-SE is not just another LLM prompt; it is a **software architecture** designed to solve the "Black Box" problem in Enterprise AI. It wraps your LLM (GPT-4, Claude, Llama 3) in a governance loop that enforces:
1.  **Contextual Permanence:** Prevents the AI from forgetting its instructions via **ALA (Anchor-Lock Agent)**.
2.  **Anti-Hallucination:** Forces a self-refutation step via **CFA (Counter-Factual Auditor)**.
3.  **Auditable Logs:** Every decision comes with a Governance Log (QCC Score, Drift Score).

## 🏗️ Architecture
The system operates as a **State Graph**:
```mermaid
graph LR
    Input --> Generator
    Generator --> Governance[MEO/CFA Audit]
    Governance -- "Reject (<95%)" --> Generator
    Governance -- "Pass" --> ALA[Drift Monitor]
    ALA -- "Drift (>5%)" --> Generator
    ALA -- "Stable" --> FCHA[Final Gate]
    FCHA --> Output
