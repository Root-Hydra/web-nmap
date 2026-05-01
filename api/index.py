from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/api/scan')
def scan():
    target = request.args.get('target', '127.0.0.1')
    
    # Mock Nmap Output to simulate reality on Vercel
    # In a real VPS, you'd use: subprocess.check_output(['nmap', '-sV', target])
    mock_result = f"""
Starting Nmap 7.94 ( https://nmap.org ) at 2026-05-01 14:32 BDT
Nmap scan report for {target}
Host is up (0.048s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 3.0.3
22/tcp   open  ssh      OpenSSH 8.9p1
80/tcp   open  http     Apache httpd 2.4.52
443/tcp  open  ssl/http Apache httpd 2.4.52
3306/tcp open  mysql    MySQL 8.0.35

Service detection performed.
Nmap done: 1 IP address (1 host up) scanned in 12.5 seconds
    """
    return jsonify({"result": mock_result})

if __name__ == '__main__':
    app.run()
