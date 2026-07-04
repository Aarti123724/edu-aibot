class MemoryService:

    def build_chat_history(
        self,
        messages,
        limit=6
    ):

        history = ""

        recent_messages = messages[-limit:]

        for message in recent_messages:

            role = message["role"].capitalize()

            history += (
                f"{role}: {message['content']}\n"
            )

        return history