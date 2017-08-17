from flask import Flask
from flask import request
from flask import Response, make_response
import xml.etree.ElementTree as ET
import time
app = Flask(__name__)


@app.route('/weixin')
def init():
    if(request.args.get("echostr")):
            return request.args.get("echostr")
    print("hello")
    return "hello"


@app.route('/weixin', methods=['Post'])
def getMessage():
    webData = request.data

    recMsg = parse_xml(webData)
    print(recMsg.ToUserName)
    print(recMsg.FromUserName)
    if recMsg.MsgType == 'text':
        print(recMsg.send())
        r = make_response(recMsg.send())
        r.content_type='application/xml'
        return r
    else:
        print("暂且不处理")
        return "success"


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData.find('FromUserName').text, xmlData.find('ToUserName').text, xmlData.find('Content').text)
    elif msg_type == 'image':
        return ImageMsg(xmlData)


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, fromUserName, toUserName, content):
        self.ToUserName = toUserName
        self.FromUserName = fromUserName
        self.CreateTime = int(time.time())
        self.Content = content
        self.MsgType = 'text'
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{0}]]></ToUserName>
        <FromUserName><![CDATA[{1}]]></FromUserName>
        <CreateTime>{2}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{3}]]></Content>
        <MsgId>1234567890123456</MsgId>
        </xml>
        """
        return XmlForm.format(self.FromUserName, self.ToUserName, int(time.time()), self.Content)


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)

if __name__ == '__main__':
        app.run(
                host="0.0.0.0",
                port=int("80"),
                debug = True
        )