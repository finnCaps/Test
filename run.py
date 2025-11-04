from calculator import SaPytha
from config import con

def main():
    a,b=con()
    c=SaPytha(a,b)
    print("c=",c)
    
if __name__ == "__main__":
        main()