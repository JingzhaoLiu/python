from zipfile import ZipFile
import os


def get_all_file_paths(directory):
    file_paths = []

    # 把所有的文件夹以及子文件夹、以及文件全部搞出来
    for root, directories, files in os.walk(directory):
        for filename in files:
            # 得到完全路径
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def main():
    directory = './Junit'

    file_paths = get_all_file_paths(directory)

    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    with ZipFile('my_python_files.zip', 'w') as zip:
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')


if __name__ == "__main__":
    main()