# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os
import glob
from flask_bootstrap import Bootstrap


app = Flask(__name__)
FileFolder = '/home/jason/'

os.chdir(FileFolder)
maps = {}

mp4_extends = '*.mp4'
jpg_extends = '*.jpg'
png_extends = '*.png'
SIZE_MB = 1024*1024
title = 'Flask Web App'
"""for fname in glob.glob(file_extends):
    if os.path.isfile(fname):
        key = fname#.decode()
        maps[key] = round(os.path.getsize(fname)/SIZE_MB,3)"""

def find_maps():
    for fname in glob.glob(mp4_extends):
        if os.path.isfile(fname):
            key = fname  # .decode()
            maps[key] = round(os.path.getsize(fname) / SIZE_MB, 3)
    for fname in glob.glob(jpg_extends):
        if os.path.isfile(fname):
            key = fname  # .decode()
            maps[key] = round(os.path.getsize(fname) / SIZE_MB, 3)
    for fname in glob.glob(png_extends):
        if os.path.isfile(fname):
            key = fname  # .decode()
            maps[key] = round(os.path.getsize(fname) / SIZE_MB, 3)
    return maps

@app.route("/")
def index():
    maps = find_maps()
    return render_template("index.html", title=title, files=maps)

@app.route("/upload", methods=['POST', 'GET'])
def upload():
    print("upload")
    if request.method == 'POST':
        for file in request.files.getlist("file"):
            print(file)
            filename = file.filename
            dest = "/".join([FileFolder, filename])
            file.save(dest)

    #return index()
    maps = find_maps()
    return redirect(url_for('index'))#redirect(url_for("index.html", title=title, files=maps))

@app.route('/download/<filename>')
def download(filename):
    fname = filename#.encode('cp936')
    return send_from_directory(FileFolder, fname, as_attachment=True)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(maps)
    app.run(debug=True, host='0.0.0.0', port=5000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
