'''
说明：
    @property是一种简单的方法，将get_value()和set_value()变为类的属性
    Python内置的@property装饰器就是负责把一个方法变成属性调用的
        既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
'''

class student_origin():
    '''
        普通方法，使用get和set方法
    '''
    def get_score(self):
        return self._score
    
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError("The input mast be a integer!\n")
        elif score < 0 or score >100:
            raise ValueError("Please input the correct value!")
        else:
            self._score = score

class student_property():
    '''
        使用property将get和set变成类的属性
    '''
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError("The input mast be a integer!\n")
        elif score < 0 or score >100:
            raise ValueError("Please input the correct value!")
        else:
            self._score = score


if __name__ == "__main__":
    print("-----origin-----")
    student = student_origin()
    student.set_score(77)
    print(student.get_score())

    print("-----property-----")
    stu = student_property()
    stu._score = 88
    print(stu._score)