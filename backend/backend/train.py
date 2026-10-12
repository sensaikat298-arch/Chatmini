
from pathlib import Path
import torch
import torch.nn as nn
from model import ChatminiModel

torch.manual_seed(42)

data_path = Path("data/training.txt")
text = data_path.read_text(encoding="utf-8")

chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
encoded = torch.tensor([stoi[ch] for ch in text], dtype=torch.long)

if len(encoded) < 2:
    raise ValueError("Add more training text to data/training.txt")

model = ChatminiModel(vocab_size=len(chars))
optimizer = torch.optim.AdamW(model.parameters(), lr=0.003)

for step in range(300):
    inputs = encoded[:-1].unsqueeze(0)
    targets = encoded[1:].unsqueeze(0)

    logits = model(inputs)
    loss = nn.functional.cross_entropy(
        logits.reshape(-1, len(chars)),
        targets.reshape(-1)
    )

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: loss={loss.item():.4f}")

Path("backend/chatmini.pt").parent.mkdir(exist_ok=True)
torch.save(
    {
        "state_dict": model.state_dict(),
        "chars": chars,
        "embedding_dim": 64,
        "hidden_dim": 128,
    },
    "backend/chatmini.pt",
)
print("Chatmini training complete!")
