import os
import datetime
import sys
import argparse
from moviepy.editor import VideoFileClip
file_path='/Volumes/DOC/baidu/piano/02 宋大叔教音乐 伴奏/02 宋大叔教音乐 伴奏'
file_type='mp4'
filelist = []
ftime = 0.0
def tongji():
    a= os.walk(file_path)
    ftime = 0.0
    for x,y,z in a:# walk格式，x是路径 y[] z是文件名
        for name in z:
            fname = os.path.join(x, name)
            if fname.endswith(file_type):
                clip = VideoFileClip(fname)
                s2=35-len(name)+(len(name)-len(str_zhogwen(name))*2)
                #print(str_zhogwen(name))
                print(name+' '*(s2),str(int(clip.duration/60))+'分钟')
                ftime += clip.duration
    print("共 %d 秒: " % ftime+' = '+str(int(ftime/3600))+'小时')
def str_zhogwen(str):
    s1=[]
    for s in str:
    # 中文字符范围
        if '\u4e00' <= s <= '\u9fff':
            s1.append(s)
    return s1 
def test():
    a ='34大调进入关系小调.mhjhjhjhjhp4'
if __name__ == '__main__':
    tongji()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description='Compute Total Time of a Series of Videos')
#     parser.add_argument("--path", metavar="PATH", default=".",
#                         help="the root path of the videos(default: .)")
#     parser.add_argument("--type", metavar="TYPE", default=".mkv",
#                         help="the type of the videos(default: .mkv)")
#     args = parser.parse_args()
#     filelist = []
#     for a, b, c in os.walk(args.path):
#         for name in c:
#             fname = os.path.join(a, name)
#             if fname.endswith(args.type):
#                 filelist.append(fname)
#     ftime = 0.0
#     for item in filelist:
#         clip = VideoFileClip(item)
#         ftime += clip.duration
#     print("%d seconds: " % ftime,str(datetime.timedelta(seconds=ftime)))
#     print (int(ftime)/3600)
