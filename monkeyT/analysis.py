

class Analysis():
    def __init__(self):
        self.filepath = input('请输入你的文件地址如F:/1.txt:')
        self.errnum = 0

    def open_file(self):
        afile = open(self.filepath,'r')
        print('*****结果分析中，请耐心等待！*****')
        for num,value in enumerate(afile):
            self.analysis_file(num,value)
        if self.errnum == 0:
            print('一切正常哦^_^')

    def analysis_file(self,n,v):
        linenum,linvalue = n + 1,v
        if 'ANR' in linvalue:
            self.errnum += 1
            print('发现错误ANR，行号为:',linenum,'异常内容为：',linvalue)
        elif 'Exception' in linvalue:
            self.errnum += 1
            print('发现异常Exception，行号为：',linenum,'异常内容为：',linvalue)
        
        
               
if __name__ == '__main__':
    analysismoneky = Analysis()
    analysismoneky.open_file()
    



