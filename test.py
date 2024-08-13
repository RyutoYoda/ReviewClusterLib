from ReviewClusterLib.preprocess import preprocess_text
from ReviewClusterLib.embedding import generate_embeddings
from ReviewClusterLib.clustering import cluster_reviews
from ReviewClusterLib.visualization import plot_clusters
from ReviewClusterLib.sentiment import analyze_sentiment
import pandas as pd

# Sample data
data = {
    "review_text": [
        "この製品は素晴らしいです！",
        "製品の品質が気に入りませんでした。",
        "驚くべきパフォーマンスと素晴らしいバッテリー寿命。",
        "製品はまあまあでしたが、特別なものではありませんでした。",
        "ひどい！もう一度買うことはありません。"
    ]
}

df = pd.DataFrame(data)

# Preprocess text
df['clean_text'] = df['review_text'].apply(preprocess_text)

# Generate embeddings
embeddings = generate_embeddings(df['clean_text'].tolist())

# Perform clustering
df['cluster'] = cluster_reviews(embeddings, num_clusters=3)

# Analyze sentiment
df['sentiment'] = df['clean_text'].apply(analyze_sentiment)

# Plot clusters
fig = plot_clusters(df, embeddings, num_clusters=3)
fig.show()
