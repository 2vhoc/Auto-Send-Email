import yagmail
import time
if __name__ == "__main__":
    main = yagmail.SMTP("Your email", "pass") # pass not is pass email, pass app is correct
    email_send = "xxxxxxx@gmail.com"
    subj = "Chào bạn"
    body = "Tôi là vhoc, được gửi bằng code python"
    path = 0 # use for photo file....
    for _ in range(5): # number of time send
        main.send(to=email_send, subject=subj, contents=body,  attachments= None) # path
        time.sleep(0.1)     
    print("Completed")