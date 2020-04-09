
# ..之所以无法使用，可能是因为该方法可以运行于相对导入中，但是该标识符并不存在于环境变量中
from source.com import monster

if __name__ == "__main__":
    monster = monster.Slime(10, 3, 2, 1)
    monster.sayHello()