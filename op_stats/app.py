from flask import Flask
import json
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/cpu')
def get_cpu_info():
  cpuInfo = Stats.cpuPercent()
  return json.dumps({'cpu_percent': cpuInfo})

@app.route('/ram')
def get_ram_info():
  ramInfo= Stats.ram()
  return json.dumps({'ram_info': ramInfo})

@app.route('/disk')
def get_disk_info():
  diskInfo = Stats.disk()
  return json.dumps({'disk_info': diskInfo})



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
