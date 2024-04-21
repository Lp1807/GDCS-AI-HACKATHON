from datetime import datetime
from typing import List, Tuple
from uuid import uuid4
from nicegui import Client, ui
from consts import TEST_PDF_LOCATION
from paragraphs_extraction_pipeline.utils.pdf2text import PDF2Text
from gptconnector import GPTConnector

# Global variables
messages: List[Tuple[str, str, str, str]] = []
user_id = str(uuid4())
avatar = f'https://robohash.org/{user_id}?bgset=bg2'


# Functions
def send_message() -> None:
    cleaned_text = "Gesù ti ascolta."
    add_message_to_history(cleaned_text)


def add_message_to_history(text: str) -> None:
    stamp = datetime.utcnow().strftime('%X')
    messages.append((user_id, avatar, text, stamp))
    display_history.refresh()


@ui.refreshable
def display_history(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        is_sent_by_user = own_id == user_id
        ui.chat_message(text=text, stamp=stamp, avatar=avatar, sent=is_sent_by_user)
    scroll_to_bottom()


def scroll_to_bottom() -> None:
    ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')


@ui.page('/')
async def chat_home(client: Client):
    setup_ui()
    await client.connected()
    display_history(user_id)


def setup_ui() -> None:
    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')
    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        setup_message_input()


def setup_message_input() -> None:
    with ui.row().classes('w-full no-wrap items-center'):
        with ui.avatar().on('click', lambda: ui.navigate.to(chat_home)):
            ui.image(avatar)
        text_input = ui.input(placeholder='message').on('keydown.enter', send_message).props('rounded outlined input-class=mx-3').classes('flex-grow')
    add_chat_app_description()


def add_chat_app_description() -> None:
    ui.markdown('Simple chat app built with [NiceGUI](https://nicegui.io)').classes('text-xs self-end mr-8 m-[-1em] text-primary')


# Main function
if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
