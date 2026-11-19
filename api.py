from flask import Flask, render_template, request
from netmiko import ConnectHandler

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET' , 'POST'])
def index():
    results = {}
    error = None

    if request.method == 'POST':
        router_device = {
            'device_type': 'cisco_ios_telnet',
            'ip': '192.168.10.78',
            'port': 32770,
            'username': 'admin',
            'password': 'eve123',
            'secret': 'eve123'
        }

        try:
            print("Connecting to router...")
            net_connect = ConnectHandler(**router_device)
            net_connect.enable()

            commands_to_run = [
                "show version",
                "show ip interface brief",
                "show running-config",
            ]

            for cmd in commands_to_run:
                print(f"--- Output for: (cmd) ---")
                output = net_connect.send_command(cmd)
                print(output)

            net_connect()
            print("\nDisconnected successfully.")
            
        except Exception as e:
            print(f"Connection failed: {e}")

    return render_template('index.html', results=results, error=error)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)