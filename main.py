import pathlib

views_translations = {
    "Authors": "Авторы",
    "Documents": "Документы",
}

cwd = pathlib.Path.cwd()
home_view_file_paths = cwd.glob(r"Views\Home\*")
views_file_paths = list(set(cwd.glob(r"Views\*\*")) - set(home_view_file_paths))

for f in views_file_paths:
    with open(f, "r", encoding="utf-8") as file:
        view_name = f.parent.name
        translation = views_translations[view_name]
        content = file.read()

        match f.stem:
            case "Create":
                content = content.replace(
                    'ViewData["Title"] = "Create";',
                    f'ViewData["Title"] = "Создание – {translation}";',
                )
                content = content.replace("<h1>Create</h1>", "<h1>Создание</h1>")
                content = content.replace(
                    f"<h4>{view_name}</h4>", f"<h4>{translation}</h4>"
                )
                content = content.replace('value="Create"', 'value="Создать"')
                content = content.replace("Back to List", "Назад к списку")
            case "Delete":
                content = content.replace(
                    'ViewData["Title"] = "Delete";',
                    f'ViewData["Title"] = "Удаление – {translation}";',
                )
                content = content.replace("<h1>Delete</h1>", "<h1>Удаление</h1>")
                content = content.replace(
                    "Are you sure you want to delete this?",
                    "Вы уверены, что хотите удалить?",
                )
                content = content.replace(
                    f"<h4>{view_name}</h4>", f"<h4>{translation}</h4>"
                )
                content = content.replace('value="Delete"', 'value="Удалить"')
                content = content.replace("Back to List", "Назад к списку")
            case "Details":
                content = content.replace(
                    'ViewData["Title"] = "Details";',
                    f'ViewData["Title"] = "Детали – {translation}";',
                )
                content = content.replace("<h1>Details</h1>", "<h1>Детали</h1>")
                content = content.replace(
                    f"<h4>{view_name}</h4>", f"<h4>{translation}</h4>"
                )
                content = content.replace(
                    ">Edit</a>",
                    ">Редактировать</a>",
                )
                content = content.replace("Back to List", "Назад к списку")
            case "Edit":
                content = content.replace(
                    'ViewData["Title"] = "Edit";',
                    f'ViewData["Title"] = "Редактирование – {translation}";',
                )
                content = content.replace("<h1>Edit</h1>", "<h1>Редактирование</h1>")
                content = content.replace(
                    f"<h4>{view_name}</h4>", f"<h4>{translation}</h4>"
                )
                content = content.replace('value="Save"', 'value="Сохранить"')
                content = content.replace("Back to List", "Назад к списку")
            case "Index":
                content = content.replace(
                    'ViewData["Title"] = "Index";',
                    f'ViewData["Title"] = "Список – {translation}";',
                )
                content = content.replace("<h1>Index</h1>", f"<h1>{translation}</h1>")
                content = content.replace("Create New", "Создать")
                content = content.replace(
                    'asp-route-id="@item.Id">Edit</a>',
                    'asp-route-id="@item.Id">Редактировать</a>',
                )
                content = content.replace(
                    'asp-route-id="@item.Id">Details</a>',
                    'asp-route-id="@item.Id">Детали</a>',
                )
                content = content.replace(
                    'asp-route-id="@item.Id">Delete</a>',
                    'asp-route-id="@item.Id">Удалить</a>',
                )

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
