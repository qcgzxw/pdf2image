# -*- coding: utf-8 -*-
import getopt
import os
import sys
from pdf2image import convert_from_path
from PIL import Image
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def image_merge(image1, image2):
    w1, h1 = image1.size
    w2, h2 = image2.size
    img = Image.new('RGB', (max(w1, w2), h1 + h2), 'white')
    img.paste(image1)
    img.paste(image2, (0, h1))
    return img


def pdf_to_jpeg(pdf, jpeg, start, end):
    if not os.path.exists(pdf):
        print('输入文件不存在！')
        sys.exit(2)
    try:
        images = convert_from_path(
            pdf_path=pdf,
            poppler_path=resource_path(os.path.join("poppler-21.09.0", "Library", "bin")),
            first_page=start,
            last_page=end,
        )
        if len(images) == 1:
            images[0].save(jpeg)
        elif len(images) > 1:
            first_image = images.pop(0)
            for image in images:
                first_image = image_merge(first_image, image)
            first_image.save(jpeg)
        else:
            print('pdf文件页数错误')
            sys.exit(2)

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
    start = 0
    end = 0
    try:
        opts, args = getopt.getopt(argv, "i:o:s:e:", ["input=", "output=", "start=", "end="])
        for opt, arg in opts:
            if opt in ("-i", "--input"):
                input_pdf = arg
            elif opt in ("-o", "--output"):
                output_jpeg = arg
            elif opt in ("-s", "--start"):
                start = int(arg)
            elif opt in ("-e", "--end"):
                end = int(arg)
        pdf_to_jpeg(input_pdf, output_jpeg, start, end)
    except getopt.GetoptError:
        print('用法：pdf转换.exe -i <input> -o <output> -s <start page> -e <end page>')
        sys.exit(2)
    except Exception as err:
        print(str(err))
        print('用法：pdf转换.exe -i <input> -o <output> -s <start page> -e <end page>')
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
