from calculator import SaPytha
from config import con

def main():
    a,b,d=con()
    c=SaPytha(a,b)
    print("c=",c)
    print("d=",d)
    
if __name__ == "__main__":
        main()