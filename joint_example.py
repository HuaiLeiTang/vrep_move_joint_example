import vrep
import math

vrep.simxFinish(-1)  # just in case, close all opened connections

clientID = vrep.simxStart('127.0.0.1',19999, True, True,2000,5)

_, joint = vrep.simxGetObjectHandle(clientID,'Junta',vrep.simx_opmode_oneshot_wait)

vrep.simxSetJointTargetPosition(clientID, joint, 20*math.pi/180, vrep.simx_opmode_oneshot)

while(1):

    _, joint_angle = vrep.simxGetJointPosition(clientID, joint, vrep.simx_opmode_oneshot)
    
    if(joint_angle > 19*math.pi/180): # With perfect control parameters we should compare with 20*math.pi/180
                                      # but we are just using a Proportinal control
                                      # and P control do not achieve the desired value
        vrep.simxSetJointTargetPosition(clientID, joint, -20*math.pi/180, vrep.simx_opmode_oneshot)
        
    elif(joint_angle < -19*math.pi/180):
        vrep.simxSetJointTargetPosition(clientID, joint, 20*math.pi/180, vrep.simx_opmode_oneshot)