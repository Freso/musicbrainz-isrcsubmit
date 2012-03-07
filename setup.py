#!/usr/bin/python2

from distutils.core import setup
from isrcsubmit import isrcsubmit_version

setup(name="isrcsubmit",
        version=isrcsubmit_version,
        description="submit ISRCs from disc to MusicBrainz",
        long_description=open("README.md").read(),
        author="Johannes Dewender",
        author_email="brainz@JonnyJD.net",
        url="https://github.com/JonnyJD/musicbrainz-isrcsubmit",
        scripts=["isrcsubmit.py"],
        license="GPL3",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Environment :: MacOS X",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 2.5",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Topic :: Database :: Front-Ends",
            "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping",
            "Topic :: Text Processing :: Filters"
            ]
        )

# vim:set shiftwidth=4 smarttab expandtab:
