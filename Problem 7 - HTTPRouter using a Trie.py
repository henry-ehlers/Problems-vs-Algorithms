class RouteTrie:

    def __init__(self, root_handler = None):

        assert isinstance(root_handler, str)

        # Define the RouteTrie's root handler name
        self.root_handler = root_handler

        # Instantiate the root node using the root handler
        self.root_node    = RouteTrieNode(handler = root_handler)

    def insert(self, sub_paths, handler = None):

        # Define the current node as the root node
        current_node = self.root_node

        # Iterate over all subpaths
        for sub_path in sub_paths:

            # Insert the current subpath in the current node's childenr
            current_node.insert(sub_path)

            # Update the current node
            current_node = current_node.children.get(sub_path, None)

        # Set the final node's handler to the provided value
        current_node.handler = handler

    def find(self, sub_paths):
        
        # Check whether the list of subpaths is only 1 long -> root
        if len(sub_paths) == 1:
            return self.root_node.handler

        # Set current node to the root
        current_node = self.root_node

        # Iterate over each path in the list of subpaths
        for sub_path in sub_paths:
            
            # Extract the next node using get (default: None)
            current_node = current_node.children.get(sub_path, None)

            # If the current node is none, nothing was found under path
            if current_node == None:
                return None

        # Return the handler of the last "current node"
        return current_node.handler

class RouteTrieNode:

    def __init__(self, handler = None):

        # Set the node's handler (if provided)
        self.handler = handler

        # Inintialize an empty dict. of its childenr
        self.children = {}

    def insert(self, sub_path):

        # Check that the subpath is not already in the list of childenr
        if sub_path not in self.children.keys():

            # Add child node
            self.children[sub_path] = RouteTrieNode()

class Router:
    def __init__(self, root_handler = None, not_found_handler = None):

        # Instantiate the routetry
        self.route_trie_thing  = RouteTrie(root_handler = root_handler)

        # Define the root handler
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler = None):

        # Ensure the provided path and handler (if provided) are of type string
        if isinstance(path, str) and (isinstance(handler, str) or handler == None):

            # Split the paths along '/'
            sub_paths = self.split_path(path)

            # Insert the new route with its final handler
            self.route_trie_thing.insert(sub_paths, handler)

    def lookup(self, path):

        # Ensure the Provided Path is actually of type string
        if not isinstance(path, str):
            return None
 
        # Split the paths along '/'
        sub_paths = self.split_path(path)

        # Lookup handler in routetrie object
        handler   = self.route_trie_thing.find(sub_paths)

        # Return either the found handler or the default "not found" handler
        return (handler if handler != None else self.not_found_handler)

    def split_path(self, path):

        # Intitialize an empty list of subpaths, and a current empty subpath
        sub_paths = []
        sub_path  = ""

        # Iterate over all charactrs in the path
        for index, character in enumerate(path):

            # If not the final index
            if index < (len(path) - 1): 
                
                # Check whether the chacter is "/" -> if not, add to current subpath
                if character != "/":
                    sub_path += character

                # -> If so, append the current subpath, and move on
                else:
                    sub_paths.append(sub_path)
                    sub_path = ""

            # If the final index
            else:

                # Check whether the chacter is "/" -> if not, add to current subpath
                if character != "/":
                    sub_path +=  character

                # Append the final  subpath
                sub_paths.append(sub_path)

        # Return
        return sub_paths

# create the router and add a route
router = Router(root_handler = "root handler", not_found_handler = "not found handler") 
router.add_handler("/home/about", "about handler") 

# Test Cases
print("Test Case #1 - should print 'root handler': " + "\t\t" +
    ("Pass" if "root handler" == router.lookup("/") else "Fail") )

print("Test Case #2 - should print 'not found handler': " + "\t" +
    ("Pass" if 'not found handler' == router.lookup("/home") else "Fail") )

print("Test Case #3 - should print 'about handler': " + "\t\t" +
    ("Pass" if "about handler" == router.lookup("/home/about") else "Fail") )

print("Test Case #4 - should print 'about handler': " + "\t\t" +
    ("Pass" if "about handler" == router.lookup("/home/about/") else "Fail") )

print("Test Case #5 - should print 'not found handler': " + "\t" +
    ("Pass" if 'not found handler' == router.lookup("/home/about/me") else "Fail") )
