import os
import google.generativeai as genai
from typing import Dict
from openai import OpenAI
from dotenv import load_dotenv


def generate_gemini_summary(text: str) -> Dict:
    """
    Генерирует краткое саммари вакансии с помощью Gemini API.

    Args:
        text (str): Текст описания вакансии.

    Returns:
            - summary (str)
            - error (str)
    """
    # Загружаем переменные из .env файла
    load_dotenv()
    # Получаем API ключ из .env
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {
            "error": "GEMINI_API_KEY не установлен"
        }

    # Настройка Gemini API
    
    try:
        genai.configure(api_key=api_key)

        gemini_model = os.getenv("gemini_model")
        model = genai.GenerativeModel(gemini_model)
    except Exception as e:
        return f"Ошибка инициализации модели: {str(e)}"
        

    # Формируем промпт
    prompt = f"""You are an HR-expert extraction algorithm.
Only extract summary of the resume or job vacancy description from the text.  At the first the scills an emploiment required
Job description:
{text}
Summary:"""

    # Генерация ответа
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.3,
                "top_p": 1.0,
                "top_k": 40,
                "max_output_tokens": 500,
            }
        )

        # Возвращаем успешный результат
        return response.text
        

    except Exception as e:
        return {
            "error": str(e)
        }



# ==========================================================================================
# Генерирует краткое саммари вакансии с помощью OpenAI-совместимых моделей через OpenRouter.
# ==========================================================================================

def generate_openai_summary(text: str) -> Dict:
    """
    Генерирует краткое саммари вакансии с помощью OpenAI-совместимых моделей через OpenRouter.

    Args:
        text (str): Текст описания вакансии.

    Returns:
        Dict: Словарь с результатом:
            - summary (str) - саммари текста
            - error (str) - текст ошибки (при наличии)
    """
    
    # Загружаем переменные из .env файла
    load_dotenv()
    # Получаем ключ
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    # Получаем API ключ OpenRouter
    api_key = OPENROUTER_API_KEY  # или OPENAI_API_KEY в зависимости от конфигурации

    if not api_key:
        return {
            "summary": "",
            "error": "OPENROUTER_API_KEY не установлен"
        }

    # Инициализация OpenAI клиента с настройками OpenRouter
    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"  # OpenRouter endpoint
        )
    except Exception as e:
        return {
            "summary": "",
            "error": f"Ошибка инициализации клиента OpenRouter: {str(e)}"
        }

    # Формируем промпт
    prompt = f"""You are an HR-expert extraction algorithm.
Only extract summary of the resume or job vacancy description from the text. Focus on skills and employment requirements.

Job description:
{text}

Summary:"""

    # Генерация ответа
    try:
        response = client.chat.completions.create(
            model = os.getenv("openai_model"),  # или другая модель через OpenRouter
            messages=[
                {
                    "role": "system", 
                    "content": "You are an HR expert specialized in extracting key information from job descriptions and resumes."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=500,
            top_p=1.0,
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Опционально: URL вашего сайта
                "X-Title": "<YOUR_APP_NAME>",  # Опционально: название вашего приложения
            }
        )

        # Извлекаем текст ответа
        summary = response.choices[0].message.content.strip()
        
        # Возвращаем успешный результат
        return {
            "summary": summary,
            "error": ""
        }

    except Exception as e:
        return {
            "summary": "",
            "error": f"Ошибка генерации: {str(e)}"
        }

# Альтернативная версия функции с упрощенным возвратом (только строка)
def generate_openai_summary_simple(text: str) -> str:
    """
    Упрощенная версия функции, возвращающая только строку с саммари или текст ошибки.
    
    Args:
        text (str): Текст описания вакансии.
        
    Returns:
        str: Саммари текста или сообщение об ошибке
    """
    result = generate_openai_summary(text)
    
    if result["error"]:
        return f"Ошибка: {result['error']}"
    else:
        return result["summary"]
