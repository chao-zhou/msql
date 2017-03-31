
import xml.etree.ElementTree
from os import path

import config


class ProjectFile:
    def __init__(self):
        self.project_path = path.join(config.BASE_DIR, r"Common.DataLayer\Common.DataLayer.csproj")
        self.root = xml.etree.ElementTree.parse(self.project_path).getroot()
        self.res = {}
        self.content = ""
        self.loaded = 0

    def load(self):
        for c in self.root.iter("{http://schemas.microsoft.com/developer/msbuild/2003}EmbeddedResource"):
            include_path = c.get("Include")
            self.res[include_path] = c

        with open(self.project_path, 'r', encoding="utf8") as f:
            self.content = f.read()

        self.loaded = 1

    def get_res(self, include_path):
        return self.res.get(include_path, None)

    def rename(self, src, dst):
        with open(self.project_path, 'w', encoding="utf8") as f:
            self.content = self.content.replace(src, dst)
            f.write(self.content)
