from heapq import heappush, heappop

class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, next):
        return self.frequency < next.frequency


def get_frequency_dict(s):
    freq_dict={}
    for c in s:
        if c in freq_dict:
            freq_dict[c]+=1
        else:
            freq_dict[c]=1
    return freq_dict


def build_huffman_tree(freq_dict):
    heap=[]
    for symbol, frequency in freq_dict.items():
        heappush(heap,(frequency,Node(frequency,symbol)))
    
    while len(heap)>1:
        freq1,node1=heappop(heap)
        freq2,node2=heappop(heap)
        #merging the two min nodes
        merged_node= Node(freq1+freq2,left=node1, right=node2)
        heappush(heap,(merged_node.frequency,merged_node))
    _,root= heappop(heap)
    return root


def traverse_tree(node, code_dict, code=""):
    #if the node is a leaf node
    if node.symbol:
        code_dict[node.symbol]=code
    #else it is a internal node and have 2 child
    else:
        traverse_tree(node.left, code_dict, code+"0")
        traverse_tree(node.right, code_dict, code+"1")


def Huffman(s):
    if not s:
        return "",{}
    #creating a frequency table
    freq_dict= get_frequency_dict(s)
    #getting the root node
    root= build_huffman_tree(freq_dict)
    code_dict={}
    traverse_tree(root,code_dict)
    encoded="".join(code_dict[c] for c in s)
    return code_dict


       
s = input()
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])