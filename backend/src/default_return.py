ai_response_fail_default = [
    {
        "title": "SQLAlchemy Modern Select Statement",
        "options": [
            "from sqlalchemy import select",
            "from sqlalchemy.orm import select",
            "from sqlalchemy.orm import Select",
            "from sqlalchemy.sql import Select"
        ],
        "correct_answer_id": 0,
        "explanation": "For writing queries in modern SQLAlchemy 2.0 style, you import select from sqlalchemy."
    },
    {
        "title": "Python Dictionary Key Check",
        "options": [
            "'key' in my_dict",
            "my_dict.has('key')",
            "my_dict.contains('key')",
            "my_dict.exists('key')"
        ],
        "correct_answer_id": 0,
        "explanation": "In Python, the 'in' keyword is used to check if a key exists in a dictionary."
    },
    {
        "title": "Python Set Add Element",
        "options": [
            "my_set.add(10)",
            "my_set.append(10)",
            "my_set.push(10)",
            "my_set.insert(10)"
        ],
        "correct_answer_id": 0,
        "explanation": "Sets in Python use the add() method to insert a single element."
    },
    {
        "title": "FastAPI Dependency Injection",
        "options": [
            "Depends(get_db)",
            "Inject(get_db)",
            "Provide(get_db)",
            "Use(get_db)"
        ],
        "correct_answer_id": 0,
        "explanation": "FastAPI uses Depends() to declare dependencies such as database sessions."
    },
    {
        "title": "Python List Remove Element by Value",
        "options": [
            "my_list.remove(5)",
            "my_list.pop(5)",
            "del my_list[5]",
            "my_list.delete(5)"
        ],
        "correct_answer_id": 0,
        "explanation": "To remove an element by value in a Python list, use remove(value). pop() removes by index."
    }
]
