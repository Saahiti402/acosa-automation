import re

def analyze_message(text):
    """
    Offline fallback AI engine (no API calls).
    Performs simple rule-based extraction for demo and assignment.
    """

    # --- Summary (basic) ---
    summary = text.strip()

    # --- Extract deadline ---
    deadline_match = re.search(r"(tomorrow|today|friday|monday|next week|tonight)", text, re.IGNORECASE)
    deadline = deadline_match.group(0) if deadline_match else None

    # --- Detect type ---
    if "finish" in text.lower() or "done" in text.lower():
        msg_type = "update"
    elif "will do" in text.lower() or "i will" in text.lower():
        msg_type = "task"
    elif "?" in text:
        msg_type = "question"
    else:
        msg_type = "unknown"

    # --- Keywords (simple split) ---
    keywords = [w for w in text.split() if len(w) > 4][:5]

    # --- Owner extraction (just a placeholder) ---
    owner = "unknown"

    return {
        "summary": summary,
        "type": msg_type,
        "owner": owner,
        "deadline": deadline,
        "keywords": keywords
    }