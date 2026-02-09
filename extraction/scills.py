# =============================================================================
# ПАТТЕРНЫ ДЛЯ ИЗВЛЕЧЕНИЯ НАВЫКОВ
# =============================================================================

SKILL_CATEGORIES = {
    'programming_languages': {
        'python': r'\bpython\b', 'java': r'\bjava(?!script)\b',
        'javascript': r'\b(?:javascript|js)\b', 'typescript': r'\btypescript\b',
        'csharp': r'\b(?:c#|csharp)\b', 'cpp': r'\b(?:c\+\+|cpp)\b',
        'go': r'\bgolang\b', 'ruby': r'\bruby\b', 'php': r'\bphp\b',
        'sql': r'\bsql\b', 'bash': r'\bbash\b', 'perl': r'\bperl\b',
    },
    'frameworks': {
        'react': r'\breact\b', 'angular': r'\bangular\b', 'vue': r'\bvue\b',
        'nodejs': r'\bnode\.?js\b', 'django': r'\bdjango\b', 'flask': r'\bflask\b',
        'spring': r'\bspring\b', 'dotnet': r'\b\.net\b', 'rails': r'\brails\b',
        'jquery': r'\bjquery\b', 'express': r'\bexpress\b',
        'mvc': r'\bmvc\b', 'wcf': r'\bwcf\b', 'webapi': r'\bweb\s*api\b',
        'entity_framework': r'\bentity\s*framework\b', 'drupal': r'\bdrupal\b',
    },
    'databases': {
        'mysql': r'\bmysql\b', 'postgresql': r'\bpostgres\b',
        'mongodb': r'\bmongodb\b', 'redis': r'\bredis\b',
        'oracle': r'\boracle\b', 'mssql': r'\b(?:mssql|sql\s*server)\b',
        'elasticsearch': r'\belastic\b', 'sqlite': r'\bsqlite\b',
    },
    'devops_tools': {
        'docker': r'\bdocker\b', 'kubernetes': r'\bkubernetes\b',
        'aws': r'\baws\b', 'azure': r'\bazure\b', 'gcp': r'\bgcp\b',
        'jenkins': r'\bjenkins\b', 'git': r'\bgit\b', 'terraform': r'\bterraform\b',
        'cicd': r'\bci/?cd\b', 'tfs': r'\btfs\b',
    },
    'operating_systems': {
        'linux': r'\blinux\b', 'unix': r'\bunix\b', 'windows': r'\bwindows\b',
    },
    'methodologies': {
        'agile': r'\bagile\b', 'scrum': r'\bscrum\b', 'kanban': r'\bkanban\b',
        'devops': r'\bdevops\b', 'tdd': r'\btdd\b', 'sdlc': r'\bsdlc\b',
        'oop': r'\boop\b', 'solid': r'\bsolid\b',
    },
}

EXPERIENCE_PATTERNS = [
    r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of)?\s*(?:experience)?',
    r'(?:minimum|min)\s*(\d+)\s*(?:years?|yrs?)',
]

EDUCATION_LEVELS = {
    'phd': (r'\bph\.?d\b', 3),
    'master': (r'\bmaster\b', 2),
    'bachelor': (r'\bbachelor\b', 1),
}

print(f" Паттерны загружены")

# пример: объединить все категории из SKILL_CATEGORIES и извлечь скиллы из вакансии
all_patterns = {}
for cat in SKILL_CATEGORIES.values():  # SKILL_CATEGORIES уже есть в ноутбуке
    all_patterns.update(cat)

def extract_skills(text, patterns_dict):
    """
    text: строка вакансии или резюме
    patterns_dict: словарь {skill_name: regex} или объединённый словарь из SKILL_CATEGORIES
    Возвращает строку навыков через запятую.
    """
    text_lower = text.lower()
    found = set()
    import re
    for skill_name, pattern in patterns_dict.items():
        if re.search(pattern, text_lower, re.IGNORECASE):
            found.add(skill_name)
    return ", ".join(sorted(found))

 