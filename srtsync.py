import sys 
import re




def readSeconds(line, index, delay) :
    
    hours = int(line[index:index+2])
    minutes = int(line[index+3:index+5])
    seconds = int(line[index+6:index+8])
    
    time = seconds + minutes*60 + hours*3600 + delay;

    if time < 0 :
        time = 0;

    return time;
    
def addDelay(line, delay) :
    
    

    
    seconds_a = readSeconds(line, 0, delay)
    

    hours_a = seconds_a // 3600
    minutes_a   = (seconds_a % 3600) // 60
    secs_a = seconds_a % 60
    

    seconds_b = readSeconds(line, 17, delay)
    

    hours_b = seconds_b // 3600
    minutes_b   = (seconds_b % 3600) // 60
    secs_b = seconds_b % 60

    return f"{hours_a:02}:{minutes_a:02}:{secs_a:02},{line[9:12]} --> {hours_b:02}:{minutes_b:02}:{secs_b:02},{line[26:29]}\n"




datoteka = open(sys.argv[1]);
lines = datoteka.readlines();
datoteka.close();
delay = int(sys.argv[2]);

if len(sys.argv) > 3 :
    lol = open(sys.argv[3], "w");
else :
    lol = open(sys.argv[1], "w");







i = 1;

for j in range(len(lines)) :
    line = lines[j]
    if i == 0 :
        lines[j] = addDelay(line, delay)
        i = i - 1;
    
    elif line[0] == '\n' :
        
        i = 1;
    else :
        i = i - 1;


lol.writelines(lines);
lol.close();






        
    
    
    
    
    
    
    
    
    





        
        
    



    
    
    
    
    
    
    


