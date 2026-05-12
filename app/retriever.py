import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("app/vectorstore/shl.index")

with open("app/vectorstore/metadata.pkl", "rb") as f:

    metadata = pickle.load(f)


def retrieve(query, top_k=5):

    embedding = model.encode([query])

    embedding = np.array(embedding).astype("float32")

    distances, indices = index.search(embedding, top_k)

    results = []

    for idx in indices[0]:

        results.append(metadata[idx])

    return results