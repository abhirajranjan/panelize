# panelize
simple bar written in python with pyqt6 bindings

## Installation and Run
1. clone this repository
```bash
git clone https://github.com/abhirajranjan/panelize.git

OR

git clone git@github.com:abhirajranjan/panelize
```

2. change directory and run dependency install
```bash
cd panelize && pip install -r requirements.txt
```

3. run panel
```bash
cd src && python3 main.py
```

## Configuration
* all configs are located in config.ini file
* __[bar/main]__ section handle how bar appears and which modules are shown
*  all __[modules/*]__ are modules that are use to set configs of small elements inside the bar
* you can have multiple modules working with left, center and right side of the bar
```ini
[bar/main]
module-left = module_1 module_2 module_3
module-right = module_3 module_4
module-center = module_5
```
> Note: we have set same module (module_3) two times (in module-left and module_right), both of them are going to get executed independently.

* you can run your custom script and output that in label as well
```ini
[module/my_custom_script]
type = custom/script  # tells bar that its a custom script module
exec = uptime  # uptime is a linux command but you can use any shell command of your choice
interval = 2  # in seconds
```
> Note: type must be set __custom/script__ whenever setting up a custom script

* name after module/ in section is the name of the module that is specified in module location (module-left, module-right, module-center)
* height and width in __bar/main__ can be written as a percentage of primary screen size or pixel size
```ini
[bar/main]
height = 50%  # % is necessary o denote that it means percentage
width = 10  # this is treated as 10px wide
```

* coord in __bar/main__ denoted the x and y point of top-left point of bar. it can commonly be called left side and top padding.

## Future Plans
need of some pre defined modules like for date, time, sys tray, etc.

## Contribution
Any contribution in form of ideas, code, bug fix are heartly welcome  