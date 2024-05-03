from pathlib import Path

import yaml

BASE_DIR = Path(__file__).parent


def main():
    course_info_filename = "course-info.yaml"
    with open(course_info_filename) as f:
        course_info = yaml.safe_load(f.read())

    generate_index_yaml(course_info)

    course_toc = get_course_toc(course_info)
    save_toc_file("toc.yaml", course_toc)

    generate_course_intro()

    for section_name in course_info["content"]:
        generate_section_intro(section_name)

        with open(BASE_DIR / section_name / "section-info.yaml") as f:
            section_info = yaml.safe_load(f.read())
            section_toc = get_section_toc(section_name, section_info)
            save_toc_file(BASE_DIR / section_name / "section-toc.yaml", section_toc)

        for lesson_name in section_info["content"]:
            with open(BASE_DIR / section_name / lesson_name / "lesson-info.yaml") as f:
                lesson_info = yaml.safe_load(f.read())
                lesson_toc = get_lesson_toc(lesson_name, lesson_info)
                save_toc_file(BASE_DIR / section_name / lesson_name / "lesson-toc.yaml", lesson_toc)


def save_toc_file(filename, toc_content: dict):
    with open(filename, "w", encoding='utf-8') as f:
        yaml.dump(toc_content, f, allow_unicode=True, sort_keys=False)


def get_course_toc(course_info: dict) -> dict:
    """
    :param course_info: Конфиг курса JetBrains Academy
    :return: Конфиг Diplodoc
    """

    title_course = course_info["title"]
    content_course = course_info["content"]

    result = {
        "title": title_course,
        "href": "index.yaml",
        "navigation": {
            "logo": {
                "url": "/",
                "text": "IDE EDU",
            }
        },
        "items": []
    }  # константа

    result["items"].append(
        {
            "name": "Введение в курс",
            "href": "course-intro.md",
        }
    )

    for name_module in content_course:
        result["items"].append(
            {
                "name": name_module,
                "include": {
                    "path": f"{name_module}/section-toc.yaml",
                    "mode": "link",
                },
            }
        )

    result["items"][1]["expanded"] = True  # Для наглядности первый модуль после введения сделать раскрытым

    return result


def get_section_toc(section_name: str, section_info: dict) -> dict:
    section_toc = {"title": section_name, "items": []}

    section_toc["items"].append({
        "name": "Введение в модуль",
        "href": "section-intro.md",
    })

    for lesson_name in section_info["content"]:
        section_toc["items"].append({
            "name": lesson_name,
            "include": {
                "path": f"{lesson_name}/lesson-toc.yaml",
                "mode": "link",
            }
        })

    return section_toc


def get_lesson_toc(lesson_name: str, lesson_info: dict) -> dict:
    return {
        "title": lesson_name,
        "items": [
            {
                "name": task_name,
                "href": f"{task_name}/task.md"
            }
            for task_name in lesson_info["content"]
        ]
    }


def generate_index_yaml(course_info: dict):
    index_yaml = {
        "title": course_info["title"],
        "description": course_info.get("summary", "Здесь должно быть описание курса"),
        "links": [
            {
                "title": section_name,
                "description": "Описание к модулю.",
                "href": f"{section_name}/section-intro.md"
            }
            for section_name in course_info["content"]
        ]
    }

    save_toc_file(BASE_DIR / "index.yaml", index_yaml)


def generate_course_intro():
    with open("course-intro.md", "w") as f:
        f.write("#Введение в курс\nЗдесь должно быть введение курса.\n")


def generate_section_intro(section_name: str):
    with open(BASE_DIR / section_name / "section-intro.md", "w") as f:
        f.write("#Введение в модуль\nЗдесь должно быть введение модуля.\n")


if __name__ == '__main__':
    main()
