from logging import captureWarnings, getLogger
from logging.handlers import SysLogHandler
from typing import Union

from discord import Bot, Member, Message, Reaction, User

User = Union[Member, User]

LOGGER = getLogger("fish.straycat.discordbot")
LOGGER.addHandler(SysLogHandler())


class PostFurryClient(Bot):
    async def on_error(self, event: str, *args: object, **kwargs: object) -> None:
        LOGGER.info("Error occured", event, *args, kwargs)

    async def on_ready(self):
        LOGGER.info("We have logged in as", self.user)

    async def on_message(self, message: Message) -> None:
        if not message.content.startswith("!rank "):
            return

        content = message.content[5:].strip()

        if content.startswith("$hello"):
            await message.channel.send("Hello!")

    async def on_reaction_add(self, reaction: Reaction, user: User) -> None:
        pass

    async def on_reaction_remove(self, reaction: Reaction, user: User) -> None:
        pass


if __name__ == "__main__":
    captureWarnings(True)
    PostFurryClient(
        "!rank",
        fetch_offline_members=False,
        guild_subscriptions=False,
        assume_unsync_clock=True,
    ).run("DISCORD_TOKEN")
