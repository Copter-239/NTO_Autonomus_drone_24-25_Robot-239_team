
from pprint import pprint
from os import startfile
from time import time, sleep
import rospy
from clover import srv
from std_srvs.srv import Trigger
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from clover import long_callback


cord = [1,1]
startfile('server.py')
bridge = CvBridge()
map = [['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', ''],
       ['', '', '', '', '', '', '', '', '', '']]
map[0][0] = 'N'


def update_site(map):
    color_str={'R':'Red', 'G':'Green', 'B':"Blue", 'Y':'Yellow', 'N':'None'}
    color_16RGB= {'R':'FF0000', 'G':'00FF00', 'B':"0000FF", 'Y':'F0F000', "N":'C0C0C0', '':'808080'}
    color_Purpose={'R':'Administration', 'G':'Laboratory', 'B':"Coal preparation", 'Y':'Mine entrance', 'N':'None'}
    i=[]
    for x_map in range(10):
        for y_map in range(10):
            e = map[x_map][y_map]
            if "N" != e and '' != e:
                i.append([e, x_map+1,y_map+1])
    if len(i) <=4:
        for u in range(5-len(i)):
            i.append(['N','None','None'])
    html = f"""
    <!DOCTYPE>
<html>
<meta http-equiv="refresh" content="1">
<p><a href="/get/start"><button class="button button_led">start</button></a></p>
<p><a href="/get/stop"><button class="button button_led">stop</button></a></p>
<p><a href="/get/kill"><button class="button button_led">kill</button></a></p>
<p><a href="/get/update"><button class="button button_led">update</button></a></p>
<table border="1" cellpadding="1" cellspacing="1">
	<tbody>
		<tr>
			<td>Color</td>
			<td>{color_str[i[0][0]]}</td>
			<td>{color_str[i[1][0]]}</td>
			<td>{color_str[i[2][0]]}</td>
			<td>{color_str[i[3][0]]}</td>
			<td>{color_str[i[4][0]]}</td>
		</tr>
		<tr>
			<td>Purpose</td>
			<td>{color_Purpose[i[0][0]]}</td>
			<td>{color_Purpose[i[1][0]]}</td>
			<td>{color_Purpose[i[2][0]]}</td>
			<td>{color_Purpose[i[3][0]]}</td>
			<td>{color_Purpose[i[4][0]]}</td>
		</tr>
		<tr>
			<td>X</td>
			<td>{i[0][1]}</td>
			<td>{i[1][1]}</td>
			<td>{i[2][1]}</td>
			<td>{i[3][1]}</td>
			<td>{i[4][1]}</td>
		</tr>
		<tr>
			<td>Y</td>
			<td>{i[0][2]}</td>
			<td>{i[1][2]}</td>
			<td>{i[2][2]}</td>
			<td>{i[3][2]}</td>
			<td>{i[4][2]}</td>
		</tr>
	</tbody>
</table>
<body>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[0][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[0][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[1][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[1][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[2][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[2][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[3][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[3][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[4][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[4][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[5][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[5][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[6][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[6][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[7][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[7][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[8][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[8][9]]};">&#9632; </span></p>
<p style="line-height: 0;"><span style="color:#{color_16RGB[map[9][0]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][1]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][2]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][3]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][4]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][5]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][6]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][7]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][8]]};">&#9632; </span><span style="color:#{color_16RGB[map[9][9]]};">&#9632; </span></p>
</body>
</html>
    """
    open('site.html', 'w').write(html)
update_site(map)
open('data.data', 'w').write('')
@long_callback
def image_callback(msg):
    global cord
    global map
    if map[cord[0]-1][cord[1]-1]=='':
        #imgg = bridge.imgmsg_to_cv2(msg, 'bgr8')
        # convert to HSV to work with color hue
        #img2 = cv2.cvtColor(imgg, cv2.COLOR_BGR2HSV)
        #img2 = cv2.cvtColor(bridge.imgmsg_to_cv2(msg, 'bgr8'), cv2.COLOR_BGR2HSV)
        img = cv2.cvtColor(bridge.imgmsg_to_cv2(msg, 'bgr8'), cv2.COLOR_BGR2HSV)[120:200, 80:160]
        r = 0
        j = cv2.inRange(img, (165, 40, 40), (180, 255, 255)).tolist()
        for a in j: r = r + sum(a)//255
        j = cv2.inRange(img, (0, 40, 40), (15, 255, 255)).tolist()
        for a in j: r = r + sum(a)//255

        g = 0
        j = cv2.inRange(img, (45, 40, 40), (75, 255, 255)).tolist()
        for a in j: g = g + sum(a)//255
        b = 0
        j = cv2.inRange(img, (95, 40, 40), (130, 255, 255)).tolist()
        for a in j: b = b + sum(a)//255
        y = 0
        j = cv2.inRange(img, (25, 40,40), (40, 255, 255)).tolist()
        for a in j: y = y + sum(a)//255
        print('\r', end=f'{r},{g},{b},{y}               ')
        c = {r:'R',g:'G',b:'B',y:'Y', 1000:"N"}
        map[cord[0]-1][cord[1]-1] = c[max(c.keys())]
        update_site(map)

rospy.init_node('flight')
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
def navigate_plys(x,y,z,frame_id):
    global cord
    navigate(x=x, y=y, z=z, frame_id=frame_id)
    a = time()
    while not a + 5 <= time():
        f = open('data.data').read()
        if f != '' or 's' != f:
            open('data.data', 'w').write('')
            if f == 'f':
                land()
                rospy.sleep(5)
                exit()
            if f == 'k':
                rospy.on_shutdown()
                rospy.sleep(5)
                exit()
    cord = [x, y]


height = 1.7


start = False
while not start:
    if open('data.data').read() == 's':start = True
    else:sleep(0.5)


# process every frame:
image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback, queue_size=1)

print('Take off and hover 1 m above the ground')
navigate(x=1, y=1, z=height, frame_id='aruco_map', auto_arm=True)
rospy.sleep(5)


navigate_plys(x=2, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=1, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=9, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=8, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=7, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=6, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=5, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=4, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=3, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=2, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=10, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=9, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=8, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=7, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=6, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=5, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=4, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=3, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=2, z=height, frame_id='aruco_map')
navigate_plys(x=1, y=1, z=height, frame_id='aruco_map')
pprint.pprint(map)




print('Perform landing')
land()
