import os

import pytest

from pylnk3 import Lnk


@pytest.mark.parametrize(
    'filename,path',
    (
        ('mounted_folder1_file1.lnk', 'Z:\\Downloads\\folder1\\file1.txt'),
        ('mounted_folder1_file2.lnk', 'Z:\\Downloads\\folder1\\file12.txt'),
        ('mounted_folder2_file1.lnk', 'Z:\\Downloads\\folder12\\file1.txt'),
        ('mounted_folder2_file2.lnk', 'Z:\\Downloads\\folder12\\file12.txt'),
    ),
)
def test_local_mounted_share(examples_path, temp_filename, filename: str, path: str):
    """This links contains both local and network path."""
    full_filename = os.path.join(examples_path, filename)
    lnk = Lnk(full_filename)
    assert lnk.path == path
    lnk.save(temp_filename)
    lnk2 = Lnk(temp_filename)
    assert lnk2.path == path


def test_local_disk_link(examples_path, temp_filename):
    filename = os.path.join(examples_path, 'local_disk.lnk')
    path = 'C:'
    lnk = Lnk(filename)
    assert lnk.path == path
    lnk.save(temp_filename)
    lnk2 = Lnk(temp_filename)
    assert lnk2.path == path


def test_local_file_link(examples_path, temp_filename):
    filename = os.path.join(examples_path, 'local_file.lnk')
    path = 'C:\\Windows\\explorer.exe'
    lnk = Lnk(filename)
    assert lnk.path == path
    lnk.save(temp_filename)
    lnk2 = Lnk(temp_filename)
    assert lnk2.path == path


def test_local_folder_link(examples_path, temp_filename):
    filename = os.path.join(examples_path, 'local_folder.lnk')
    path = 'C:\\Users\\stray\\Desktop\\New folder'
    lnk = Lnk(filename)
    assert lnk.path == path
    lnk.save(temp_filename)
    lnk2 = Lnk(temp_filename)
    assert lnk2.path == path


def test_local_send_to_fax(examples_path, temp_filename):
    filename = os.path.join(examples_path, 'send_to_fax.lnk')
    path = '%windir%\\system32\\WFS.exe'
    lnk = Lnk(filename)
    assert lnk.path == path
    lnk.save(temp_filename)
    lnk2 = Lnk(temp_filename)
    assert lnk2.path == path
