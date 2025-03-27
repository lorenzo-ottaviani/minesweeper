import time

class Timer:
    def __init__(self, label):
        self.label = label
        self.running = False
        self.start_time = None
        
    def start(self):
        self.running = True
        self.start_time = time.time()
    
    def update(self):
        if self.running:
            timer = time.time() - self.start_time
            self.label.config(text=f'Timer: {timer}')
               
    def stop(self):
        self.running = False