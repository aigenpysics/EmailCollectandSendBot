import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    global count
    # Create a MIME message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the message content
    msg.attach(MIMEText(message, 'plain'))

    # Create a SMTP session
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print(f"메세지 전송이 {count}개 완료되었습니다.")
        count += 1

count = 1

with open('emailGathering.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for idx, row in enumerate(reader):
        recipient_email = row[0]  # Assuming email address is in the first column
        #Debug
        #print(f"{idx+1}, {recipient_email}")
        subject = "유입은 있는데 실제 구매가 안이뤄지는 이유"  # Title
        message = """
    안녕하세요. 사장님 리뷰허브 팀장 이채준입니다. 

    우리 모두는 첫인상의 중요성을 알고 있습니다. 새로운 사람을 만나든 새로운 장소를 방문하든 우리는 처음 몇 순간에 보고 경험한 것을 바탕으로 빠르게 의견을 형성하는 경향이 있습니다. 그렇기 때문에 쇼핑몰은 처음부터 방문자에게 긍정적인 인상을 심어주는 것이 매우 중요합니다. 

    리뷰 허브(Review-Hub)에서는 귀사와 같은 쇼핑몰이 최상의 첫인상을 남길 수 있도록 전문적으로 도와드립니다. 저희 리뷰허브 팀은 쇼핑몰의 가장 좋은 면을 보여주고 잠재 방문자에게 가치 있는 통찰력을 제공하는 진실되고 설득력 있는 리뷰 작성에 전념하고 있습니다. 

    연구에 따르면 거의 90%의 소비자가 구매하기 전에 온라인 리뷰를 읽고 긍정적인 리뷰는 전환율을 최대 270%까지 높일 수 있다고 합니다.실제로 저희의 서비스도 좋은 첫인상을 남기는 것 그 이상의 효과 즉, 구매 전환을 높여주고 있습니다.

    소위 “월 1000만원” 번다고 하는 셀러들은 새로운 상품에 대한 리뷰 작업과, 기존 상품들의 상위 리뷰가 안좋게 표시가 된다면 지속적인 리뷰 관리를 하는 것이 현실입니다. 이런 부분은 저희 업체에서 진행 중인 여러 상위 셀러 고객분들만 보아도 인지할 수 있습니다.


    “사장님의 사업이 성공해야 저희도 신규 고객의 유입 / 단골 고객의 유지를 진행할 수 있으며 이익을 취할 수 있습니다”


    긴 글 읽어주시고 리뷰허브를 이용하는 것에 대해 고려해 주셔서 감사합니다. 저희에게 귀하의 쇼핑몰이 번창할 수 있도록 도울 수 있는 기회를 주실 것이라 기대하겠습니다.

    https://reviewhub.imweb.me/

    """  # Content
    #recipient_email = 'asap____@naver.com' #Debug
        sender_email = 'gimjeongheon38@gmail.com'
        sender_password = 'zkcbxmysbswlolqy'
        send_email(sender_email, sender_password, recipient_email, subject, message)
        print("메세지 전송이 완료되었습니다.")