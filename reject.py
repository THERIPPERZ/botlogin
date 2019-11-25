# BY TEAMBOTMAX
# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
maxbots = LINE()
int1 = len(maxbots.getGroupIdsInvited())
if int1 == 0:
    print("No groups inviting")
else:
    for groups in maxbots.getGroupIdsInvited():
        print("Reject " + maxbots.getGroup(groups).name)
        sleep(0.7)
        maxbots.rejectGroupInvitation(groups)
    print("\nYou reject" + str(int1) + "groups invitation")
    
