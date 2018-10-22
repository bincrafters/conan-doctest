#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class DoctestConan(ConanFile):
    name = "doctest"
    version = "2.0.0"
    url = "https://github.com/bincrafters/conan-doctest"
    description = "C++98/C++11 single header testing framework"
    license = "MIT"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/onqtam/doctest"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)
        #Rename to self.source_subfolder is a convention to simplify later steps

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*doctest.h*", dst="include", src=os.path.join(self.source_subfolder,"doctest"))

    def package_id(self):
        self.info.header_only()
