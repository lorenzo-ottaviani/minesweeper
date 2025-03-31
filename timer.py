import time


class Timer:
    def __init__(self, label):
        self.label = label
        self.running = False
        self.start_time = None
        
    def start(self):
        self.running = True
        self.start_time = time.time()
        self.update()
    
    def update(self):
        if self.running:
            timer = int(time.time() - self.start_time)
            self.label.config(text=f'Timer: {timer}')
            self.label.after(1000, self.update)
               
    def stop(self):
        self.running = False
        