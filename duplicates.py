import os


def are_files_duplicates(file_path1):
    dir_list = []
    vocabular = {}
    for tup in os.walk(file_path1):
        dir_list.append(tup)
        for lfile in tup[2]:
            if lfile in vocabular:
                index = 0
                for file_size in vocabular[lfile]:
                    if file_size == os.path.getsize(tup[0] + '/' + lfile):
                        print('Файл', lfile, 'с размером', file_size,
                              'байт существует. Расположение его дубликата: в папке', tup[0])
                        break

                    if index == len(vocabular[lfile]) - 1:
                        vocabular[lfile].append(
                            os.path.getsize(tup[0] + '/' + lfile))
                        break
                    index += 1
            else:
                vocabular[lfile] = [os.path.getsize(tup[0] + '/' + lfile)]


if __name__ == '__main__':
    pdir = input()
    are_files_duplicates(pdir)
