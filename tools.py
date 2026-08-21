from ddgs import DDGS

def web_search(query):
    text = ""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

        for r in results:
            text += f"{r['title']}\n{r['body']}\n\n"

    return text or "No web results"


def calculator(query):
    try:
        return str(eval(query))
    except:
        return "Invalid math expression"