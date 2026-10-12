# Chatmini — your own AI, built from scratch

Chatmini is a learning-first starter project for building a small language model and a phone-friendly chat website with a ₹0 software budget.

## What is included

- `frontend/index.html`: responsive chat interface that works on phones and computers.
- `backend/app.py`: small API server and a safe demo chat mode.
- `backend/model.py`: a tiny character-level Transformer language model implemented with PyTorch.
- `backend/train.py`: trains the model from random initialization on the text in `data/training.txt`.
- `backend/requirements.txt`: Python dependencies.
- `data/training.txt`: tiny example training corpus to prove the pipeline works.

## Honest expectations

This is a first educational prototype, not a frontier chatbot. The sample corpus is far too small for useful general conversation. A character-level model trained on it may produce incoherent text. The first milestone is to prove that **we can train and load our own model**; then we can improve the dataset, tokenizer, architecture, and evaluation.

## Run the website in demo mode

Requires Python 3.10+.

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000` in a browser. The demo chat works without downloading a pretrained model.

## Train Chatmini's tiny model

From the project root:

```bash
pip install -r backend/requirements.txt
python backend/train.py --steps 500
```

This creates `backend/chatmini.pt`. Then set the environment variable and restart the server:

```bash
# macOS/Linux
CHATMINI_MODEL=backend/chatmini.pt uvicorn backend.app:app --reload

# Windows PowerShell
$env:CHATMINI_MODEL="backend/chatmini.pt"
uvicorn backend.app:app --reload
```

The trained character model is a learning demo and will not behave like an instruction-following assistant. The API uses it for a short continuation after a prompt; otherwise, it uses the demo response engine.

## Free training plan

1. Start with this local prototype.
2. Move the training step to Google Colab's free tier if a compatible GPU is available. Free availability and quotas vary.
3. Build a better, permissively licensed training corpus. Check each dataset's licence and terms before use.
4. Upgrade from character-level prediction to a subword tokenizer and a small decoder-only Transformer.
5. Evaluate the model on held-out examples before connecting it to the live site.
6. Deploy the frontend and backend only where current free-tier limits fit. Do not put private API keys in browser code.

## Safety and data handling

- The demo stores no chat history on the server.
- Do not enter passwords, bank details, or other sensitive information.
- Keep the model and API server behind appropriate limits before making it public.
- A public website needs abuse protection and rate limiting before launch.
