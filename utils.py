class Util():


    def search(self, object, data, target):
        for i in range(len(object)):
            if object[i][data] == target:
                return object[i][data]
        return None
        
    def insert(self, object, data):
        object.append(data)
    def delete(self):
        pass
    def update(self, object, data, new_data, target):
        self.search(object, data, target) = new_data
    def sort(self):
        pass

