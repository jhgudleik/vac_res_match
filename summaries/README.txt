#ЗОНА ОТВЕТСТВЕННОСТИ ПЕРОВА БОРИСА
#Была задача сделать функцию, которая принимает на вход текст (вакансии), инициализирует внутри модель и возвращает саммари
#Была создана функция, далее функция была разбита на модули для удобного добавления в общий проект
Использование из модулей
from vacancy_summarizer import VacancySummarizer

summarizer = VacancySummarizer(use_model="gemini")
df = summarizer.summarize_vacancies(vacancies)

 Использование конкретного генератора
from vacancy_summarizer.gemini_generator import GeminiSummaryGenerator

generator = GeminiSummaryGenerator(api_key="your_api_key")
results = generator.create_dataset_summaries(vacancies)

Использование утилит
from vacancy_summarizer.utils import save_summaries_to_csv, print_summary_results

save_summaries_to_csv(df, "results.csv")

print_summary_results(df)
