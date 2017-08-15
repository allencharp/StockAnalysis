from flask import Flask
from flask import request
import xml.etree.ElementTree as ET

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
    if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        content = "test"
        replyMsg = TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    else:
        print
        "暂且不处理"
        return "success"


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)


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