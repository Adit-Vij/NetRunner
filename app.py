from flask import Flask, render_template, request, redirect, url_for, jsonify
from port_scan import scan_ports
from ip_logger import start_sniffing, contacted_ips

import threading

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html',open_ports=None)

@app.route('/port_scan', methods=['POST'])
def start_scan():

    start_port = int(request.form['start_port'])
    end_port = int(request.form['end_port'])
    open_ports = scan_ports(start_port,end_port)

    return render_template('index.html',open_ports=open_ports, contacted_ips=contacted_ips)

@app.route('/log_ip',methods=['POST'])
def start_logging():

    threading.Thread(target = start_sniffing, daemon = True).start()
    return redirect(url_for('index'))

@app.route('/get_contacted_ips')
def get_contacted_ips():
    return jsonify(contacted_ips)

#Main
if __name__ =='__main__':
    app.run(debug=True)