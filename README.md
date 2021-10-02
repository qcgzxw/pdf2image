## pdf转图片
指定转换pdf文件的某页保存为图片文件


### 用法:
```shell
# exe文件可直接运行
.\dist\pdf转图片.exe --input ../test.pdf --output ../test.png --page 1

# py脚本运行需要指定poppler目录
python.exe .\pdf转图片.py --input test.pdf --output test.png --page 1
```

### 打包:
```shell
pyinstaller -F .\pdf转图片.spec
```