# Python3 program to find path between two 
# cell in matrix 
from collections import defaultdict 
class Graph: 
	def __init__(self): 
		self.graph = defaultdict(list) 
	
	# add edge to graph 
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	# BFS function to find path from source to sink	 
	def BFS(self, s, d): 
		
		# Base case 
		if s == d: 
			return True
			
		# Mark all the vertices as not visited 
		visited = [False]*(len(self.graph) + 1) 

		# Create a queue for BFS 
		queue = [] 
		queue.append(s) 

		# Mark the current node as visited and 
		# enqueue it 
		visited[s] = True
		while(queue): 

			# Dequeue a vertex from queue 
			s = queue.pop(0) 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent has 
			# not been visited, then mark it visited 
			# and enqueue it 
			for i in self.graph[s]: 
				
				# If this adjacent node is the destination 
				# node, then return true 
				if i == d: 
					return True

				# Else, continue to do BFS 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True

		# If BFS is complete without visiting d 
		return False

def isSafe(i, j, matrix): 
	if i >= 0 and i <= len(matrix) and j >= 0 and j <= len(matrix[0]): 
		return True
	else: 
		return False

# Returns true if there is a path from a source (a 
# cell with value 1) to a destination (a cell with 
# value 2) 
def findPath(M): 
	s, d = None, None # source and destination 
	N = len(M) 
	g = Graph() 

	# create graph with n * n node 
	# each cell consider as node 
	k = 1 # Number of current vertex 
	for i in range(N): 
		for j in range(N): 
			if (M[i][j] != 0): 

				# connect all 4 adjacent cell to 
				# current cell 
				if (isSafe(i, j + 1, M)): 
					g.addEdge(k, k + 1) 
				if (isSafe(i, j - 1, M)): 
					g.addEdge(k, k - 1) 
				if (isSafe(i + 1, j, M)): 
					g.addEdge(k, k + N) 
				if (isSafe(i - 1, j, M)): 
					g.addEdge(k, k - N) 
			
			if (M[i][j] == 1): 
				s = k 

			# destination index	 
			if (M[i][j] == 2): 
				d = k 
			k += 1

	# find path Using BFS 
	return g.BFS(s, d) 

# Driver code 
if __name__=='__main__': 
	M =[[0, 3, 1, 0], [3, 0, 3, 3], [2, 3, 3, 3], [0, 3, 3, 3]] 
	if findPath(M): 
		print("Yes") 
	else: 
		print("No") 

# This Code is Contributed by Vikash Kumar 37 
