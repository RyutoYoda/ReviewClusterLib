from snownlp import SnowNLP

def analyze_sentiment(text):
    """
    テキストの感情を分析し、ポジティブ・ネガティブスコアを返す関数。
    
    Parameters:
        text (str): 前処理されたテキストデータ
    
    Returns:
        float: 感情スコア (0: ネガティブ, 1: ポジティブ)
    """
    s = SnowNLP(text)
    return s.sentiments
