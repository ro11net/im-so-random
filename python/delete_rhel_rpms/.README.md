Mount the BaseOS RHEL iso in your rhel machine

cp iso to somewhere on your machine

list the default packages in the rhel image
```shell
ll <path-to-iso-files>/Appstream/Packages > ./Appstream
```

list the current packages installed on your machine
```shell
yum list installed > ./installed
```
  
Move this python script to the current directory where you saved the file "Appstream" and "installed"
  
run the python script

make the delete_packages.sh file executable

chmod +x delete_packages.sh

move the delete_packages.sh file to the Appstream/Packages directory

```shell
mv delete_packages.sh <path-to-iso-files>/Appstream/Packages
```

Run the shell script inside the Packages directory

```shell
delete_packages.sh <path-to-iso-files>/Appstream/Packages

./delete_packages.sh
```
