import itertools
import json
import re

# Split lines in installed packages
installed_packages = []

with open('./installed', 'r') as f:
    data = f.read()

for line in data.split("\n"):
    if "@" in line:
        installed_packages.append(line)
import json

output = "#!/bin/bash\n"

# Split lines in packages from iso
iso_packages = []

with open('./BaseOS', 'r') as f:
    data = f.read()

for line in data.split("\n"):
    if "rpm" in line:
        iso_packages.append(line)

# Split lines in installed packages
installed_packages = []

with open('./installed', 'r') as f:
    data = f.read()

for line in data.split("\n"):
    if "@" in line:
        installed_packages.append(line)

# Separate packages names from the above lists
data = {
    'iso_packages' : [],
    'installed_packages' : [],
    'keep' : [],
    'package' : [],
    'version': [],
    'osnotclean' : [],
    'ostype' : [],
    'iso_pieces' : []
}

for item in installed_packages:
    raw_data = [i for i in item.split(".") if i != '']
    raw_data1 = [i for i in item.split(" ") if i != '']
    raw_data2 = [i for i in re.split("\s|(?<!\d)[,.](?!\d)", item) if i != '']
    data['iso_pieces'].append(
        {
            "name" : raw_data[0],
            "ver" : raw_data1[1],
            "os" : raw_data2[1]
        }
    )

rpm_list = []
installed_list = []
for item in data['iso_pieces']:
    name = item['name']
    version = item['ver']
    os = item['os']
    installed_list.append(str(name + "-" + version + "." + os + ".rpm"))

for item in iso_packages:
    raw_data = [i for i in item.split(" ") if i != '']
    rpm_list.append(raw_data[8])

main_list = list(set(rpm_list).difference(installed_list))

print(installed_list)

for item in main_list:
    output += "rm -rvf " + item + "\n"

with open("delete_base_os_packages.sh", 'w', newline='\n') as f:
    f.write(output)

