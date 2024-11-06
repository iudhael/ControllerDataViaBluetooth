from approxeng.input.selectbinder import ControllerResource
import time

while True:
    try:
        # Get a joystick
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            # Loop until disconnected
            while joystick.connected:
                message = {
                    "CH1" : int(joystick.rx * 100),
                    "CH2" : int(joystick.ry * 100),
                    "CH3" : int(joystick.ly * 100),
                    "CH4" : int(joystick.lx * 100),
                }
                print(message)
                
                
                time.sleep(0.1)

        # Joystick disconnected...
        print('Connection to joystick lost')
    except IOError:
        # No joystick found, wait for a bit before trying again
        print('Unable to find any joysticks')
        time.sleep(1.0)

        

        
