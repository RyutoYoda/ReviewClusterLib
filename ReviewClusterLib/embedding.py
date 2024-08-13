from sentence_transformers import SentenceTransformer

def generate_embeddings(text_list, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(text_list)
    return embeddings
