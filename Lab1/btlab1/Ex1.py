from gmail import GMail, Message
from random import choice
import datetime

gmail = GMail('cookiedeptraivl@gmail.com','a06111997')

stickness_list = ["ngứa tay", "thất tình", "cô mắng"]


template = '''<p>m&igrave;nh về m&igrave;nh c&oacute; nhớ ta&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /></p>
<p>mười lăm năm ấy thiết tha mặn n&ocirc;ng&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-foot-in-mouth.gif" alt="foot-in-mouth" /></p>
<p>m&igrave;nh về m&igrave;nh c&oacute; nhớ&nbsp; kh&ocirc;ng&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-frown.gif" alt="frown" /></p>
<p>nh&igrave;n c&acirc;y nhớ n&uacute;i nh&igrave;n s&ocirc;ng nhớ nguồn, h&acirc;y h&acirc;y h&acirc;y h&acirc;y&nbsp;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p> 
'''
stickness = 'đốt trường'
symptom = choice(stickness_list)
content = template.replace("{{sick}}", stickness).replace('{{symptom}}',symptom)

message = Message('Đơn xin nghỉ học', to='khains0000@gmail.com', html = template)

x = datetime.datetime.now().strftime("%I:%M %p")

if x == "07:00 AM":
    gmail.send(message)