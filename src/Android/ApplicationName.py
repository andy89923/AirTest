
from enum import Enum

class AndroidApp(Enum):
    chrome = "com.android.chrome"
    youtube = "com.google.android.youtube"



if __name__ == "__main__":
    print(AndroidApp.chrome) 
    print(AndroidApp.youtube)
    
    