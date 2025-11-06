class CounterSepartor():
    def __init__(self,content:str=None):
        char=content
        self.words=char
        self.alphabet_list = [chr(i) for i in range(97, 123)]   #list of comma separated alphabets using ascii characters
        self._counts={}
        
  
    def m_Count(self):

        for i in self.words:
            for j in self.alphabet_list:
                if i.lower() == j:
                    self._counts[i]=self._counts.get(i,0) + 1
        self.res=self._counts.items()
        self.res1=self._counts
        return dict(sorted(self.res))
    

    def m_Keys(self):
        
        return list(sorted(self._counts))
    

    def m_Values(self):
       
       return list(sorted(self.res1.values()))



    
   


