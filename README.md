Step 1) open a terminal, sudo apt install the following:
chromium-chromedriver
gnome-terminal
Step 2) in a terminal, pip install -r requirements.txt
Step 3) open viewBot.py and verify the driver address is /usr/bin/chromedriver
Step 4) in the terminal cd into /usr/bin. Verify chromedriver installed in the correct directory. If not cd ..; cd lib to check for the chromedriver file.
Step 5) Install pi-apps using the command: wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash . After pi-apps has installed run pi-apps in a terminal or launch pi-apps from the search menu and install tor.
Step 6) Verify the tor location in viewBot.py is set to the location on your pi that tor is installed to.
Fin) If the files are installed in a different location change the paths in viewBot.py to wherever you find the files.

Downgrade Chromium/chromedriver
0.5.) If chromedriver was installed from the step above, uninstall chrome driver. sudo apt remove chromium-chromedriver
1.) With pi-apps installed, install chromium downgrade application (Found under internet apps)
2.) Run app and Downgrade chromium (Match next step; I got this to work with version 92)
3.) Download new chrome driver from this thread -> https://stackoverflow.com/questions/38732822/compile-chromedriver-on-arm
4.) place it in the folder /usr/bin/
