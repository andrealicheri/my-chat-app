import mimetypes
from flask import Response, abort
import os

def send_file(path: str):
    full_path = os.path.join(path)
    try:
        with open(full_path, "rb") as file:
            mime_type, _ = mimetypes.guess_type(full_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            return Response(file.read(), mimetype=mime_type)
    except FileNotFoundError:
        abort(404)

def bundle_lib(path: str):
    full_path = os.path.join(path)
    file_list = os.listdir("src/lib/")
    lib_string = ""
    try:
        for file_name in file_list:
            if os.path.isfile(os.path.join("src/lib/", file_name)):
                file_extension = os.path.splitext(file_name)[1]  # Get the file extension
                if file_extension == '.js':
                    lib_string += '<script src="/lib/{}"></script>'.format(file_name)
                elif file_extension == ".css":
                    lib_string += '<link rel="stylesheet" href="/lib/{}" />'.format(file_name)
        with open(full_path, "r") as file:
            mime_type = "text/html"
            return Response(file.read().replace("</head>", lib_string + "</head>").encode('utf-8'), mimetype=mime_type)
    except FileNotFoundError:
        abort(404)
