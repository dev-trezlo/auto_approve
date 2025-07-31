from os import path, getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID", "17468849"))
    API_HASH = getenv("API_HASH", "36c072effa318649bdc42db4cda2c4eb")
    BOT_TOKEN = getenv("BOT_TOKEN", "8264446461:AAF4xNmRI_QgtI4ch4MN7v8CkuwSCqgTDJE")
    FSUB = getenv("FSUB", "rizzxbots")
    CHID = int(getenv("CHID", "-1002708353673"))
    
    # ✅ Fixed SUDO parsing with fallback to empty list
    SUDO = list(map(int, (getenv("SUDO") or "").split()))
    
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://trezlomm:gFzlvFQ3A0ttvm9y@cluster0.toyco5h.mongodb.net/")

cfg = Config()
