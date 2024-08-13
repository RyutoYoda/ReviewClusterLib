from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def cluster_reviews(embeddings, num_clusters=5):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(embeddings)
    return clusters

def apply_pca(embeddings, n_components=3):
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(embeddings)
    return pca_result
