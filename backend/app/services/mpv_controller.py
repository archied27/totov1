import socket
import json
import os
import subprocess

MPV_SOCKET = "/tmp/mpvsocket"

def testMpv():
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        client.connect(MPV_SOCKET)
        return True
    except (FileNotFoundError, ConnectionRefusedError, socket.error):
        return False

def closeMpv():
    if testMpv():
       send_mpv_command("quit")
    else:
        subprocess.run(["pkill", "-f", "mpv"], check=False)
    return {"status": "closed"}
    
def send_mpv_command(command: str, args=None):
    payload = {"command": [command]}
    if args:
        payload["command"].extend(args)
    payload = json.dumps(payload).encode("utf-8") + b"\n"
    
    if not testMpv():
        return -1

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(MPV_SOCKET)
        client.sendall(payload)
        response = client.recv(4096)
        client.close()
        return json.loads(response.decode("utf-8"))

def getCurrTitle():
    resp = send_mpv_command("get_property", ["media-title"])
    if resp == -1:
        return {"title": None, "error": "mpv not open in correct mode"}
    elif resp.get("error") != "success":
        return {"title": None, "error": resp.get("error")}
    else:
        return {"title": resp.get("data")}

def play(path: str):
    closeMpv()
    subprocess.Popen(["mpv", path, f"--input-ipc-server={MPV_SOCKET}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    return{"status": "started", "file": path}

def fullscreen(val: bool):
    if send_mpv_command("set_property", ["fullscreen", val]) == -1:
        return {"status": "mpv not open in correct mode"}
    else:
        return {"status": "fullscreen toggled"}

def playPause():
    status = getPause()
    if status == -1:
        return {"status": "mpv not open in correct mode"}
    else:
        send_mpv_command("set_property", ["pause", not status.get("pause")])
        return {"status": not status.get("pause")}

def getPause():
    response = send_mpv_command("get_property", ["pause"])
    
    if response == -1:
        return {"pause": None, "status": "mpv not open in correct mode"}
    else:
        return {"pause": response.get('data')}