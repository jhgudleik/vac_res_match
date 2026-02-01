# Использование
from vacancy_summarizer import create_summarizer
from vacancy_data_utils import load_sample_vacancies

# Создаем суммаризатор
summarizer = create_summarizer()

# Загружаем данные
vacancies = load_sample_vacancies()

# Создаем CSV саммари
results = summarizer.create_csv_summary(
    vacancies, 
    output_file="my_vacancy_summaries.csv"
)

# CSV файл автоматически создается