from nullsec_phantom_id.core import DeviceProfiler
p=DeviceProfiler()
for dev in ["windows10","macos","iphone","android","iot"]:
    phantom=p.generate_phantom(dev)
    print(f"{dev}: MAC={phantom['mac']} TTL={phantom['ttl']} Hostname={phantom['hostname']}")
print(f"\nOS Detection: TTL=128 -> {p.detect_os(128,65535)}")
