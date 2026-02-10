"""Phantom ID Engine"""
import random,json,hashlib

class DeviceProfiler:
    PROFILES={
        "windows10":{"ttl":128,"window_size":65535,"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)","os":"Windows"},
        "macos":{"ttl":64,"window_size":65535,"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)","os":"macOS"},
        "linux":{"ttl":64,"window_size":29200,"user_agent":"Mozilla/5.0 (X11; Linux x86_64)","os":"Linux"},
        "iphone":{"ttl":64,"window_size":65535,"user_agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0)","os":"iOS"},
        "android":{"ttl":64,"window_size":65535,"user_agent":"Mozilla/5.0 (Linux; Android 14)","os":"Android"},
        "iot":{"ttl":64,"window_size":5840,"user_agent":"","os":"Embedded"},
    }
    
    def get_profile(self,device_type):
        return self.PROFILES.get(device_type,self.PROFILES["linux"])
    
    def detect_os(self,ttl,window_size):
        if ttl>100: return "Windows"
        if window_size==29200: return "Linux"
        if window_size==65535 and ttl==64: return "macOS/iOS"
        return "Unknown"
    
    def generate_phantom(self,device_type):
        profile=self.get_profile(device_type)
        mac=":".join(f"{random.randint(0,255):02x}" for _ in range(6))
        hostname=f"{device_type}-{random.randint(1000,9999)}"
        return {"mac":mac,"hostname":hostname,**profile,"phantom":True}
