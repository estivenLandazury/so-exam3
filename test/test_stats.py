import pytest
from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'cpuPercent', return_value=100)
  response = client.get('/cpu')
  assert response.data.decode('utf-8') == '{"cpu_percent": 100}'
  assert response.status_code == 200 



def test_get_ram_info(mocker, client):
  mocker.patch.object(Stats, 'ram' , return_value=100)
  response = client.get('/ram')
  assert response.data.decode('utf-8') == '{"ram_info": 100}'
  assert response.status_code ==200 

def test_get_disk_info(mocker, client):
  mocker.patch.object(Stats, 'disk' , return_value=100)
  response = client.get('/disk')
  assert response.data.decode('utf-8') == '{"disk_info": 100}'
  assert response.status_code ==200
