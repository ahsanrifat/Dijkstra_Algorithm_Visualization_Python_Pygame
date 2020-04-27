import pygame
import sys
import math
import time
import os

def change_green(tup1,tup2,n1,n2,red):
    
    font = pygame.font.Font(None, 40)
    
    pygame.draw.circle(screen, red, tup1, 30)
    pygame.draw.circle(screen, red, tup2, 30)
    pygame.draw.line(screen,red,tup1,tup2,4)
    
    
    text = font.render(n1, 1, (255,255,255))
    screen.blit(text,tup1)
    
    text = font.render(n2, 1, (255,255,255))
    screen.blit(text,tup2)
    
    pygame.display.update()
    time.sleep(.3)


def change_red(tup1,tup2,n1,n2,red):
    
    font = pygame.font.Font(None, 40)
    
    pygame.draw.circle(screen, red, tup1, 30)
    pygame.draw.circle(screen, red, tup2, 30)
    pygame.draw.line(screen,red,tup1,tup2,4)
    
    
    text = font.render(n1, 1, (255,255,255))
    screen.blit(text,tup1)
    
    text = font.render(n2, 1, (255,255,255))
    screen.blit(text,tup2)
    
    pygame.display.update()
    time.sleep(.1)
    
    pygame.draw.circle(screen, graph_color, tup1, 30)
    pygame.draw.circle(screen, graph_color, tup2, 30)
    pygame.draw.line(screen,graph_color,tup1,tup2,4)
    
    text = font.render(n1, 1, (255,255,255))
    screen.blit(text,tup1)
    
    text = font.render(n2, 1, (255,255,255))
    screen.blit(text,tup2)
    

def find_smallest():
    global all_nodes
    ret=list()
    min=10000
    
    for key in all_nodes:
        if int(all_nodes[key][1])<min:
            min=all_nodes[key][1]
            ret=all_nodes[key]
    return ret

def dijkstra(source,destination):
    
    global visited
    global weight
    global connected
    global all_nodes
    global graph
    global clock
    global path
    global sequnce
    global red
    global green
    
    if(len(all_nodes)!=0):
        visited[source]=True
        all_nodes[source][1]=0
    
    while len(all_nodes)!=0:
        
        small=(find_smallest())
        
        current_node=small[0]
        current_dist=small[1]
        visited[current_node]=True
        cirA=(graph[current_node][0],graph[current_node][1])
      
        del all_nodes[current_node]
        
        path[current_node]=small
        
        for i in connected[current_node]:
            
            if visited[i]!=True:
                
                cirB=graph[i][0],graph[i][1]
                
                change_red(cirA,cirB,current_node,i,red)
                pygame.display.update()
                time.sleep(.1)
                
                str1="".join(sorted(current_node+i))
                dist_i=weight[str1]
                total_weight=dist_i+current_dist
                if all_nodes[i][1]>total_weight:
                    all_nodes[i][1]=total_weight
                    all_nodes[i][2]=current_node
                   
    find=destination
    sequence.append(find)
    for _ in range(len(graph)):
        prev=path[find]
        prev=prev[2]  
        if prev==source:
            sequence.append(prev)
            break
        else:
            sequence.append(prev)
            find=prev
    le= len(sequence)
    count=le-1         
    if le>2:
        for x in range (0,le-1):
            cirA=graph[sequence[count]]
            cirA=(cirA[0],cirA[1])
            cirB=graph[sequence[count-1]]
            cirB=(cirB[0],cirB[1])
            change_green(cirA,cirB,sequence[count],sequence[count-1],green)
            count=count-1  
    

def draw_cir(tup):
    global graph_color
    pygame.draw.circle(screen, graph_color, tup, 30)

def draw_path(a,b,n1,n2):
    global graph_color
    pygame.draw.line(screen,graph_color,a,b,4)
    
    font = pygame.font.Font(None, 40)
    text = font.render(n1, 1, (255,255,255))
    screen.blit(text,a)
    text = font.render(n2, 1, (255,255,255))
    screen.blit(text,b)

def draw_graph():
    
    global all_nodes
    global conn
    global visited
    global screen
    global graph
    global connected
    global way
    global weight
    
    
    
    for key in graph:
        tup=(graph[key][0],graph[key][1])
        draw_cir(tup)
        
        visited[key]=False
        connected[key]=set()
        all_nodes[key]=[key,10000,"False"]
        
    for i in conn:
        cirA=(graph[i[0]][0],graph[i[0]][1])
        cirB=(graph[i[1]][0],graph[i[1]][1])
        
        
        midx=round((cirA[0]+cirB[0])//2)
        midy=round((cirA[1]+cirB[1])//2)
        
        distance=abs(cirA[0]-cirB[0])*abs(cirA[0]-cirB[0]) + abs(cirA[1]-cirB[1])*abs(cirA[1]-cirB[1])
        
        distance=str(math.sqrt(distance)//10).split(".")
        
        draw_path(cirA,cirB,i[0],i[1])
        
        font = pygame.font.Font(None, 40)  
        text = font.render(str(distance[0]), 1, (0,0,0))
        screen.blit(text, (midx,midy))
        str1=i[0]+i[1]
        str1=sorted(str1)
        str1=''.join(str1)
        weight[str1]=int(distance[0])
        
        
        
        connected[i[0]].add(i[1])
        connected[i[1]].add(i[0])
        
    
    
    
    
graph={
    "A":[150,50],
    "B":[50,200],
    "C":[550,100],
    "D":[250,200],
    "E":[160,400],
    "F":[700,180],
    "G":[330,400],
    "H":[400,600],
    "I":[600,500],
    "J":[700,700],
    "K":[70,600],
    "L":[250,750]
}

conn=[
    ["A","B"],["A","C"],["A","D"],["B","E"],
    ["C","G"],["C","F"],["D","E"],["D","G"],
    ["E","G"],["E","H"],["F","G"],["F","I"],
    ["G","I"],["H","I"],["I","J"],["D","C"],
    ["G","H"],["B","D"],["J","H"],["J","F"],
    ["K","B"],["K","E"],["K","H"],
    ["L","K"],["L","H"],["L","J"]
]  
    

all_nodes=dict()
visited=dict()
connected=dict()
weight=dict()
way=set()
path=dict()
sequence=list()

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock=pygame.time.Clock()

graph_color=(58,0,118)
text_color=(0,0,0)
red=(255,89,0)
green=(255,212,0)

screen_width=800
screen_height=3000

screen=pygame.display.set_mode((800, 800), pygame.RESIZABLE)
screen.fill((163,255,240))
pygame.display.set_caption("Path Finding")
flag=True

draw_graph()
time.sleep(10)
dijkstra("A","J")
print(path)
print(sequence)

while flag:
    for event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            flag=False
        pygame.display.update()
        # 
        pygame.display.update()
    clock.tick(60)