"""this program is bassed on Breadth-first search.BFS is a basic graph searching algorithm that can find the shortest path to a node in an unweighted graph.
BFS variation Dijkstra's algorithm is used to find the shortest path between nodes in a weighted graph.
THIS ALGORITHM IS MAINLY USED BY DELIVERY COMPANIES AND MAP FOR THE SHORTEST POSSIBLE ROUTE """
import curses
from curses import wrapper
import queue
import time

# maze = [
#     ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
#     ["#", " ", " ", " ", " ", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", " ", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
#     ["#", " ", "#", " ", " ", " ", " ", " ", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
# ]

def file_to_list(file_path):
    """
    Reads an ASCII maze file and converts it into a nested list.
    Each line becomes a list of characters, and all lines are stored in a parent list.
    """
    try:
        with open(file_path, 'r') as file:
            # Read lines and split each line into a list of characters
            nested_list = [list(line.strip()) for line in file]
        return nested_list
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

# Path to the ASCII maze file
file_path = "maze_ascii.txt"

# Convert the file to a nested list
maze= file_to_list(file_path)

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j, "X", RED)#this is for showing the path
            else:
                stdscr.addstr(i, j, value, BLUE)#this is for normal maze print+



def start_position(maze,start):
    for i, row in enumerate(maze):
        for j, values in enumerate(row):
            if values==start:
                return i,j
    return None

def find_path(maze,stdscr):
    start="O"
    end="X"
    start_pos=start_position(maze,start)

    q=queue.Queue()
    q.put((start_pos,[start_pos]))

    visited=set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
       
        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.005)
        stdscr.refresh()   

        if maze[row][col]==end:
            return path
        
        neighbors= find_neighbors(maze,row,col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c=neighbor
            if maze[r][c]=="|":
                continue
            new_path = path + [neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  # UPSIDE NEIGHBOUR
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWNSIDE NEIGHBOUR
        neighbors.append((row + 1, col))
    if col > 0:  # LEFTSIDE NEIGHBOUR
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHTSIDE NEIGHBOUR
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    
    find_path(maze,stdscr)
    stdscr.getch()

wrapper(main)
