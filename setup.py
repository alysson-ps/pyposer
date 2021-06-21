# import subprocess
# import os

# print("[*] Installing requirements.txt...")
# subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
# print("[*] Installing ppm to /usr/share/ppm..")
# subprocess.Popen("mkdir /usr/share/ppm/;cp -rf * /usr/share/ppm/",
#                  shell=True).wait()
# print(
#     '[*] Done. Add export PATH="$PATH:/usr/share/ppm/src" in your .bashrc or .zshrc'
# )
# print("[*] Finished. Run 'ppm' to start the Python Package Maneger.")

from setuptools import setup, find_packages

setup(
    name='ppm',
    version='0.1.0',
    description='Python Packeage Manager',
    packages=find_packages("src"),
    package_dir={"": "src/ppm_pkg"},
    author='Alisson Santos',
    author_email='dev.alysson@gmail.com',
    entry_points={
        'console_scripts': [
            'ppm = ppm_pkg.ppm:main',
        ],
    },
    url=
    'https://github.com/alysson3dev/pyposer',  # Provide either the link to your github or to your website
    download_url=
    'https://github.com/alysson3dev/pyposer/archive/refs/tags/0.1.0.tar.gz',
    keywords=['PPM', 'PIP', 'PACKAGE', 'KEYWORDS'],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
)
