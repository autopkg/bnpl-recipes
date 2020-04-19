#!/usr/bin/env python

import os, subprocess

from autopkglib import Processor, ProcessorError


__all__ = ["IzPackExecutor"]


class IzPackExecutor(Processor):

    """Runs IzPack installer with all install options checked."""
    input_variables = {
        "app_root": {
            "required": True,
            "description": "Path where the app should be temporarily unpacked (installed in this case)"
        },
        "app_installer": {
            "required": True,
            "description": "Path to IzPack installer JAR"
        }
    }
    output_variables = {
    }
    description = __doc__

    def main(self):
        real_path = os.path.realpath(__file__)

        expect_path = real_path.replace(".pyc", "-install.expect").replace(".py", "-install.expect")
        subprocess.call(["expect", expect_path, self.env["app_installer"], self.env["app_root"]])

        zsh_path = real_path.replace(".pyc", "-get_version.zsh").replace(".py", "-get_version.zsh")
        izpack_app_ver = subprocess.check_output(["zsh", zsh_path, self.env["app_root"]]).decode('ascii').replace("\r\n", "").replace("\r", "").replace("\n", "")
        self.env["izpack_app_ver"] = izpack_app_ver
        print(izpack_app_ver)


if __name__ == "__main__":
    processor = IzPackExecutor()
    processor.execute_shell()
