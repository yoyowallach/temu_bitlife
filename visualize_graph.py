
# visualize_graph.py
from Resources.graphs import G
from Resources.visualize import visualize_graph, visualize_graph_simple

# Try the detailed visualization first
try:
    print("Generating detailed graph visualization...")
    visualize_graph(G)
except Exception as e:
    print(f"Detailed visualization failed: {e}")
    print("Using simplified visualization instead...")
    visualize_graph_simple(G)

print("Graph visualization complete! Check the output image files.")
