import re

def preprocess_text(text):
    """
    テキストデータの前処理を行う関数。
    - 小文字に変換
    - 数字を削除
    - 不要な空白を削除
    - 特殊文字を削除
    
    Parameters:
        text (str): 元のテキストデータ
    
    Returns:
        str: 前処理されたテキストデータ
    """
    text = text.lower()  # 小文字に変換
    text = re.sub(r'\d+', '', text)  # 数字を削除
    text = re.sub(r'\s+', ' ', text)  # 不要な空白を削除
    text = re.sub(r'[^\w\s]', '', text)  # 特殊文字を削除
    return text
