suricata_logs = [
    {
        "timestamp": "2025-10-02T05:43:12.123456+0000",
        "flow_id": 1234567890,
        "event_type": "alert",
        "src_ip": "192.168.1.10",
        "src_port": 52345,
        "dest_ip": "93.184.216.34",
        "dest_port": 80,
        "proto": "TCP",
        "alert": {
            "action": "allowed",
            "gid": 1,
            "signature_id": 2100498,
            "rev": 3,
            "signature": "ET MALWARE Possible Malicious HTTP User-Agent",
            "category": "A Network Trojan was detected",
            "severity": 2
        }
    },
    {
        "timestamp": "2025-10-02T05:43:15.543210+0000",
        "flow_id": 987654321,
        "event_type": "dns",
        "src_ip": "192.168.1.15",
        "src_port": 52000,
        "dest_ip": "8.8.8.8",
        "dest_port": 53,
        "proto": "UDP",
        "dns": {
            "type": "query",
            "id": 1234,
            "rrname": "suspicious-domain.com",
            "rrtype": "A",
            "tx_id": 0
        }
    },
    {
        "timestamp": "2025-10-02T05:43:20.000000+0000",
        "flow_id": 192837465,
        "event_type": "http",
        "src_ip": "192.168.1.20",
        "src_port": 52300,
        "dest_ip": "93.184.216.34",
        "dest_port": 80,
        "proto": "TCP",
        "http": {
            "hostname": "test.example.com",
            "url": "/login",
            "http_user_agent": "curl/7.81.0",
            "http_method": "POST",
            "status": 200,
            "length": 512
        }
    }
]

seen = set()
ordered_unique_dest_ips = []
for log in suricata_logs:
    ip = log.get("dest_ip")
    if ip and ip not in seen:
        seen.add(ip)
        ordered_unique_dest_ips.append(ip)


print(ordered_unique_dest_ips)
