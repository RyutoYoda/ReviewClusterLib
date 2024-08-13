from sentence_transformers import SentenceTransformer

def generate_embeddings(text_list, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    テキストリストから埋め込みベクトルを生成する関数。
    
    Parameters:
        text_list (list): テキストデータのリスト
        model_name (str): 使用するSentenceTransformerモデルの名前
    
    Returns:
        numpy.ndarray: 埋め込みベクトルのリスト
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(text_list)
    return embeddings
