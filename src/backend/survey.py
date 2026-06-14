"""
AromaType - Survey Logic Module
Telegram Mini App for personalized fragrance recommendations
"""

class FragranceProfile:
    """User's fragrance profile based on survey answers"""
    
    def __init__(self):
        self.style = None
        self.situations = []
        self.weather_preference = None
        self.sillage_level = None
        
    def from_survey_responses(self, answers):
        """Convert survey answers into a structured profile"""
        # This will be connected to LLM API
        pass

def ask_question(question_text, options):
    """Template for survey questions"""
    # In production, this will be a Telegram UI component
    return {
        "question": question_text,
        "options": options,
        "type": "single_choice"
    }

# Sample survey flow
SURVEY_QUESTIONS = [
    ask_question("Какой стиль одежды вам ближе?", 
                 ["Классический", "Спортивный", "Романтичный", "Креативный"]),
    ask_question("Для каких ситуаций ищете аромат?",
                 ["Работа/офис", "Свидание", "Повседневность", "Вечеринка"]),
    ask_question("Предпочитаете легкий или насыщенный шлейф?",
                 ["Едва уловимый", "Средний", "Заметный", "Интенсивный"]),
]
