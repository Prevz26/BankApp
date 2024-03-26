import flet as ft

def main(page):
    header = ft.Text()
    header.value = "NOTEBOOK"
    header.color = "red"
    page.add(header)
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

ft.app(target=main)
    
# flet run main.py -d