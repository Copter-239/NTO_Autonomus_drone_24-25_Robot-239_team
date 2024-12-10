import random

with open("top.world", "r") as file:
    lines = file.readlines()


def r(x, y,id):
    return ['    <include>\n', '      <uri>model://dronepoint_red</uri>\n', '      <name>' + str(id)+'</name>','      <pose>' + str(x) + ' ' + str(y) +  ' 0 0 0 0</pose>\n' + '    </include>\n']
def g(x, y,id):
    return ['    <include>\n', '      <uri>model://dronepoint_green</uri>\n', '      <name>' + str(id)+'</name>','      <pose>' + str(x) + ' ' + str(y) +  ' 0 0 0 0</pose>\n' + '    </include>\n']
def b(x, y,id):
    return ['    <include>\n', '      <uri>model://dronepoint_blue</uri>\n', '      <name>' + str(id)+'</name>','      <pose>' + str(x) + ' ' + str(y) +  ' 0 0 0 0</pose>\n' + '    </include>\n']
def y(x, y,id):
    return ['    <include>\n', '      <uri>model://dronepoint_yellow</uri>\n','      <name>' + str(id)+'</name>', '      <pose>' + str(x) + ' ' + str(y) +  ' 0 0 0 0</pose>\n' + '    </include>\n']


for i in range(5):
    cx, cy = random.randint(0, 9), random.randint(0, 9)
    rand = random.choice(('r', 'g', 'b', 'y'))
    if rand[0] == 'r':
        lines.extend(r(cx, cy,i))
    elif rand[0] == 'g':
        lines.extend(g(cx, cy,i))
    elif rand[0] == 'b':
        lines.extend(b(cx, cy,i))
    elif rand[0] == 'y':
        lines.extend(y(cx, cy,i))

with open("bottom.world", "r") as file:
    lines.extend(file.readlines())

with open("/home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/clover_aruco.world", "w") as file:
    file.writelines(lines)
with open("/home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/clover.world", "w") as file:
    file.writelines(lines)