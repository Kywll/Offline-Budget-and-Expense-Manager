class Util():


    def search(self, object, data, target):
        for i in range(len(object)):
            if object[i][data] == target:
                return object[i]
        return None
        
    def insert(self, object, data):
        object.append(data)
    def delete(self, object, data, target):
        object.remove(self.search(object, data, target))
    def update(self, object, data, new_data, target):
        self.search(object, data, target)[data] = new_data
    def sort(self):
        pass
    def filter(self, object, data, target):
        result = []
        for i in range(len(object)):
            if object[i][data] == target:
                result.append(object[i])
        return None
    def most(self, object, data):
        most = object[0]
        for i in range(1, len(object)):
            most = max(most[data], object[i][data])
        return most