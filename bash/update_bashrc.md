# Updating your .bashrc to source environment variables from files in a directory

I am working on a script which pulls a lot of variables and functions from multiple files.  (I have each function segregated into it's own file in order to improve the readablity of the script and make it easier for the rest of the teamn to make changes.

below is an example tree of my files:

```bash
/usr/lib/app/
            └── scripts
                ├── main.sh
                └── source
                    ├── update_bashrc.sh
                    ├── function1.sh
                    ├── function2.sh
                    ├── function3.sh
                    └── variables
```

The script requires environment variables to be set for the duration of the script in order to set configurations as well as run kubectl commands later on once Kubernetes has been installed.

It's easy enough to source the entire directory with the source command:

```shell
source <(cat /usr/lib/app/scripts/source/*)
```
but this only works for the current shell the script is using.

#
Once the script is complete, I still want all of the functions and environment variables available as command line tools for administrative actions and troubleshooting.

To do this I have create a file in the source directory named `update_bashrc.sh` containing the function `update_bashrc` (I know I don't need to name the file with the .sh extension, but I like the way vim and vscode color it when I do)

The easy way out would be to add it the end of the .bashrc file:

```bash
update_bashrc () {
	cat >> /root/.bashrc <<EOF
source <(cat /usr/lib/app/scripts/source/*)
EOF
}

```
This works great unless you run it more than once and the script just keeps appending the source line to the end of the .bashrc.  It probably wont hurt anything but it sure doesn't look very clean:

```bash
# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

source <(cat /usr/lib/app/scripts/source/*)
source <(cat /usr/lib/app/scripts/source/*)
source <(cat /usr/lib/app/scripts/source/*)
source <(cat /usr/lib/app/scripts/source/*)
source <(cat /usr/lib/app/scripts/source/*)
source <(cat /usr/lib/app/scripts/source/*)
source <(cat /usr/lib/app/scripts/source/*)
---snippet---
```

I would rather check to see if the line exists already so I will use grep to accomplish that for me:

> **NOTE** Make sure you place an escape character "\" before the asterisk or it will not read right

```bash
update_bashrc () {
	if ! grep -e "source <(cat /usr/lib/app/scripts/source/\*)" /root/.bashrc; then
		cat >> /root/.bashrc <<EOF
source <(cat /usr/lib/app/scripts/source/*)
EOF
        echo "Source successfully added to the root bashrc file"
	else
		echo "source already present in the root bashrc. Doing nothing."
	fi
}
```

This is the resulting output

```shell
# ./main.sh 
source added to the root bashrc file
```

And if I run it again:

```shell
./main.sh 
source <(cat /usr/lib/app/scripts/source/*)
source already present in the root bashrc
```

and again...

```shell
./main.sh 
source <(cat /usr/lib/app/scripts/source/*)
source already present in the root bashrc
```

and the .bashrc file still only wrote it once
```shell
# cat ~/.bashrc
# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

source <(cat /usr/lib/app/scripts/source/*)
```

