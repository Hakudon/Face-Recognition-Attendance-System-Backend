import os
import uuid
from io import BytesIO

from flask import current_app as app
from PIL import Image
from werkzeug.datastructures import FileStorage
from database import DB
from . import helper_functions as hf


def save_image(file: FileStorage) -> str:
    """
    Checks if the file is valid and saves it.
    Args:
        file (FileStorage): A file uploaded to flask obtained from request.files
    Returns:
        str: The filename of the saved file if its valid else assertion error is thrown
    """

    assert file.filename, "No image selected."
    extension = hf.is_image(file.filename)

    filename = f"{uuid.uuid4()}.{extension}"
    DB.dbx.files_upload(file.stream.read(), path=f"/images/{filename}")

    return filename


def remove_image(filename: str):
    try:
        pass
    #! TODO: Remove the image from dropbox

    except FileNotFoundError:
        print("ERROR: Uploaded file accidentally removed")
