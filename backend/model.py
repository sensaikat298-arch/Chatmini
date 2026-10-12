
import torch
import torch.nn as nn

class ChatminiModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim=64, hidden_dim=128):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.gru = nn.GRU(
            embedding_dim,
            hidden_dim,
            batch_first=True
        )
        self.output = nn.Linear(hidden_dim, vocab_size)

    def forward(self, tokens):
        x = self.embedding(tokens)
        x, _ = self.gru(x)
        return self.output(x)
