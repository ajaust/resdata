from conan import ConanFile


class ResdataConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    tool_requires = "m4/1.4.20"

    def requirements(self):
        self.requires("backward-cpp/1.6")
        self.requires("catch2/2.13.9")
        self.requires("fmt/8.0.1")

    def package_info(self):
        self.conf_info.define("tools.build:verbosity", "debug")

    def configure(self):
        self.options["catch2"].with_main = True
        if self.settings.os == "Macos":
            self.options["backward-cpp"].stack_details = "backtrace_symbol"
