from functools import reduce
V = [1,2,3,4,5,6]
E = [ [1,2],[1,3],[2,4], [3,5] ]

def parents_old(vertices): 
	acc = []
	for e in E:
		if e[1] in vertices:
			acc.append(e[0])
	return acc


def parent(v, e):
	return reduce(lambda a,b: a + [b[0]] if b[1] in v else a, e, [])

def children(v,e):
	return reduce(lambda a,b: a + [b[1]] if b[0] in v else a, e, [])




class Vertex():
	def __init__(self, _id = False):
		self._id = _id
		self._out = set() 
		self._in = set()
	def __str__(self):
		return str([self._id, list(self._in), list(self._out)])

class Edge():
	def __init__(self, source = None, target = None):
		self.source = source
		self.target = target
		self.s_ptr = None
		self.t_ptr = None
	
	def __str__(self):
		return str([self.source, self.target])


class D_graph():
	def __init__(self, V = [], E = []):
		self.edges = [] 
		self.vertices = [] 




		self.vertexIndex = {}
		
		self.autoid = 0
		self.addVertices(V)
		self.addEdges(E)

	
	def addVertices(self, V):
		for v in V:
			self.addVertex(v)


	def addVertex(self, v):
		if not v._id:
			v._id = self.new_id()
		else: 
			if v._id in self.vertexIndex:
				print("Vertex with id " + v._id + " already exists")
				return
		self.vertices.append(v)
		self.vertexIndex[v._id] = v
		v._out = set()
		v._in = set()


	def addEdges(self, E):
		for e in E:
			self.addEdge(e)

	def addEdge(self, e):
		if e.source not in self.vertexIndex: print(e.source + "of edge " + e + " not in vertex list")
		if e.target not in self.vertexIndex: print(e.target + "of edge " + e + " not in vertex list")
		
		e.t_ptr = self.vertexIndex[e.target]
		e.s_ptr = self.vertexIndex[e.source]

		self.vertexIndex[e.source]._out.add(e.target)
		self.vertexIndex[e.target]._in.add(e.source)
		self.edges.append(e)

	def new_id(self):
		self.autoid += 1
		return self.autoid

	def __str__(self):
		out = [str(v) for v in self.vertexIndex.values()]
		return "\n".join(out)

	def v(self, args):
		query = Query(self)
		query.add('vertex', *args])
		return query
#Query system

Q = {}

class Query():
	def __init__(self, graph):
		self.graph = graph
		self.state = []
		self.program = []
		self.gremlins = []

	def add(self, pipetype, args):
		step = (pipetype, args)
		self.program.append(step)
		return self

	def __str__(self):
		return str([self.state, self.program])

Pipetypes = {}
def addPipetype(name, fun):
	Pipetypes[name] = fun
	def q_fun(query, args):
		return query.add(name,*args)


#run this part
v_test = [Vertex(),Vertex(), Vertex()]
e_test = [Edge(1,2),Edge(1,3),Edge(3,1),Edge(3,2)]
g = D_graph(v_test, e_test)
print(g)

q_test = Query(g)
q_test.add("hello:","pipelines")
print(q_test)
