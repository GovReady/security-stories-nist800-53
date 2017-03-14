#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Make markdown file versions of issue-pack user story files

LICENSE

ComplianceLib SystemCompliance is a class for representing compliance as code for an information system.
Copyright (C) 2016  GovReady PBC.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


Example python CLI
------------------

python makemd.py


"""

__author__ = "Greg Elin (gregelin@govready.com)"
__version__ = "$Revision: 0.1.0 $"
__date__ = "$Date: 2017/03/14 20:13:00 $"
__copyright__ = "Copyright (c) 2017 GovReady PBC"
__license__ = "GNU General Public License v3 (GPLv3)"

import os
import json
import yaml
import re
import sys
import glob

if sys.version_info >= (3, 0):
    from urllib.parse import urlparse
    from urllib.request import urlopen
if sys.version_info < (3, 0) and sys.version_info >= (2, 5):
    from urlparse import urlparse
    from urllib2 import urlopen

print ("Generating markdown files from source Issue Pack YAML files")

# read all yaml files
path = "./"

# for each yaml file
for yaml_file in glob.glob( os.path.join(path, '*.yaml') ):

    # ignore template.yaml
    if yaml_file == "{}template.yaml".format(path):
        continue

    # log file working on
    print("processing {}".format(yaml_file.strip(".yaml")))

    # read yaml file
    yaml_stories = yaml.load(open(yaml_file,"r"))

    # set up empty string
    md_text = ""

    # append issue pack name
    md_text += "# {}\n\n".format(yaml_stories['name'])

    # for each story in yaml file
    for issue in yaml_stories['issues']:

        # append title as markdown to md_text
        # print(issue['title'][0:30])
        md_text += "## {}\n".format(issue['title'])

        # append body as markdown to md_text
        # print(issue['body'][0:30])
        md_text += "{}".format(issue['body'].encode('utf-8','ignore'))

    # write md_text to file
    with open("{}{}.md".format(path, yaml_file.strip(".yaml")), "w") as md_file:
        md_file.write(md_text)

print("Whew! Done")





