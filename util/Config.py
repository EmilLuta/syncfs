"""
Config

Reads various config sources in order of priority:
    - /etc/syncfs.conf
        - [name] section
        - [default] section
    - ~/.syncfs.conf
        - [name] section
        - [default] section

Writes ~/.syncfs.conf

"""

from configparser import ConfigParser


class Config:
    config_global = None
    config_local = None

    def __init__(self):
        config = ConfigParser()
        self.config_global = config.read('/etc/syncfs.conf')
        # TODO ~ probably doesn't work
        self.config_local = config.read('~/.syncfs.conf')
        # This most likely should read a bunch of dictionaries that you could merge.
        # Merging should be done based on priority?

    def get(self, section, name, default):
        self.config_global.get(
            section,
            name,
            fallback=self.config_local.get(
                section,
                name,
                fallback=default
            )
        )

    def set(self, section, name, value):
        if section not in self.config_local.sections:
            self.config_local.add_section(section)
        self.config_local.set(section, name, value)
