# Native-backlight

**Why ?** Because `redshift` mess things up and override most system backlight control. And because it is useless to have a color shift with a full bright monitor, we have to use another approch to control brightness.
Also, most windows mananger like gnome or kde might provide some way to control color shift and brightness control, it is not always true one using more lightweight wm (I use `i3` and it does not give such control natively since it is a wm and not a gaz factory). 
**How ?** This soft, registered as a service, provide a control to the file responsible to set the brightness value of the monitor (thanks to unix, most configration, even low level ones, are done using files).

## Install

just run :

```bash
chmod +x install.sh
sudo ./install.sh

sudo systemctl enable native-backlight.service
sudo systemctl start native-backlight.service
```

and that's all. Now you can have control the brightness using:

```bash
# increase the brightness
/opt/native-backlight/bin/nb-client.py increase

# decrease the brightness
/opt/native-backlight/bin/nb-client.py decrease

# reset to default / max value
/opt/native-backlight/bin/nb-client.py reset
```

## config

the few things you might haev a look:

* `port`: set the communcation port. Since it use a client/server architecture to manage system file without tempering with access right, it must communicate through a port. Pick the one you want
* `max`: the max brightness value. Mandatory since, if you put too high value in the brightness system file, you will get an error
* `default`: the standart birghtness you want. Most of the time, it should be the same as max
* `threshold`: the minimum time in ms between two brightness change
* `step`: the value used to increase or decrease the brightness. Low value will bring a more precise control. If you put low value, you should also decrease the `threshol` in order to have a smoother experience
* `brightness_file`: the file used by linux to contorl brithness.

## i3

to bind the control command to keyboard shortcut, I had to put those two lines in my `i3/config` file :

```
bindsym XF86MonBrightnessDown exec "/opt/native-backlight/bin/nb-client.py decrease"
bindsym XF86MonBrightnessUp exec "/opt/native-backlight/bin/nb-client.py increase"
```

the key name has been found using `xev` to show X events.

## limitation

Right now, it is more a (usasable) proof of concept than a full feature soft. It might show limitation:
* with multiple monitor. I will adapt it if requested or if I, myself, feel the need.
* with a `default` value different than the `max` value. It will start with the `max` brightness unless the command `/opt/native-backlight/bin/nb-client.py reset` is launched.
* wayland... it shouldn't make any difference, either wayland or X, but I didn't test it, so I can't be sure.
* other not known ?

