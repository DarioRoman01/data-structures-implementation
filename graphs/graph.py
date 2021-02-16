"""Graph implementation."""

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def get_paths(self, start, end, path=[]):
        """Get all the paths between the specified nodes."""
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict.keys():
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        
        return paths

    def get_short_path(self, start, end, path=[]):
        """Get the shortest path between the specified nodes."""
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict.keys():
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_short_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path