import psutil

def test_cpu_usage():
    cpu = psutil.cpu_percent(interval=0.1)
    assert isinstance(cpu, float)
    assert 0.0 <= cpu <= 100.0

def test_ram_usage():
    ram = psutil.virtual_memory().percent
    assert isinstance(ram, float)
    assert 0.0 <= ram <= 100.0

def test_disk_usage():
    disk = psutil.disk_usage('/').percent
    assert isinstance(disk, float)
    assert 0.0 <= disk <= 100.0

def test_network_usage():
    net = psutil.net_io_counters()
    assert hasattr(net, "bytes_sent")
    assert hasattr(net, "bytes_recv")
