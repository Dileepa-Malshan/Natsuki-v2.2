# This file is part of EzilaX (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from telethon import TelegramClient

from EzilaXBotV.conf import get_int_key, get_str_key

TOKEN = get_str_key("TOKEN", required=True)
NAME = TOKEN.split(":")[0]

tbot = TelegramClient(
    NAME, get_int_key("API_ID", required=True), get_str_key("API_HASH", required=True)
)

# Telethon> V3.0
tbot.start(bot_token=TOKEN)