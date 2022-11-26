import os

from flask import Flask, render_template, request, send_from_directory


upload_folder = os.path.join(os.getcwd(), 'uploads')


def __clean_folder():
    for file in os.listdir(upload_folder):
        print('[*] DELETING: {}'.format(file))
        os.remove(os.path.join(upload_folder, file))


def index():
    return render_template('index.html')


def upload():
    file = request.files['file']
    if not file:
        return 'Not found file', 400

    __clean_folder()
    filename = file.filename.replace(' ', '_')
    print('[*] UPLOADING: {}'.format(filename))

    file.save(os.path.join(upload_folder, filename))
    url = request.url_root + 'download/' + filename

    print('[*] URL: {}'.format(url))
    return url


def download(filename):
    return send_from_directory(upload_folder, filename)


def setup_route(app: Flask):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/upload', 'upload', upload, methods=['POST'])
    app.add_url_rule('/download/<filename>', 'download', download)
