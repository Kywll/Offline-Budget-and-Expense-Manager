import json
class Util():
    def search(self, object, data, target):
        for i in range(len(object)):
            if object[i][data] == target:
                return object[i]
        return None
        
    def delete(self, object, filename, root_key, id):
        item = self.search(object, "id", id)
        if item is None:
            print("Item not found.")
            return False
        object.remove(item)

        with open(filename, "w") as f:
            json.dump({root_key: object}, f, indent=4)


        return True

    def update(self, object, filename, root_key, data, new_data, id):
        item = self.search(object, "id", id)
        if item is None:
            print("Item not found.")
            return False
        
        if isinstance(object[0][data], bool):
            new_data = new_data.lower() == "true"
        elif isinstance(object[0][data], int):
            new_data = int(new_data)
        elif isinstance(object[0][data], float):
            new_data = float(new_data)

        item[data] = new_data

        with open(filename, "w") as f:
            json.dump({root_key: object}, f, indent=4)
        return True
    
    def most(self, object, data):
        most = object[0]
        for i in range(1, len(object)):
            if most[data] < object[i][data]:
                most = object[i]
        return most
    
    def filter(self, object, data, target):
        result = []
        for i in range(len(object)):
            if object[i][data] == target:
                result.append(object[i])
        return result


