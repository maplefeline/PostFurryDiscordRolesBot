from logging import INFO, basicConfig, captureWarnings, getLogger
from os import environ
from typing import Union

from discord import Member, Reaction, User
from discord.ext.commands import Bot

User = Union[Member, User]
basicConfig(level=INFO)
LOGGER = getLogger("fish.straycat.discordbot")


class PostFurryClient(Bot):
    async def on_error(self, event: str, *args: object, **kwargs: object) -> None:
        LOGGER.info("Error occured", event, *args, kwargs)

    async def on_ready(self) -> None:
        LOGGER.info("We have logged in as", self.user)

    async def on_reaction_add(self, reaction: Reaction, user: User) -> None:
        LOGGER.info(reaction, user)

    async def on_reaction_remove(self, reaction: Reaction, user: User) -> None:
        LOGGER.info(reaction, user)


if __name__ == "__main__":
    captureWarnings(True)
    PostFurryClient(
        "!rank",
        fetch_offline_members=False,
        guild_subscriptions=False,
        assume_unsync_clock=True,
    ).run(environ["DISCORD_TOKEN"])
