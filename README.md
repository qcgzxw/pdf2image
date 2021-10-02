## pdf转图片
指定转换pdf文件的某几页保存为图片文件


### 用法:
```shell
# exe文件可直接运行
.\dist\pdf转图片.exe --input ../test.pdf --output ../test.png --start 1 --end 5

# py脚本运行需要指定poppler目录
python.exe .\pdf转图片.py --input test.pdf --output test.png --start 1 --end 5
```

### 打包:
```shell
pyinstaller -F .\pdf转图片.spec
```