from naoqi import ALProxy
import threading

class RobotTaiChi(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip_robot = ip
        self.port_robot = port

    def run(self):
        motion = ALProxy("ALMotion", self.ip_robot, self.port_robot)
        motion.moveInit()
        #motion.post.moveTo(0.2, 0, 0)
        p = ALProxy("ALAnimatedSpeech", self.ip_robot, self.port_robot)
        p.say("Hello everybady! Do you see us? ^run(animations/Stand/Gestures/Hey_7)")
        for i in range(4):
            motion.openHand("RHand")
            motion.closeHand("RHand")
        print 'A robot vegzet'

pepper = RobotTaiChi("192.168.18.250", 9559)

print 'A foprogram tovabb fut az eloterben.'
nao = RobotTaiChi("192.168.18.79", 9559)
nao.start()
pepper.start()

pepper.join()
nao.join()  # Varakozas a hattermuvelet befejezesere

print 'A foprogram megvarja, hogy a hattermuvelet befejezodjon.'

