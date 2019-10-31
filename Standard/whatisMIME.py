import filetype


def main():
    kind = filetype.guess('D:\Downloads\Apps\com.tencent.radio_3.9.2.2_26.rar')
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)


if __name__ == '__main__':
    main()
