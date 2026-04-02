import sys

while(1):
    question = sys.stdin.readline().strip()

    if(question == "animal"):
        print("Panthera tigris")
    
    elif(question == "tree"):
        print("Pinus densiflora")
    
    elif(question == "flower"):
        print("Forsythia koreana")
    
    elif(question == "end"):
        break