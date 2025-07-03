from azure.communication.email import EmailClient
from dotenv import load_dotenv
from typing import Any
import os
from pipecat.services.llm_service import FunctionCallParams

load_dotenv()

async def _send_email_tool(params: FunctionCallParams):

    args = params.arguments
    subject = args.get("subject")
    plain_text_body = args.get("plain_text_body")

    POLLER_WAIT_TIME = 10

    message = {
        "senderAddress": os.getenv("SENDER_ADDRESS"),
        "recipients": {
            "to": [{"address": os.getenv("RECIPIENT_ADDRESS")}],
        },
        "content": {
            "subject": subject,
            "plainText": plain_text_body,
        } 
    }
    try:
        client = EmailClient.from_connection_string(os.getenv("ACS_CONNECTION_STRING"))

        poller = client.begin_send(message)

        time_elapsed = 0
        while not poller.done():
            print("Email send poller status: " + poller.status())

            poller.wait(POLLER_WAIT_TIME)
            time_elapsed += POLLER_WAIT_TIME

            if time_elapsed > 18 * POLLER_WAIT_TIME:
                raise RuntimeError("Polling timed out.")

        if poller.result()["status"] == "Succeeded":
            result = f"Successfully sent the email (operation id: {poller.result()['id']})"
            print(result)
        else:
            raise RuntimeError(str(poller.result()["error"]))
    
    except Exception as ex:
        print(ex)

    return result