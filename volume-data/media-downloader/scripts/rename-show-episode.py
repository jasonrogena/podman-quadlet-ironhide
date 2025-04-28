#! /usr/bin/env python3

import os
import re
import shutil
import sys

from typing import Optional
from pathlib import Path

class ShowEpisode:
    show: str
    season: int
    episode: int
    extension: str

    def __init__(self, path: str, show: str, season: int, episode: int, extension: str):
        self.path = path
        self.show = show.strip('.').strip().lower().replace(' ', '.')
        self.season = season
        self.episode = episode
        self.extension = extension.lower()
    
    @classmethod
    def get_episode(cls, path: str) -> Optional["ShowEpisode"]:
        basename = os.path.basename(path)
        m = re.search(r'(?P<show>.+)(s|S)(?P<season>\d+)(e|E)(?P<episode>\d+).*\.(?P<extension>\w+)', basename)
        if m is None:
            return None
        return ShowEpisode(path=path,show=m.group("show"),season=m.group("season"),episode=m.group("episode"),extension=m.group("extension"))

    def get_parent_dir(self) -> str:
        return f"{self.show}/season{self.season}/{self.show}.s{self.season}e{self.episode}"

    def get_path(self) -> str:
        return f"{self.get_parent_dir()}/{self.show}.s{self.season}e{self.episode}.{self.extension}"


    def move_to(self, dest: str):
        src_parent_dir = Path(self.path).parent.absolute()
        os.makedirs(f"{dest}/{self.get_parent_dir()}", exist_ok=True)
        shutil.move(self.path, f"{dest}/{self.get_path()}")
        print(f"Moved {self.path} to {dest}/{self.get_path()}")


episode_path = sys.argv[1]
dest = sys.argv[2]

if episode_path is None or dest is None:
    print(f"episode_path: {episode_path} or dest: {dest} is not set. Exiting")
    exit(1)

ep = ShowEpisode.get_episode(path=episode_path)
if ep is None:
    print(f"Could not determine the episode for {episode_path}")
    exit(1)
ep.move_to(dest=dest)
