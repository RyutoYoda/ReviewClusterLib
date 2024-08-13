from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd

def cluster_reviews(embeddings, num_clusters=5):
    """
    埋め込みベクトルをクラスタリングする関数。
    
    Parameters:
        embeddings (numpy.ndarray): 埋め込みベクトル
        num_clusters (int): クラスタ数
    
    Returns:
        list: クラスタラベルのリスト
    """
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(embeddings)
    return clusters

def apply_pca(embeddings, n_components=3):
    """
    埋め込みベクトルにPCAを適用して次元を削減する関数。
    
    Parameters:
        embeddings (numpy.ndarray): 埋め込みベクトル
        n_components (int): 主成分数
    
    Returns:
        numpy.ndarray: 次元削減されたデータ
    """
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(embeddings)
    return pca_result
