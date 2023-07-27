def reverse_text(text):
    current_idx = len(text) - 1
    end_idx = 0
    while current_idx >= end_idx:
        yield text[current_idx]
        current_idx -= 1
