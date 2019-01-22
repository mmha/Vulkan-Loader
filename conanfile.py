from conans import ConanFile, CMake, tools

class VulkanLoaderConan(ConanFile):
    name = "vulkan-loader"
    settings = "os", "arch", "build_type", "compiler"
    version = "1.1.97"
    requires = "vulkan-headers/[>=1.1.97]@mmha/testing"
    exports_sources = "*", "!.git"
    no_copy_source = True
    options = {
        "shared": [False, True]
    }
    default_options = {
        "shared": True
    }

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_STATIC_LOADER"] = self.options.shared
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
