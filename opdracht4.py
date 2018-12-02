from csv import writer

def freq_table(file_name,trie):
    word_freq = dict()
    with open(file_name,'r') as file:
        for line in file:
            for word in line.split(sep=" "):
                word = word.strip("\n.\'\"\,;(){}\t\r\f\b\a\0")
                if word != "":
                    word = word.lower()
                    trie.insert(word)
                    if word in word_freq:
                        word_freq[word] += 1
                    else:
                        word_freq[word] = 1
    with open("table_using_dict.csv", "w", newline='') as file:
        file.write("SEP=,\n")
        csv = writer(file,delimiter=',')
        csv.writerow(["Word","freq"])
        for word in word_freq:
            csv.writerow([word,word_freq[word]])
            

class TrieNode:
    def __init__(self):
        self.n = 0
        self.d = dict()

    def insert(self,word,letter=1):
        if letter != len(word)+1:
            if word[:letter] not in self.d:
                self.d[word[:letter]] = TrieNode()
            if word[:letter] == word:
                self.d[word[:letter]].n += 1
            self.d[word[:letter]].insert(word,letter+1)

    def create_csv_file(self,writer,word=None):
        '''takes a CSV writer as parameter'''
        if self.n > 0:
            writer.writerow([word,self.n])
        if self.d:
            for node in self.d:
                self.d[node].create_csv_file(writer,node)

trie = TrieNode()
freq_table("test.txt",trie)

with open("table_using_trie.csv", "w", newline='') as file:
            file.write("SEP=,\n")
            csv = writer(file,delimiter=',')
            csv.writerow(["Word","freq"])
            trie.create_csv_file(csv)