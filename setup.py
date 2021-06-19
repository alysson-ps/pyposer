import subprocess
import os

print("[*] Installing requirements.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
print("[*] Installing ppm to /usr/share/ppm..")
subprocess.Popen("mkdir /usr/share/ppm/;cp -rf * /usr/share/ppm/",
                 shell=True).wait()
print(
    '[*] Done. Add export PATH="$PATH:/usr/share/ppm/src" in your .bashrc or .zshrc'
)
print("[*] Finished. Run 'ppm' to start the Python Package Maneger.")