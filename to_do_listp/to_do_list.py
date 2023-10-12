class TDL:
    def __init__(self) -> None:
        self._list = []
        self._load()

    def create_task(self, title : str, task : str):
        self._list.append({'title': title, 'task': task})

    def show_list(self):
        for l in self._list:
            print(f"{l['title']}: {l['task']}")

    def update_task(self, position : int, new_title : str, new_task : str):
        try:
            self._list[position]['title'] = new_title
            self._list[position]['task'] = new_task
        
        except IndexError:
            print('List out of range')
            return False
        
    def remove_task(self, position):
        try:
            del self._list[position]
        
        except IndexError:
            print('List out of range')
            return False
        
    def save(self):
        import os
        import json

        PATH = os.path.join(os.path.dirname(__file__), "my_list.json")

        with open(PATH, 'w', encoding='utf8') as a:
            json.dump(self._list, a)

    def _load(self):
        import os
        import json

        NAME = 'my_list.json'

        if os.path.isfile(NAME):
            PATH = os.path.join(os.path.dirname(__file__), "my_list.json")
            with open(PATH, 'r') as a:
                self._list = json.load(a)
   

if __name__ == '__main__':
    tdl = TDL()

    tdl.create_task('Go to sleep', 'Make the bed, lie down and close your eyes')
    tdl.create_task('Take the dog to the park', 'Take the leash, put it on the dog and go to the park')
    tdl.create_task('Study', 'Pick up the notebook and pen, turn on the course and take notes')
    
    tdl.show_list()

    tdl.update_task(1, 'Go to the park', 'Get the keys, change and leave the house')
    tdl.remove_task(0)

    tdl.show_list()

    tdl.save()
