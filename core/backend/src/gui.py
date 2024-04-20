
from datetime import datetime
from typing import List, Tuple
from uuid import uuid4

from nicegui import Client, ui

from core.backend.src.consts import TEST_PDF_LOCATION
from core.backend.src.extractor import Extractor
from core.backend.src.gptconnector import GPTConnector

messages: List[Tuple[str, str, str, str]] = []

user_id = str(uuid4())
avatar = f'https://robohash.org/{user_id}?bgset=bg2'


@ui.refreshable
def display_history(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        ui.chat_message(text=text, stamp=stamp, avatar=avatar, sent=own_id == user_id)
    ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')





@ui.page('/')
async def chat_home(client: Client):

    def send_message() -> None:
        extracted = Extractor.pdf_to_string(TEST_PDF_LOCATION)
        gpt_connector = GPTConnector()
        cleaned_text = gpt_connector.clean(extracted).content

        stamp = datetime.utcnow().strftime('%X')
        messages.append((user_id, avatar, text.value, stamp))
        messages.append((user_id, avatar, cleaned_text, stamp))
        text.value = ''
        display_history.refresh()

    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')
    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        with ui.row().classes('w-full no-wrap items-center'):
            with ui.avatar().on('click', lambda: ui.navigate.to(chat_home)):
                ui.image(avatar)
            text = ui.input(placeholder='message').on('keydown.enter', send_message) \
                .props('rounded outlined input-class=mx-3').classes('flex-grow')
        ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io)') \
            .classes('text-xs self-end mr-8 m-[-1em] text-primary')

    await client.connected()  # chat_messages(...) uses run_javascript which is only possible after connecting
    with ui.column().classes('w-full max-w-2xl mx-auto items-stretch'):
        display_history(user_id)


# Press the green button in the gutter to run the script.
if __name__ in {"__main__", "__mp_main__"}:
    ui.run()



"""

"""