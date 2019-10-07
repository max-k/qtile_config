#! /bin/bash

# arandr configuration
read -r -a screens <<< "$(xrandr --query | grep ' connected' | awk '{print $1}' | xargs)"
if [[ " ${screens[*]} " =~ " Virtual1 " ]]; then
    xrandr --newmode "1920x1080_60.00" 173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
    xrandr --addmode Virtual1 "1920x1080_60.00"
    xrandr --output Virtual1 --mode "1920x1080_60.00"
elif [[ " ${screens[*]} " =~ " DVI-I-1-1 " && " ${screens[*]} " =~ " DVI-I-2-2 " ]]; then
    ~/.screenlayout/tri-screens-displaylink.sh
elif [[ " ${screens[*]} " =~ " HDMI-1 " && " ${screens[*]} " =~ " DP-1 " ]]; then
    ~/.screenlayout/tri-screens.sh
elif [[ " ${screens[*]} " =~ " eDP1 " && " ${screens[*]} " =~ " DP1 " ]]; then
    # ~/.screenlayout/dual-screen-orange.sh
    ~/.screenlayout/default.sh
else
    ~/.screenlayout/default.sh
fi

# gconf settings
gsettings set org.gtk.Settings.FileChooser startup-mode cwd
gsettings set org.gtk.Settings.FileChooser window-size '(840, 630)'

# Xscreensaver startup
# xscreensaver -no-capture-stderr -no-splash &

# wallpaper configuration
hostname="$(hostname -f)"
if [[ "$hostname" == "maxpad.local" ]]; then
    feh --bg-fill ~/images/nuda-sketch.jpg
elif [[ "$hostname" == "workport.local" ]]; then
    feh --bg-scale ~/images/notwindows800.png
else
    feh --bg-scale ~/images/notwindows800.png
fi

# Compton compositor
if [[ "$(hostname)" =~ .*vm ]]; then
    compton -bc --backend=xrender
else
    compton -bc --backend=glx --vsync=opengl --glx-no-rebind-pixmap
fi

# Enable vbox guest features
if [[ "$(hostname)" =~ .*vm ]]; then
    VBoxClient-all &
fi

# Launch PulseAudio systray
pasystray &

# Launch Blueman applet
if [[ ! ( "$(hostname)" =~ .*vm ) ]]; then
    for id in $(sudo rfkill | grep bluetooth | awk '{print $1}'); do
        sudo rfkill block "$id"
        sudo rfkill unblock "$id"
        break
    done
    blueman-applet &
fi

# Launch wicd-gtk
#wicd-client -t &

# Launch redshift
redshift-gtk &

# Launch udiskie (req by spacefm)
# udiskie -t &

# Launch SpaceFM
# spacefm -d &

# Launch PCmanFM
pcmanfm -d &

# Enable numlock
numlockx

# Screensaver inhibitor
#~/projects/lightsonplus/lightson+ -d 220 &
caffeine &

# Lauch polkit agent
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
