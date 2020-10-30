#https://www.facebook.com/sukarna.jana.9/posts/861280437944655
#Subscribed by Sukarna Jana

import imageio
import moviepy.editor

def convert(aa='import.mp4',bb='export.mp3'):
    aa=(r'{}'.format(a))
    bb=(r'{}'.format(b))
    video=moviepy.editor.VideoFileClip(aa)
    audio=video.audio
    audio.write_audiofile(bb)
    print('converted successfully')

if __name__=="__main__":
    print(r"Enter the path of your video file:- eg:-C:\Users\VAIO\Desktop\IMPORT.mp4 or press enter")
    a=str(input("path:---"))
    print(r"Enter the path of your audio file should be expoted with name of the audio file:- eg:-C:\Users\VAIO\Desktop\EXPORT.mp3 or press enter")
    b=str(input("path:---"))
    if(a=='' or None and b=='' or None):
        convert()
    else:
        convert(a,b)
        
