#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class DoctestConan(ConanFile):
    name = "doctest"
    version = "2.0.0"
    url = "https://github.com/bincrafters/conan-doctest"
    homepage = "https://github.com/onqtam/doctest"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "C++98/C++11 single header testing framework"
    license = "MIT"
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"
    
    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*doctest.h*", dst="include", src=os.path.join(self._source_subfolder, "doctest"))

    def package_id(self):
        self.info.header_only()
