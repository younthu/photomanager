# photomanager
manage my photos

# roadmap

1. 扫描某目录下的所有文件
2. 读出文件的基本属性: 文件名，路径，大小，修改时间，作者

# refer
[https://github.com/pallets/click](https://github.com/pallets/click)


# issues
1. pathlib 不认识 `~/Desktop`这种路径，需要传`/Users/userxxx/Desktop`才能正常工作. 
    1. 已经解决。 `Path('~/Desktop').expanduser()` 可以得到转义后的路径.
1. 