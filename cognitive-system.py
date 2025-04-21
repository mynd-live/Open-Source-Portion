import numpy as np
from collections import deque

class CognitiveNode:
    def __init__(self, node_type, processing_function=None):
        self.node_type = node_type
        self.processing_function = processing_function
        self.connections = []
        self.state = None
        self.activation_history = deque(maxlen=100)
        
    def connect_to(self, other_node, weight=1.0):
        self.connections.append((other_node, weight))
        
    def process(self, input_data):
        if self.processing_function:
            self.state = self.processing_function(input_data)
        else:
            self.state = input_data
        self.activation_history.append(self.state)
        return self.state

class AdaptiveCognitiveSystem:
    def __init__(self):
        self.processing_modules = {
            'perception': [],
            'reasoning': [],
            'memory': [],
            'emotion': []
        }
        self.node_network = {}
        self.initialize_network()
        
    def initialize_network(self):
        # Create root node
        self.root_node = CognitiveNode('root')
        
        # Create primary nodes for each module
        for module_type in self.processing_modules.keys():
            node = CognitiveNode(module_type)
            self.node_network[module_type] = node
            self.root_node.connect_to(node)
            
    def process_input(self, input_data, input_type):
        # Initial processing through root node
        processed_data = self.root_node.process(input_data)
        
        # Process through relevant module
        if input_type in self.node_network:
            module_node = self.node_network[input_type]
            processed_data = module_node.process(processed_data)
            
        return processed_data
    
    def self_modify(self):
        """
        Basic self-modification mechanism based on activation patterns
        """
        for module_type, node in self.node_network.items():
            if len(node.activation_history) > 0:
                # Analysis of activation patterns could trigger structural changes
                activation_mean = np.mean(list(node.activation_history))
                if activation_mean > 0.8:  # High activation threshold
                    # Create new sub-node for highly active modules
                    new_node = CognitiveNode(f"{module_type}_sub")
                    node.connect_to(new_node)
                    self.processing_modules[module_type].append(new_node)

    def get_network_structure(self):
        """
        Returns the current network structure for visualization
        """
        structure = {
            'nodes': [],
            'connections': []
        }
        
        # Add root node
        structure['nodes'].append({
            'id': 'root',
            'type': 'root'
        })
        
        # Add module nodes and their connections
        for module_type, node in self.node_network.items():
            structure['nodes'].append({
                'id': module_type,
                'type': module_type
            })
            structure['connections'].append({
                'source': 'root',
                'target': module_type
            })
            
        return structure
