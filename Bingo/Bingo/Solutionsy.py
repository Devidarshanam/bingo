
class ArrayListADT:
    def __init__(self):
        self.data=[]
        self.size=len(self.data)

    def add(self,integer):
        self.data.append(integer)
        self.size=len(self.data)
        return True
    
    def add_at(self,index,element):
        x=[]
        for i in range(len(self.data)):
            if i==index:
                x.append(element)
            x.append(self.data[i])
        if index==len(self.data):
            x.append(element)
        self.data=x
        self.size=len(self.data)

    def add_all_at(self,index,collection):
        y=[]
        for i in range(len(self.data)):
            if i!=index:
                y.append(self.data[i])
            if i==index:
                for j in collection:
                    y.append(j)
                y.append(self.data[i])
        self.data=y
        self.size=len(self.data)

    def add_all(self,collection):
        for i in collection:
            self.data.append(i)
        self.size=len(self.data)

    def clear(self):
        self.data=[]
        self.size=len(self.data)
    
    def contains(self,obj):
        for i in self.data:
            if i==obj:
                return True
        return False
    
    def ensure_capacity(self,minCapacity):
        z=[]
        if len(self.data)<minCapacity:
            for i in range(minCapacity+len(self.data)):
                if len(self.data)>i:
                    z.append(self.data[i])
                else:
                    z.append(None)
        self.data=z
        self.size=len(self.data)

    def get(self,index):
        self.trim_to_size()
        for i in range(len(self.data)):
            if i==index:
                return self.data[i]
        if index==len(self.data):
            return self.data[-1]
        self.size=len(self.data)

    def size_(self):
        return self.size
    
    def index_of(self,object):
        for i in range(len(self.data)):
            if self.data[i]==object:
                return i
        return -1
    
    def last_index_of(self,object):
        s=-1
        for i in range(len(self.data)):
            if self.data[i]==object:
                s=i
        if s!=-1:
            return s
        return -1
    
    def is_empty(self):
        if self.data==[]:
            return True
        return False
    
    def remove_at(self,index):
        s=-1
        for i in range(len(self.data)):
            if i==index:
                s=self.data[i]
                self.data.remove(self.data[i])
        return s
    
    def remove(self,object):
        for i in self.data:
            for i in self.data:
                if i==object:
                    self.data.remove(i)
                    return True
        return False
    
    def set(self,index,element):
        x=-1
        for i in range(len(self.data)):
            if i==index:
                x=self.data[i]
                self.data[i]=element
        return x
    
    def size(self):
        return len(self.data)
    
    def trim_to_size(self):
        s=[]
        for i in self.data:
            if i!=None:
                s.append(i)
            else:
                break
        self.data=s
        self.size=len(self.data)
                
    def __str__(self):
        return str(self.data)


