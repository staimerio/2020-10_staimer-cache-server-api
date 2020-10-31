# Os
import os

# Shutil
import shutil


def rmtree(path):
    """Delete all files in a directory

    :param path: Path of the directory
    """
    shutil.rmtree(path)


def mkdir(path):
    """Create a directory

    :param path: Path of the directory
    """
    os.mkdir(path)


def isfile(filepath):
    """Check if a file exists

    :param filepath: Path of the file
    """
    return os.path.isfile(filepath)


def isdir(path):
    """Check if a file exists

    :param path: Path of the directory
    """
    return os.path.isdir(path)


def get_content_from_file(fname, mode="rb"):
    """Get all content from a file

    :param fname: Name of the file to get information.
    """

    """Open the file"""
    _file = open(fname, mode)
    """Read the file"""
    _content = _file.read()
    """Close the file"""
    _file.close()
    """Return data"""
    return _content


def save_content_in_file(filepath, content, mode="wb"):
    """Write content in a file

    :param filepath: Path of the file to write information.
    :param content: Content to sabe in the file
    :param mode: Kind of mode to open the file
    """
    """Open the file"""
    _file = open(filepath, mode)
    """Write the file"""
    _file.write(content)
    """Close the file"""
    _file.close()
