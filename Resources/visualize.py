
# visualize.py

import matplotlib.pyplot as plt
import networkx as nx
import random

def visualize_graph(G):
    """
    Visualize the graph using matplotlib and networkx.
    This is a detailed visualization showing different node types with different colors.
    """
    # Create a networkx graph
    graph = nx.DiGraph()
    
    # Add nodes with different colors based on their type
    for node_key, node in G.graph.items():
        if isinstance(node, G.__class__.MainMenu):
            graph.add_node(node_key, color='skyblue', type='MainMenu')
        elif isinstance(node, G.__class__.EventCategory):
            graph.add_node(node_key, color='lightgreen', type='EventCategory')
        elif isinstance(node, G.__class__.EventNode):
            graph.add_node(node_key, color='salmon', type='EventNode')
        else:
            graph.add_node(node_key, color='gray', type='Other')
    
    # Add age nodes separately
    for node in G.agenodes:
        graph.add_node(node.key, color='gold', type='AgeNode')
    
    # Add edges
    for node_key, node in G.graph.items():
        for neighbor in node.neighbors:
            if hasattr(neighbor, 'key'):
                graph.add_edge(node_key, neighbor.key)
    
    # Add edges for age nodes
    for node in G.agenodes:
        for neighbor in node.neighbors:
            if hasattr(neighbor, 'key'):
                graph.add_edge(node.key, neighbor.key)
    
    # Get positions for nodes
    pos = nx.spring_layout(graph, seed=42)
    
    # Get node colors
    node_colors = [graph.nodes[node]['color'] for node in graph.nodes]
    
    # Draw the graph
    plt.figure(figsize=(12, 10))
    
    # Draw nodes
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, alpha=0.8, node_size=700)
    
    # Draw edges
    nx.draw_networkx_edges(graph, pos, edge_color='gray', arrows=True, arrowsize=15, width=1.5)
    
    # Draw labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight='bold')
    
    # Create a legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='skyblue', markersize=15, label='MainMenu'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=15, label='EventCategory'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='salmon', markersize=15, label='EventNode'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gold', markersize=15, label='AgeNode'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=15, label='Other')
    ]
    
    plt.legend(handles=legend_elements, loc='upper right')
    plt.title('Game Event Graph Visualization')
    plt.axis('off')
    
    # Save the figure
    plt.savefig('graph_visualization.png', dpi=300, bbox_inches='tight')
    plt.close()


def visualize_graph_simple(G):
    """
    A simpler visualization of the graph, as a fallback if the detailed one fails.
    """
    # Create a networkx graph
    graph = nx.DiGraph()
    
    # Add all nodes from the graph
    for node_key in G.graph:
        graph.add_node(node_key)
    
    # Add age nodes
    for node in G.agenodes:
        graph.add_node(node.key)
    
    # Add edges
    for node_key, node in G.graph.items():
        for neighbor in node.neighbors:
            if hasattr(neighbor, 'key'):
                graph.add_edge(node_key, neighbor.key)
    
    # Add edges for age nodes
    for node in G.agenodes:
        for neighbor in node.neighbors:
            if hasattr(neighbor, 'key'):
                graph.add_edge(node.key, neighbor.key)
    
    # Draw the graph
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=123)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', 
            node_size=600, font_size=10, font_weight='bold',
            arrows=True, arrowsize=10)
    
    plt.title('Simple Game Event Graph')
    plt.savefig('simple_graph_visualization.png', dpi=300, bbox_inches='tight')
    plt.close()
