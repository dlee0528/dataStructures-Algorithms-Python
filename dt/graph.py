class Graph:
    def __init__(self,edges) -> None:
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("Graph Dict:", self.graph_dict)

    
    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = [] # paths: [[["Mumbai", "Paris", "Dubia", "New York"]]]

        for node in self.graph_dict[start]: # node: "New York"
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths: # p: ["Mumbai", "Paris", "Dubai", "New York"]
                    paths.append(p) 
                    
        return paths


    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None


        shortest_path = None # unknown

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        # return only a single shortest path
        return shortest_path
     



if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    # transform tuple to a better dt such as hash
    #d = {"Mumbai": {"Paris", "Dubai"}}

    start = "Mumbai"
    end = "New York"
    # {'Mumbai': ['Paris', 'Dubai'], 'Paris': ['Dubai', 'New York'], 'Dubai': ['New York'], 'New York': ['Toronto']}  
   
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start,end))
    
    
    start = "Paris"
    end = "New York"

    print(f"Shortest Path between {start} and {end}:", route_graph.get_shortest_path(start,end))