def print_file_info(file_name):
    """
     print_file_info说明
    :param file_name:文件路径传入
    """
    f = None
    try:
        f = open(file_name, "r",encoding="utf-8")
        print(f.read())

        f.close()

    except:
        print("文件未找到，或者文件路径配置错误")

    finally:
        if f:
            f.close()

def append_to_file(file_name,date):
    """
    append_to_file说明
    :param file_name:文件路径传入
    :param date:需写入的内容
    """
    f = None

    try:
        f = open(file_name, "a", encoding="utf-8")
        f.write(date)
        f.flush()
        f.close()

    except:
        print("文件未找到，或者文件路径配置错误")

    finally:
        if f:
            f.close()

if __name__ == "__main__":
    print(print_file_info(r"D:\D.txt"))
    print(append_to_file(r"D:\D.txt", "基尼太美哦贝贝"))