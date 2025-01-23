import modules.varGlobals as varGlobals
import threading
import time
from library.playGame import playGame 
import modules.dataRobot as dataRobot
from modules.dataRobot import catch_ball
from library.skillBaru import (
    powerShoot,
    pindahAwalKiper,
    ballPredictKiper,
    kejarBolaPelan,
    passing,
    lihatBolaDiam,
    kejarBolaCepat,
    ubahPosisi,
    lihatBolaGeser,
    dribbling
)

def reset():
    varGlobals.runCornerKanan = False
    varGlobals.runCornerKiri = False
    
    varGlobals.runKickoffKanan = False
    varGlobals.runKickoffKiri = False
    
    varGlobals.runFreeKickTeam = False
    varGlobals.runFreeKickMusuh = False
    
    varGlobals.runGoalKickTeam = False
    varGlobals.runGoalKickMusuh = False
    
    varGlobals.runThrowInTeam = False
    varGlobals.runThrowInMusuh = False
    
    varGlobals.runCornerTeam = False
    varGlobals.runCornerMusuh = False
    
    varGlobals.runPenaltyTeam = False
    varGlobals.runPenaltyMusuh = False
    
    varGlobals.stop = False
    varGlobals.start = False
    varGlobals.dropBall = False
    varGlobals.park = False
    varGlobals.endPart = False

def KickOffHandler(isLeftKickoff):
    reset()
    varGlobals.runKickoffKiri = isLeftKickoff
    varGlobals.runKickoffKanan = not isLeftKickoff
    print("Mulai Kick Off Kanan")

    pindahAwalKiper()
    ballPredictKiper()

    positions = {
        1: {'x': 0, 'y': 0, 'angle': 90},  # Back
        2: {'x': 0, 'y': 0, 'angle': 360}   # Striker
    }

    # Lakukan pergerakan
    for robot_id, pos in positions.items():
        ubahPosisi(robot_id, pos['x'], pos['y'], pos['angle'])

    # Cek posisi
    diPosisi = all(
        dataRobot.xpos[robot_id] // 50 == pos['x'] // 50 and 
        dataRobot.ypos[robot_id] // 50 == pos['y'] // 50 
        for robot_id, pos in positions.items()
    )
    
    print("Sudah Di Posisi" if diPosisi else "Belum Di Posisi")

    # Strategi berdasarkan kondisi tim
    if varGlobals.striker and varGlobals.back:
        lihatBolaDiam(1)

        retry_count = 0
        while dataRobot.catch_ball[2] == 0 and retry_count < 1:  # Retry hingga bola tertangkap            
            kejarBolaCepat(2)
            retry_count += 1
            time.sleep(0.1)

        passing(2)
        lihatBolaDiam(1)

        while dataRobot.catch_ball[1] == 0 and retry_count < 2: 
            kejarBolaPelan(1)
            retry_count += 1
            time.sleep(0.1)

        dribbling(1)
        lihatBolaGeser(2)
        passing(1)
        dribbling(2)
        lihatBolaGeser(1)
        passing(2)
        dribbling(1)
        passing(1)
        dribbling(2)

        print("Striker berpindah 0,5 meter")
        powerShoot(2)

    elif varGlobals.striker and not varGlobals.back:
        kejarBolaPelan(2)
        dribbling(2)
        powerShoot(2)
        print("Selesai tendang gawang") 

    elif not varGlobals.striker and varGlobals.back:
        kejarBolaPelan(1)
        dribbling(1)
        powerShoot(1)
        print("Selesai tendang gawang")

    elif not varGlobals.striker and not varGlobals.back and varGlobals.kiper:
        kejarBolaPelan(1)
        dribbling(1)
        powerShoot(1)
        print("Selesai tendang gawang")

def KickOffKiri():
    KickOffHandler(True)
