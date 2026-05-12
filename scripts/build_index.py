import json
import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("app/catalog.json", "r", encoding="utf-8") as f:

    catalog = json.load(f)

texts = []

for item in catalog:

    text = f"{item['name']} {item['description']}"
    texts.append(text)

embeddings = model.encode(texts)

embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])

index.add(embeddings)

faiss.write_index(index, "app/vectorstore/shl.index")

with open("app/vectorstore/metadata.pkl", "wb") as f:

    pickle.dump(catalog, f)

print("FAISS index built successfully")