from conans import ConanFile, tools, CMake
import os


class DoctestConan(ConanFile):
    name = "doctest"
    version = "2.3.4"
    url = "https://github.com/bincrafters/conan-doctest"
    homepage = "https://github.com/onqtam/doctest"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "C++11/14/17/20 single header testing framework"
    topics = ("conan", "doctest", "tdd", "testing", "testing-framework")
    license = "MIT"
    exports = ["LICENSE.md"]
    no_copy_source = True
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        sha256 = "d5d9c5b6d2c8737acd64823805d3419c7d49cd4e809fa92c326280367bb694b2"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["DOCTEST_WITH_TESTS"] = False
        cmake.definitions["DOCTEST_WITH_MAIN_IN_STATIC_LIB"] = False
        cmake.configure(build_folder=self._build_subfolder, source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs.append(os.path.join("include", "doctest"))

    def package_id(self):
        self.info.header_only()
