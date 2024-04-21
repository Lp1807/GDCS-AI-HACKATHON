from nicegui import ui

if __name__ in {"__main__", "__mp_main__"}:
    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')
    ui.run()
