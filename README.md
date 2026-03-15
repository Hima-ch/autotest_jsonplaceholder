# API AutoTesting Framework (JSONPlaceholder)

Allure report: https://hima-ch.github.io/autotest_jsonplaceholder/

<a href="#english">English</a> \
<a href="#russian">Русский</a>

<a name="english"></a>

## English

### Description
This project is a professional automated testing framework for the **JSONPlaceholder** API. It demonstrates a scalable architecture for backend testing, focusing on data integrity, clear reporting, and maintainable code.

### Tech Stack
* Python 3.12
* Pytest - Test runner
* Request - HTTP client
* Pydantic - Schema validation
* Loguru - Logging

### Project Structure
* api/ - API clients
* models/ - Pydantic models
* tests/ - Test suites

### Quick Start
git clone https://github.com/Hima-ch/autotest_jsonplaceholder.git \
pip install -r requirements.txt \
pytest tests/ -v -s

<a name="russian"></a>

## Русский

### Описание
Данный проект представляет собой профессиональный фреймворк для автоматизации тестирования **JSONPlaceholder** API. В нем реализована масштабируемая архитектура, ориентированная на проверку целостности данных, прозрачную отчетность и чистоту кода.

### Технологический стек
* Python 3.12
* Pytest - Движок тестов
* Request - Работа с HTTP
* Pydantic - Валидация схем ответов
* Loguru - Логирование

### Структура проекта
* api/ - Клиенты для работы с эндпоинтами
* models/ - Pydantic модели
* tests/ - Тестовые сценарии

### Запуск проекта
git clone https://github.com/Hima-ch/autotest_jsonplaceholder.git \
pip install -r requirements.txt \
pytest tests/ -v -s