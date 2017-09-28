import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)