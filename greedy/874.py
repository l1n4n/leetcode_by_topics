#874 Walking Robot Simulation
# A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# Some of the grid squares are obstacles. 

# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

# If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

# Return the square of the maximum Euclidean distance that the robot will be from the origin.


#GREEDY: LOCAL MAXIMUM IS THE GLOBAL MAXIMUM
# USE matrix to represent rotation, i.e., linear transformation
# USE set to store obstacles for O(1) lookup

class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        def v_dot_m(A, v):
            x, y = v
            v[0] = A[0][0]*x + A[0][1]*y
            v[1] = A[1][0]*x + A[1][1]*y
        
        direction = [0, 1]
        L90 = [[0, -1],
               [1, 0]]
        R90 = [[0, 1],
              [-1, 0]]
        pos = [0, 0]
        mx_dis = 0
        obstacles = {(x, y) for (x, y) in obstacles}
        for cmd in commands:
            if cmd == -2:
                v_dot_m(L90, direction)
            elif cmd == -1:
                v_dot_m(R90, direction)
            else:
                dx, dy = direction
                for i in range(cmd):
                    if (pos[0] + dx, pos[1] + dy) in obstacles:
                        break
                    pos[0] += dx
                    pos[1] += dy
                mx_dis = max(mx_dis, pos[0]**2 + pos[1]**2)
        return mx_dis