# -*- coding: utf-8 -*-
import getopt
import os
import sys
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def pdf_to_jpeg(pdf, jpeg, index):
    if not os.path.exists(pdf):
        print('输入文件不存在！')
        sys.exit(2)
    try:
        images = convert_from_path(
            pdf_path=pdf,
            poppler_path=resource_path(os.path.join("poppler-21.09.0", "Library", "bin"))
        )
        images[index].save(jpeg)

    except PDFInfoNotInstalledError:
        print('错误')
        sys.exit(2)
    except PDFPageCountError:
        print('pdf文件页数错误')
        sys.exit(2)
    except PDFSyntaxError:
        print('错误')
        sys.exit(2)
    except Exception as err:
        print(str(err))
        sys.exit(2)


def main(argv):
    input_pdf = ''
    output_jpeg = ''
    page = ''
    try:
        opts, args = getopt.getopt(argv, "i:o:p:", ["input=", "output=", "page="])
        for opt, arg in opts:
            if opt in ("-i", "--input"):
                input_pdf = arg
            elif opt in ("-o", "--output"):
                output_jpeg = arg
            elif opt in ("-p", "--page"):
                page = arg
        pdf_to_jpeg(input_pdf, output_jpeg, int(page) - 1)
    except getopt.GetoptError:
        print('用法：pdf转换.exe -i <input> -o <output> -p <page>')
        sys.exit(2)
    except Exception as err:
        print(str(err))
        print('用法：pdf转换.exe -i <input pdf> -o <output jpeg> -p <page>')
        sys.exit(2)


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    else:
        sys.exit(2)
    os.chdir(application_path)
    main(sys.argv[1:])
