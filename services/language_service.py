import re


class LanguageService:

    def detect_language(self, question):

        question = question.lower()

        # Explicit language requests
        if "in hindi" in question:
            return "hindi"

        if "in english" in question:
            return "english"

        if "in hinglish" in question:
            return "hinglish"

        # Common Hindi/Hinglish words
        hindi_words = [
            "kya",
            "kaise",
            "kyu",
            "kyun",
            "hai",
            "ka",
            "ki",
            "ke",
            "samjhao",
            "batao",
            "matlab"
        ]

        for word in hindi_words:

            if re.search(rf"\b{word}\b", question):
                return "hinglish"

        return "english"
