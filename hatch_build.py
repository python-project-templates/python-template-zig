from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from pydust.build import build


class BuildZig(BuildHookInterface):
    PLUGIN_NAME = "build_zig"

    def initialize(self, version, build_data):
        build()
        return super().initialize(version=version, build_data=build_data)


if __name__ == "__main__":
    build()

