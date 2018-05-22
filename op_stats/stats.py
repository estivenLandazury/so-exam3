import psutil

class Stats():

  @classmethod
  def cpuPercent(cls):
    cpuPercent = psutil.cpu_percent()    
    return  cpuPercent

  @classmethod
  def ram(cls):
    ramMemory = psutil.virtual_memory()[1]
    return  ramMemory

  @classmethod   
  def disk(cls):
    diskete = psutil.disk_usage('/')[3]
    return  diskete
