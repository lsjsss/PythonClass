
# python中的self和cls区别
# 1 self表示一个具体的实例本身
# 如果用了staticmethod,那么就可以无视这个self,将这个方法当成一个普通的函数使用
# 2 cls 表示这个类本身
# 3 类先调用__new__方法，返回