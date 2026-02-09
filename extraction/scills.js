
```javascript
// ============================================================================
// КОД ДЛЯ N8N NODE (JAVASCRIPT)
// Извлечение таргетов из вакансий
// ============================================================================

// ПАТТЕРНЫ ДЛЯ ИЗВЛЕЧЕНИЯ
const PROGRAMMING_LANGUAGES = {
  'python': /\bpython\b/i,
  'java': /\bjava(?!script)\b/i,
  'javascript': /\b(?:javascript|js)\b/i,
  'typescript': /\btypescript\b/i,
  'csharp': /\b(?:c#|csharp|c\s*sharp)\b/i,
  'cpp': /\b(?:c\+\+|cpp)\b/i,
  'go': /\b(?:golang|go\s+lang)\b/i,
  'rust': /\brust\b/i,
  'ruby': /\bruby\b/i,
  'php': /\bphp\b/i,
  'swift': /\bswift\b/i,
  'kotlin': /\bkotlin\b/i,
  'scala': /\bscala\b/i,
  'perl': /\bperl\b/i,
  'sql': /\bsql\b/i,
  'bash': /\bbash\b/i,
  'powershell': /\bpowershell\b/i,
};

const FRAMEWORKS = {
  'react': /\breact(?:\.?js)?\b/i,
  'angular': /\bangular(?:\.?js)?\b/i,
  'vue': /\bvue(?:\.?js)?\b/i,
  'jquery': /\bjquery\b/i,
  'bootstrap': /\bbootstrap\b/i,
  'nextjs': /\bnext\.?js\b/i,
  'nodejs': /\bnode\.?js\b/i,
  'express': /\bexpress(?:\.?js)?\b/i,
  'django': /\bdjango\b/i,
  'flask': /\bflask\b/i,
  'fastapi': /\bfastapi\b/i,
  'spring': /\bspring(?:\s*boot)?\b/i,
  'hibernate': /\bhibernate\b/i,
  'dotnet': /\b(?:\.net|dotnet|asp\.?net)\b/i,
  'rails': /\b(?:ruby\s+on\s+)?rails\b/i,
  'laravel': /\blaravel\b/i,
  'mvc': /\b(?:asp\.?net\s+)?mvc\b/i,
  'wcf': /\bwcf\b/i,
  'entity_framework': /\bentity\s*framework\b/i,
  'webapi': /\bweb\s*api\b/i,
  'drupal': /\bdrupal\b/i,
};

const DATABASES = {
  'mysql': /\bmysql\b/i,
  'postgresql': /\b(?:postgresql|postgres)\b/i,
  'sqlite': /\bsqlite\b/i,
  'oracle': /\boracle(?:\s+db)?\b/i,
  'mssql': /\b(?:ms\s*sql|sql\s*server|mssql)\b/i,
  'mongodb': /\bmongodb?\b/i,
  'redis': /\bredis\b/i,
  'elasticsearch': /\belastic\s*search\b/i,
  'cassandra': /\bcassandra\b/i,
  'dynamodb': /\bdynamodb\b/i,
  'mariadb': /\bmariadb\b/i,
};

const DEVOPS_TOOLS = {
  'docker': /\bdocker\b/i,
  'kubernetes': /\b(?:kubernetes|k8s)\b/i,
  'aws': /\b(?:aws|amazon\s+web\s+services)\b/i,
  'azure': /\b(?:azure|microsoft\s+azure)\b/i,
  'gcp': /\b(?:gcp|google\s+cloud)\b/i,
  'terraform': /\bterraform\b/i,
  'ansible': /\bansible\b/i,
  'jenkins': /\bjenkins\b/i,
  'git': /\bgit(?!hub|lab)\b/i,
  'gitlab': /\bgitlab\b/i,
  'github': /\bgithub\b/i,
  'tfs': /\btfs\b/i,
  'cicd': /\b(?:ci\/?cd|continuous\s+integration)\b/i,
};

const OPERATING_SYSTEMS = {
  'linux': /\blinux\b/i,
  'unix': /\bunix\b/i,
  'windows': /\bwindows(?:\s+server)?\b/i,
  'macos': /\b(?:macos|mac\s+os|osx)\b/i,
};

const METHODOLOGIES = {
  'agile': /\bagile\b/i,
  'scrum': /\bscrum\b/i,
  'kanban': /\bkanban\b/i,
  'waterfall': /\bwaterfall\b/i,
  'devops': /\bdevops\b/i,
  'tdd': /\btdd\b/i,
  'sdlc': /\bsdlc\b/i,
  'oop': /\b(?:oop|object[\-\s]?oriented)\b/i,
  'solid': /\bsolid\b/i,
};

const EXPERIENCE_PATTERNS = [
  /(\d+)\+?\s*(?:years?|yrs?|года|лет)\s*(?:of)?\s*(?:experience|exp|опыта)?/gi,
  /(?:experience|exp|опыт)\s*(?:of|от)?\s*(\d+)\+?\s*(?:years?|yrs?|года|лет)/gi,
  /(?:minimum|min|at\s+least|минимум)\s*(\d+)\s*(?:years?|yrs?|года|лет)/gi,
];

const EDUCATION_LEVELS = {
  'phd': /\b(?:ph\.?d|doctorate|doctoral|аспирантура|кандидат\s+наук)\b/i,
  'master': /\b(?:master|m\.?s\.?|m\.?sc|магистр)\b/i,
  'bachelor': /\b(?:bachelor|b\.?s\.?|b\.?sc|b\.?a\.?|бакалавр)\b/i,
};

const SKILL_CATEGORIES = {
  'programming_languages': PROGRAMMING_LANGUAGES,
  'frameworks': FRAMEWORKS,
  'databases': DATABASES,
  'devops_tools': DEVOPS_TOOLS,
  'operating_systems': OPERATING_SYSTEMS,
  'methodologies': METHODOLOGIES,
};

// Иерархия навыков
const SKILL_HIERARCHY = {
  'postgresql': ['sql'],
  'mysql': ['sql'],
  'mssql': ['sql'],
  'oracle': ['sql'],
  'mariadb': ['sql'],
  'react': ['javascript'],
  'angular': ['javascript'],
  'vue': ['javascript'],
  'nodejs': ['javascript'],
  'jquery': ['javascript'],
  'typescript': ['javascript'],
  'nextjs': ['javascript'],
  'django': ['python'],
  'flask': ['python'],
  'fastapi': ['python'],
  'spring': ['java'],
  'hibernate': ['java'],
  'dotnet': ['csharp'],
  'mvc': ['csharp', 'dotnet'],
  'wcf': ['csharp', 'dotnet'],
  'entity_framework': ['csharp', 'dotnet'],
  'webapi': ['csharp', 'dotnet'],
  'kubernetes': ['docker'],
  'gitlab': ['git'],
  'github': ['git'],
  'tfs': ['git'],
};

// ============================================================================
// ФУНКЦИИ
// ============================================================================

function cleanRtfText(rtfText) {
  if (!rtfText) return '';
  
  let text = rtfText;
  
  // Удаляем RTF control words
  text = text.replace(/\\[a-z]+\d*\s?/g, '');
  
  // Удаляем фигурные скобки
  text = text.replace(/[{}]/g, '');
  
  // Удаляем escape-последовательности
  text = text.replace(/\\'[0-9a-fA-F]{2}/g, '');
  
  // Удаляем обратные слеши
  text = text.replace(/\\/g, '');
  
  // Заменяем множественные пробелы на одиночные
  text = text.replace(/\s+/g, ' ');
  
  // Trim
  text = text.trim();
  
  return text;
}

function extractSkills(text, patterns) {
  const found = new Set();
  
  for (const [skillName, pattern] of Object.entries(patterns)) {
    if (pattern.test(text)) {
      found.add(skillName);
    }
  }
  
  return found;
}

function extractExperienceYears(text) {
  const years = [];
  
  for (const pattern of EXPERIENCE_PATTERNS) {
    const matches = [...text.matchAll(pattern)];
    for (const match of matches) {
      const year = parseInt(match[1]);
      if (!isNaN(year)) {
        years.push(year);
      }
    }
  }
  
  return years.length > 0 ? Math.max(...years) : 0;
}

function extractEducationLevel(text) {
  const levelScores = {
    'phd': 3,
    'master': 2,
    'bachelor': 1
  };
  
  for (const [level, pattern] of Object.entries(EDUCATION_LEVELS)) {
    if (pattern.test(text)) {
      return levelScores[level];
    }
  }
  
  return 0;
}

function extractAllTargets(text) {
  const result = {};
  
  // Извлекаем навыки по категориям
  for (const [categoryName, patterns] of Object.entries(SKILL_CATEGORIES)) {
    result[categoryName] = extractSkills(text, patterns);
  }
  
  // Извлекаем опыт и образование
  result.experience_years = extractExperienceYears(text);
  result.education_level = extractEducationLevel(text);
  
  return result;
}

function expandSkills(targets) {
  const expanded = {};
  
  for (const [category, skills] of Object.entries(targets)) {
    if (skills instanceof Set) {
      const expandedSet = new Set(skills);
      
      // Добавляем родительские навыки из иерархии
      for (const skill of skills) {
        if (SKILL_HIERARCHY[skill]) {
          for (const parentSkill of SKILL_HIERARCHY[skill]) {
            expandedSet.add(parentSkill);
          }
        }
      }
      
      expanded[category] = expandedSet;
    } else {
      expanded[category] = skills;
    }
  }
  
  return expanded;
}

function formatTargets(targets) {
  const formatted = {};
  
  for (const [key, value] of Object.entries(targets)) {
    if (value instanceof Set) {
      formatted[key] = Array.from(value).sort();
    } else {
      formatted[key] = value;
    }
  }
  
  return formatted;
}

// ============================================================================
// ОСНОВНАЯ ЛОГИКА
// ============================================================================

const items = $input.all();
const results = [];

for (const item of items) {
  // Получаем текст вакансии из поля 'data'
  const vacancyText = item.json.data || '';
  
  if (!vacancyText) {
    results.push({
      json: {
        success: false,
        error: 'No data field found',
        targets: null
      }
    });
    continue;
  }
  
  try {
    // Шаг 1: Очищаем RTF
    const cleanText = cleanRtfText(vacancyText);
    
    // Шаг 2: Извлекаем таргеты
    let targets = extractAllTargets(cleanText);
    
    // Шаг 3: Расширяем навыки по иерархии
    targets = expandSkills(targets);
    
    // Шаг 4: Форматируем для JSON (Set -> Array)
    const formattedTargets = formatTargets(targets);
    
    // Шаг 5: Создаем сводку
    const totalSkills = Object.entries(formattedTargets)
      .filter(([key]) => !['experience_years', 'education_level'].includes(key))
      .reduce((sum, [, skills]) => sum + skills.length, 0);
    
    const summary = {
      total_skills_found: totalSkills,
      programming_languages_count: formattedTargets.programming_languages?.length || 0,
      frameworks_count: formattedTargets.frameworks?.length || 0,
      databases_count: formattedTargets.databases?.length || 0,
      devops_tools_count: formattedTargets.devops_tools?.length || 0,
      operating_systems_count: formattedTargets.operating_systems?.length || 0,
      methodologies_count: formattedTargets.methodologies?.length || 0,
      experience_required_years: formattedTargets.experience_years || 0,
      education_level: formattedTargets.education_level || 0
    };
    
    // Формируем результат
    results.push({
      json: {
        success: true,
        targets: formattedTargets,
        summary: summary,
        debug_info: {
          original_length: vacancyText.length,
          cleaned_length: cleanText.length,
          clean_preview: cleanText.substring(0, 200) + (cleanText.length > 200 ? '...' : '')
        }
      }
    });
    
  } catch (error) {
    results.push({
      json: {
        success: false,
        error: error.message,
        error_type: error.name,
        targets: null
      }
    });
  }
}

return results;
```
