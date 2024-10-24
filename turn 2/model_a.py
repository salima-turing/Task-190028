import unittest
import networkx as nx

class TestDataGraphIntegrity(unittest.TestCase):

	def setUp(self):
		# Create a sample data graph for testing
		self.graph = nx.Graph()
		self.graph.add_node(1, name="Product 1", price=10.0)
		self.graph.add_node(2, name="Product 2", price=15.0)
		self.graph.add_node(3, name="Product 3", price=8.0)
		self.graph.add_edge(1, 2, weight=0.5)
		self.graph.add_edge(1, 3, weight=0.8)

	def test_node_count(self):
		expected_node_count = 3
		actual_node_count = self.graph.number_of_nodes()
		self.assertEqual(actual_node_count, expected_node_count, "Node count mismatch in the data graph.")

	def test_edge_count(self):
		expected_edge_count = 2
		actual_edge_count = self.graph.number_of_edges()
		self.assertEqual(actual_edge_count, expected_edge_count, "Edge count mismatch in the data graph")

	def test_node_properties(self):
		node_1_data = self.graph.nodes[1]
		self.assertEqual(node_1_data["name"], "Product 1")
		self.assertEqual(node_1_data["price"], 10.0)

	def test_relationship_properties(self):
		edge_1_data = self.graph.edges[(1, 2)]
		self.assertEqual(edge_1_data["weight"], 0.5)

	def test_query_result(self):
		# Test a simple query to find nodes with a price greater than 12
		expected_nodes = [2]
		query_nodes = [node for node, data in self.graph.nodes(data=True) if data["price"] > 12]
		self.assertEqual(set(query_nodes), set(expected_nodes), "Query result mismatch")

if __name__ == '__main__':
	unittest.main()
