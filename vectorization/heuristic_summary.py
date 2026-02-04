# -*- coding: utf-8 -*-
"""
Эвристический генератор саммари для вакансий — без классов, в одном модуле.
Извлекает ключевые требования, стек технологий и опыт из текста вакансии.
"""

import re
from typing import Dict, List

# === Конфигурация ===
MAX_TEXT_LENGTH = 3000
MAX_SUMMARY_LENGTH = 500

# === Ключевые слова, указывающие на ТРЕБОВАНИЯ (не маркетинг!) ===
REQUIREMENT_KEYWORDS_ = [
    "required", "required:", "requirements", "must have", "should have",
    "experience", "qualifications", "proficiency", "responsibilities",
    "need", "looking for", "seeking"
]
# === Ключевые слова, указывающие на ТРЕБОВАНИЯ (не маркетинг!) ===
REQUIREMENT_KEYWORDS = [
    "required", "required:", "requirements", "must have", "should have",
    "experience", "qualifications", "proficiency", "responsibilities",
    "duties", "functions", "need", "looking for", "seeking"
]
# === Маркетинговые фразы — всегда игнорируем ===
MARKETING_WORDS = [
    "we offer", "we provide", "benefits", "perks", "insurance",
    "remote", "flexible", "schedule", "team", "culture",
    "competitive salary", "bonus", "stock options", "relocation",
    "learning", "development", "growth opportunities", "what we offer",
    "join us", "apply now", "career path", "work-life balance"
]

# === Технологии для извлечения ===
TECH_KEYWORDS = [
    "python", "java", "javascript", "react", "docker", "kubernetes",
    "aws", "postgresql", "mysql", "mongodb", "typescript", "git",
    "jenkins", "terraform", "ansible", "linux", "sql", "nosql",
    "c++", "c#", "angular", "vue", "node.js", "express.js",
    "spring", "django", "flask", "fastapi", "ruby", "rails",
    "php", "laravel", "symfony", "go", "golang", "rust",
    "swift", "kotlin", "android", "ios", "flutter", "react native",
    "rest", "graphql", "api", "microservices", "cloud", "ci/cd", "devops"
]

# === Опыт — для классификации ===
EXP_KEYWORDS = [
    "experience", "years", "year", "senior", "junior", "mid-level",
    "entry-level", "expert", "advanced", "intermediate", "beginner"
]

# === Основная функция (структурированный вывод) ===
def generate_heuristic_summary(text: str) -> Dict[str, str]:
    if not text or len(text.strip()) < 50:
        return {
            "success": False,
            "summary": "",
            "error": "Текст слишком короткий или пустой"
        }

    text = text[:MAX_TEXT_LENGTH]
    sentences = re.split(r'[.!?]+', text)
    extracted = []

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 10:
            continue
        sentence_lower = sentence.lower()

        # Только предложения с индикаторами требований
        if not any(keyword in sentence_lower for keyword in REQUIREMENT_KEYWORDS):
            continue
        # Исключаем маркетинг
        if any(word in sentence_lower for word in MARKETING_WORDS):
            continue

        extracted.append(sentence)

    # Fallback: если ничего не найдено — берем первые 3 предложения
    if not extracted:
        first_sentences = [s.strip() for s in sentences[:3] if len(s.strip()) > 10]
        summary = "Brief summary:\n• " + "\n• ".join(first_sentences)
        if len(summary) > MAX_SUMMARY_LENGTH:
            summary = summary[:MAX_SUMMARY_LENGTH] + "..."
        return {
            "success": True,
            "summary": summary,
            "error": ""
        }

    # Классификация
    requirements, technologies, experience = [], [], []
    for sentence in extracted:
        sl = sentence.lower()
        if any(tech in sl for tech in TECH_KEYWORDS):
            technologies.append(sentence)
        elif any(exp in sl for exp in EXP_KEYWORDS):
            experience.append(sentence)
        else:
            requirements.append(sentence)

    # Формируем вывод
    summary_parts = []
    if requirements:
        summary_parts.append("KEY REQUIREMENTS:")
        for req in requirements[:5]:
            summary_parts.append(f"• {req}")
    if technologies:
        summary_parts.append("\nTECHNOLOGY STACK:")
        unique_techs = _extract_unique_technologies(technologies, TECH_KEYWORDS)
        for tech in unique_techs[:10]:
            summary_parts.append(f"• {tech}")
    if experience:
        summary_parts.append("\nREQUIRED EXPERIENCE:")
        for exp in experience[:3]:
            summary_parts.append(f"• {exp}")

    if not summary_parts:
        summary_parts.append("Extracted summary:")
        for sentence in extracted[:3]:
            summary_parts.append(f"• {sentence}")

    summary = "\n".join(summary_parts)
    if len(summary) > MAX_SUMMARY_LENGTH:
        summary = summary[:MAX_SUMMARY_LENGTH] + "..."

    return {
        "success": True,
        "summary": summary,
        "error": ""
    }


def _extract_unique_technologies(sentences: List[str], tech_keywords: List[str]) -> List[str]:
    unique_techs = []
    for sentence in sentences:
        for keyword in tech_keywords:
            if keyword in sentence.lower():
                if keyword == "c++": unique_techs.append("C++")
                elif keyword == "c#": unique_techs.append("C#")
                elif keyword == "node.js": unique_techs.append("Node.js")
                elif keyword == "express.js": unique_techs.append("Express.js")
                elif keyword == "react native": unique_techs.append("React Native")
                elif keyword == "ci/cd": unique_techs.append("CI/CD")
                elif keyword == "machine learning": unique_techs.append("Machine Learning")
                elif keyword == "data science": unique_techs.append("Data Science")
                else:
                    unique_techs.append(keyword.capitalize())
    return list(set(unique_techs))


