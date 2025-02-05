import smtplib
from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route("/send-email", methods= ["POST"])
def send_handler():

    result= send_email()
    return jsonify({"message": result})

def send_email():

    email= "devlinhahn@gmail.com"
    reciever_email= "dr274400@gmail.com"

    subject= "testing"
    message= "python sent you an email"

    text= f"Subject: {subject}\n\n{message}"

    try:

        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            server.starttls()

            server.login(email, "ncqj wtuh gplf ldxm")

            server.sendmail(email, reciever_email, text)

            return f"Email sent t0 {reciever_email}"

    except Exception as e:

        return str(e)
    

if __name__ == "__main__":
    app.run(debug=True)



