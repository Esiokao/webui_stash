import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Message

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print('Receiving message from:', session.peer)
        print('Message addressed from:', envelope.mail_from)
        print('Message addressed to  :', envelope.rcpt_tos)
        print('Message content       :', envelope.content.decode('utf8', errors='replace'))
        return '250 Message accepted for delivery'

# Set hostname to None to bind to all interfaces, or use '127.0.0.1' for localhost only
controller = Controller(CustomSMTPHandler(), hostname=None, port=1025)

# Start the SMTP server
controller.start()

# Print a success message once the server is running
print("SMTP server is running and listening on all interfaces (0.0.0.0) on port 1025.")

# Keep the server running indefinitely
asyncio.get_event_loop().run_forever()
