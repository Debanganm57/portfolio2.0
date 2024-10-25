from flask import Flask, request, jsonify
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

app = Flask(__name__)

# Replace with your SendGrid API key
SENDGRID_API_KEY = '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'
sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    from_email = Email('your_email@example.com')  # Your email
    to_email = To(data['email'])
    subject = data['subject']
    content = Content('text/plain', data['message'])
    mail = Mail(from_email, to_email, subject, content)
    
    try:
        response = sg.send(mail)
        return jsonify({'status': 'Email sent', 'response_code': response.status_code}), 200
    except Exception as e:
        return jsonify({'status': 'Failed', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
