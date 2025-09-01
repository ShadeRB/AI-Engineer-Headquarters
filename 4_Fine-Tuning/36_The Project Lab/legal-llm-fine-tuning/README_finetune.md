Fine-tuning Legal LLM — Phase 2 Scaffold

This folder contains the scaffold for Phase 2: fine-tuning a Legal LLM on top of the data pipeline built in Phase 1.

The aim is to take clean legal text chunks and (optionally) labeled clauses, and fine-tune a base model (e.g., Mistral-7B-Instruct or Llama-3.1-8B-Instruct) using LoRA/QLoRA adapters.

📂 Project Layout
legal-llm-fine-tuning/
├─ configs/
│  ├─ sft_config.yaml        # training config
│  └─ eval_config.yaml       # evaluation config (stub)
├─ data/
│  └─ prepared/
│     ├─ train.jsonl         # tiny demo dataset
│     └─ eval.jsonl          # tiny demo eval set
├─ outputs/                  # model artifacts go here
├─ scripts/
│  ├─ prepare_data.py        # will turn processed text → JSONL (stub now)
│  ├─ train_sft.py           # stub for supervised fine-tuning (LoRA)
│  └─ eval_simple.py         # stub for evaluation
└─ README_finetune.md        # this file

🚀 Quickstart Steps
1. Activate environment
. ../../.venv/Scripts/activate   # adjust if your venv is elsewhere

2. Install libraries
pip install datasets peft trl transformers accelerate bitsandbytes

3. Prepare demo data

Small examples already live in data/prepared/train.jsonl and eval.jsonl.
Each row is one instruction-tuning sample:

{"instruction": "Answer the question using the contract text. Cite spans.", 
 "input": "TEXT: The agreement may be terminated by either party with 30 days notice.\nQUESTION: Does this contain a termination for convenience clause?", 
 "output": "Yes. Clause: 'The agreement may be terminated by either party with 30 days notice.' Citation: [§2.1]"}


👉 Add 5–10 rows per file for a smoke test. Later, prepare_data.py will auto-generate from data/processed/.

4. Adjust config

See configs/sft_config.yaml.
Key knobs: model name, batch size, learning rate, LoRA params.

5. Run training (stub)

Right now, this just prints the config path:

python scripts/train_sft.py --config configs/sft_config.yaml


Later this will launch supervised fine-tuning (SFT) with LoRA.

6. Run evaluation (stub)
python scripts/eval_simple.py --config configs/eval_config.yaml


Later this will compute metrics like:

Clause presence (yes/no accuracy)

Citation rate

Hallucination checks (citation must exist in input)

7. Check outputs

Trained adapters will appear in:

outputs/lora-legal/

🧩 How This Connects to the Pipeline

Phase 1: ingest.py → normalize.py → cleaned chunks in data/processed/

Phase 2: prepare_data.py → JSONL in data/prepared/ → LoRA fine-tuning

Phase 3: downstream app (RAG, API, or UI) for real-time legal Q&A

⚠️ Risks & Next Steps

Fine-tuning alone won’t guarantee correct citations → add RAG for grounding.

Add guardrails: PII redaction, bias checks, hallucination filters.

Grow dataset: from demo rows → thousands from CUAD / your legal PDFs.