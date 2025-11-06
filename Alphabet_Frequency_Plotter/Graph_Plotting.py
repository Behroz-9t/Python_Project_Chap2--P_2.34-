from Doc_Reader import DocumentReader
from Counter_V1 import CounterSepartor
import matplotlib.pyplot as plt


class GraphPlotter(DocumentReader):

    def __init__(self):
        # if self._content!=None:
        
        super().__init__() # super initiates the init of the DocReader
        
                
        self.reader()  #then the reader function is initiated
        if self._content!=[]:   #check for the empty _content attribute
           
            _trigger=CounterSepartor(self._content)  #instantiated CounterSeparatoe class ---> COMPOSITION
            
            self._count=_trigger.m_Count()    #calling of its functions 
            self._labels=_trigger.m_Keys()    #calling of its functions
            self._values=self._count.values() #calling of its functions

    def Plotter(self):

        if self._content!=[]:
            plt.figure(figsize=(8, 5))  #graph size
                    
            plt.bar(self._labels, self._values)  #plt library bar function takes labels and values from Counter_V1 class

            plt.title('Frequency of Alphabets')
            plt.xlabel('Alphabet')
            plt.ylabel('Count')


    def Show_Graph(self):
        if self._content!=[]:
            plt.show()   



