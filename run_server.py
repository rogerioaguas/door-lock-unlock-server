from flask import Flask
from flask import jsonify
# import time
# from panda import Panda

app = Flask(__name__)

# p = Panda()

lockCommand = [0x40, 0x05, 0x30, 0x11, 0x00, 0x80, 0x00, 0x00]
unlockCommand = [0x40, 0x05, 0x30, 0x11, 0x00, 0x40, 0x00, 0x00]


def lock_door():
    # p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
    # p.can_send(0x750, bytes(unlockCommand), 0)
    # p.can_send(0x750, bytes(lockCommand), 0)
    # p.can_send(0x750, bytes(unlockCommand), 0)
    # p.can_send(0x750, bytes(lockCommand), 0)
    # time.sleep(0.2)
    # p.set_safety_mode(Panda.SAFETY_TOYOTA)
    # p.send_heartbeat()
    pass


def unlock_door():
    # p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
    # p.can_send(0x750, bytes(lockCommand), 0)
    # p.can_send(0x750, bytes(unlockCommand), 0)
    # p.can_send(0x750, bytes(lockCommand), 0)
    # p.can_send(0x750, bytes(unlockCommand), 0)
    # time.sleep(0.2)
    # p.set_safety_mode(Panda.SAFETY_TOYOTA)
    # p.send_heartbeat()
    pass

@app.route('/')
def init():
    return "Welcome To Comma Door Server"

@app.route("/lock")
def lock():
    lock_door()
    return jsonify("{method:'lock',status:true}")


@app.route("/unlock")
def unlock():
    unlock_door()
    return jsonify("{method:'unlock',status:true}")
