from SACHINxSANATANIxMUSIC.core.bot import DAXX
from SACHINxSANATANIxMUSIC.core.dir import dirr
from SACHINxSANATANIxMUSIC.core.git import git
from SACHINxSANATANIxMUSIC.core.userbot import Userbot
from SACHINxSANATANIxMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DAXX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
