import heapq
class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.freq < other.freq
    def __eq__(self,other):
        return self.freq == other.freq


class HuffmanCoding:

    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__codes = {}

    def __make_frequency_dict(self,text):
        freq_dict ={}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1

        return freq_dict
    
    def __buildHeap(self,freq_dict):

        for key in freq_dict:
            frequency = freq_dict[key]
            binary_Tree = BinaryTreeNode(key,frequency)
            heapq.heappushpush(self.__heap,binary_Tree)

    def __buildTree(self):
        while (len(self.__heap) > 1):
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heapq.heappop(self.__heap)
            freq_sum = binary_tree_node_1.freq + binary_tree_node_2.freq
            new_node = BinaryTreeNode(None,freq_sum)
            new_node.left = binary_tree_node_1
            new_node.right = binary_tree_node_2
            heapq.heappush(self.__heap,new_node)
        return
    def __buildCodesHelper(self,root,curr_bits):
        if root is None:
            return
        
        if root.value is not None:
            self.__codes[root.value] = curr_bits
            return
        self.__buildCodesHelper(self,root.left,curr_bits+"0")
        self.__buildCodesHelper(self,root.right,curr_bits+"1")
        
    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")
    
    def __getEncodedText(self,text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text
    
    def __getPaddedEncodedText(self,encoded_text):

        padded_amount = 8 - (len(encoded_text)%8)

        for i in range(padded_amount):
            encoded_text += "0"
        
        padded_info = {"0:0.8b"}.format(padded_amount)
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text
    def __getBytesArray(self,padded_encoded_text):

        array = []
        for i in range(0,len(padded_encoded_text),8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte,2))
        return array


    def compress(self):
        # get file from the path 
        # read text from file 
        text = "lorem eoprk"

        # make frequency dictonary of the text
        freq_dict = self.__make_frequency_dict(text)


        # construct the heap from the frequency dict
        self.__buildHeap(freq_dict)

        # construct the binary tree from heap
        self.__buildTree()

        # construct the codes from the binary tree
        self.__buildCodes()


        # create the encoded text using the binary codes 
        encoded_text = self.__getEncodedText(text)

        # pad this encoded Text
        padded_encoded_text = self.__getPaddedEncodedText(encoded_text)

        bytes_array = self.__getBytesArray(padded_encoded_text)

        final_bytes = bytes(bytes_array)

        # put this encoded text into a binary file 

        #  return the binary file as a output
