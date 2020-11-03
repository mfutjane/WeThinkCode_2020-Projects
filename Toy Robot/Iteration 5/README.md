# Toy Robot 5

In this iteration, the toy robot can navigate a maze on its own (if you tell it to).

### To use

- Download the repo and run python3 robot.py with one of these flags:
  - turtle to use text graphics
  - text to use the console only
  - simple_maze to use the maze as the world (independent of turtle or text)
  - obstacles to use the simple obstacles from toy robot 4 as the world (independent of turtle or text)
- Name the robot.
- To move the robot, give it a command,
- forward X will move it forward by X steps.
- back X will move it back by X steps.
- left will have it turn left.
- right will have it turn right.
- sprint X will make it move forward by X, X-1, X-2, until X=0.
- replay X will replay the last X commands (excluding replay, help, off).
- replay M-N will replay from the Mth command to the Nth command. M > N
- replay will replay all previous commands.
- mazerun will tell the turtle to find a path to the top of the screen and go there. Use a flag to direct it:
  - mazerun bottom will tell the turtle to find a path to the bottom of the screen.
  - mazerun top will tell the turtle to find a path to the top of the screen.
  - mazerun left will tell the turtle to find a path to the left of the screen.
  - mazerun right will tell the turtle to find a path to the right of the screen.
- off will turn the robot off.
