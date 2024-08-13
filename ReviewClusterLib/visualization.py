import plotly.express as px
from .clustering import apply_pca

def plot_clusters(df, embeddings, num_clusters=5):
    pca_result = apply_pca(embeddings)
    df['pca_one'] = pca_result[:, 0]
    df['pca_two'] = pca_result[:, 1]
    df['pca_three'] = pca_result[:, 2]
    
    fig = px.scatter_3d(
        df, x='pca_one', y='pca_two', z='pca_three',
        color='cluster', hover_data=['clean_text'],
        color_discrete_sequence=px.colors.qualitative.T10[:num_clusters]
    )
    return fig
