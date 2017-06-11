In order to distribute an application without python itself:
pip3.6 install pyinstaller
pyinstaller --onefile --windowed frontend.py (did not worked for me https://github.com/pyinstaller/pyinstaller/issues/2286)
