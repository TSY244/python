import tarfile
import zipfile
import py7zr
import os
import shutil
def get_file_extension(filename):
    _, extension = os.path.splitext(filename)
    return extension
def find_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list
def extract_innermost_file(path,base):
    tmp=path
    for i in range(1000000):
        if os.path.isdir(tmp):
            tmp=find_files(tmp)[0]
        if  tmp.endswith(".zip")or tmp.endswith(".7z")or tmp.endswith(".tar.gz") or tmp.endswith('.gz')or tmp.endswith(".tar"):
            # 解压.tar.gz文件
            # 解压.zip文件
            if tmp.endswith(".zip"):
                with zipfile.ZipFile(tmp, "r") as zip:
                    inner_filepath = zip.namelist()[0]  # 获取第一个文件路径
                    zip.extract(inner_filepath)
                    zip.close()
            elif tmp.endswith(".7z"):
                with py7zr.SevenZipFile(tmp, mode='r') as archive:
                    inner_filepath = archive.getnames()[0]  # 获取第一个文件路径
                    archive.extract(inner_filepath)
                    archive.close
            elif tmp.endswith(".tar"):
                with tarfile.open(tmp, "r") as tar:
                    inner_filepath = tar.getnames()[0]  # 获取第一个文件路径
                    tar.extract(inner_filepath)
                    tar.close()
            else:
                with tarfile.open(tmp, "r:gz") as tar:
                    inner_filepath = tar.getnames()[0]  # 获取第一个文件路径
                    tar.extract(inner_filepath)
                    tar.close()
            os.unlink(tmp)
            tmp0=inner_filepath
            if os.path.isdir(inner_filepath):
                inner_filepath=find_files(inner_filepath)[0]
            tmp=os.path.join(base, 'tmp'+get_file_extension(inner_filepath))
            shutil.copy2(inner_filepath, tmp)
            if get_file_extension(inner_filepath) not in ['.zip', '.tar.gz', '.gz','.7z']:
                break
            if os.path.isdir(tmp0):
                shutil.rmtree(tmp0)
            else:
                os.remove(tmp0)

innermost_file = extract_innermost_file(r"G:\CTF\ziploop.tar",r"G:\CTF\output")