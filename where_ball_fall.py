class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid) # of rows
        n = len(grid[0]) # of cols
        balls = [i for i in range(n)]
        for y in range(m):
            new_balls = []
            for ball in balls:
                if ball+1 != n and grid[y][ball] == 1 and ball != -1 and grid[y][ball+1] != -1:
                    ball += 1
                elif ball-1 >= 0 and grid[y][ball] == -1 and ball != -1 and grid[y][ball-1] != 1:
                    ball -= 1
                else:
                    ball = -1
                new_balls.append(ball)
            balls = new_balls
        return balls
            
